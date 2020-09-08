#!/usr/bin/env python3

from doc_utils import Options, Bundesland, set_skip, print_err
import document

import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext
import difflib
from pprint import pprint


views = []

class View(tk.Frame):
    def __init__(self, parent):
        super().__init__(
                parent,
                relief = tk.RAISED,
                # borderwidth = 2
        )
        self.bundesland = Bundesland.BW
        self.options = Options.ATTEST
        self.glaubhaftmachung = False
        self.init_ui()
    def init_ui(self):
        self.options_var = tk.IntVar(0)
        self.glaubhaftmachung_var = tk.IntVar(0)
        self.pack(
                side = tk.LEFT,
                fill=tk.BOTH,
                expand = True
        )
        self.buttons_frame = ttk.Frame(
                self,
                relief = tk.RAISED,
                borderwidth = 1
        )

        self.buttons_frame.pack(
                fill=tk.X,
        )

        self.bundesland_gui = ttk.Combobox(
                self.buttons_frame,
                values = [x.name for x in Bundesland],
        )
        self.bundesland_gui.pack(
                fill = tk.X,
                expand = True,
        )
        self.bundesland_gui.current(0)
        self.bundesland_gui.bind("<<ComboboxSelected>>", self.set_bundesland)

        tk.Radiobutton(
                self.buttons_frame,
                text="Attest",
                padx = 20,
                variable = self.options_var,
                value = Options.ATTEST.value,
                command = self.set_options,
        ).pack()
        tk.Radiobutton(
                self.buttons_frame,
                text="kein Attest",
                padx = 20,
                variable = self.options_var,
                value = Options.NO_ATTEST.value,
                command = self.set_options,
        ).pack()
        tk.Radiobutton(
                self.buttons_frame,
                text="Liste",
                padx = 20,
                variable = self.options_var,
                value = Options.LIST.value,
                command = self.set_options,
        ).pack()
        tk.Checkbutton(
                self.buttons_frame,
                text = "glaubhaftmachung",
                variable = self.glaubhaftmachung_var,
                command = self.set_glaubhaftmachung,
        ).pack()


        self.text_gui = tk.Text(
                self
        )
        self.text_gui.config(
                wrap = tk.NONE
        )
        self.vsb = tk.Scrollbar(
                self,
                orient="vertical",
        )
        self.vsb.pack(side="right",fill="y")
        self.vsb.config(
                command=on_scroll
        )
        self.text_gui['yscrollcommand'] = self.vsb.set 
        self.text_gui.config(
                width = 40,
        )
        self.text_gui.pack(
                fill = tk.BOTH,
                expand = True
        )

    def set_bundesland( self, event ):
        self.bundesland = Bundesland[ self.bundesland_gui.get() ]
        print( self.bundesland )
        set_output()

    def set_options(self):
        self.options = Options(self.options_var.get())
        print( self.options )
        set_output()

    def set_glaubhaftmachung(self):
        self.glaubhaftmachung = bool(self.glaubhaftmachung_var.get())
        print( self.glaubhaftmachung )
        set_output()

def set_output():
    differ = difflib.Differ()
    first_view = views[0]
    first_doc = document.generate(
        options = first_view.options,
        glaubhaftmachung = first_view.glaubhaftmachung,
        bundesland = first_view.bundesland
    )

    """ format:
        [ [(rel1, doc_0_line_0), (rel1, doc_1_line_0), (rel2, doc_2_line_0), ...],
          ...
        ]
        where
            rel1, rel2, ... one of
                "=": if line is equal to first_doc
                "e": if the line differ from first doc
            doc_i_line_j can also be 'None': a dummy line in order to keep correspondence between matching lines

    """
    docs_marked_lines = [[("=", line)] for line in first_doc.splitlines(keepends = True)]

    for view_nr, view in enumerate(views[1:], 1):
        doc = document.generate(
            options = view.options,
            glaubhaftmachung = view.glaubhaftmachung,
            bundesland = view.bundesland
        )
        diff = differ.compare(
                first_doc.splitlines(keepends = True),
                doc.splitlines(keepends = True)
        )
        b = []
        last_matching_line = -1
        line_nr = 0
        for diff_line_nr, line in enumerate(diff):
            # line common in both sequences:
            if line.startswith( "  " ):
                line_nr = dump_lines(
                        line_nr,
                        docs_marked_lines,
                        last_matching_line,
                        b,
                        view_nr
                )
                b.clear()
                docs_marked_lines[line_nr].append(
                        ('=', line[2:])
                )
                last_matching_line = line_nr
                line_nr += 1
            elif line.startswith( "+ " ):
                b += [("e", line[2:])]
            elif line.startswith( "- " ):
                line_nr += 1
        # pprint( list(enumerate(docs_marked_lines)) )
        if len(b) > 0:
            # print( f"b: {b}, line_nr: {line_nr}" )
            line_nr = dump_lines(
                    line_nr,
                    docs_marked_lines,
                    last_matching_line,
                    b,
                    view_nr
            )
            b.clear()

    first_view.text_gui.config(
            state=tk.NORMAL
    )
    first_view.text_gui.delete(
            1.0,
            tk.END
    )
    for view in views:
        view.text_gui.tag_config(
                "dummy",
                background="SkyBlue1"
        )
        for index, color in enumerate(("red", "green", "blue")):
            view.text_gui.tag_config(
                    "hi" + str(index),
                    background=color
            )
    for view in views[1:]:
        view.text_gui.config(
                state=tk.NORMAL
        )
        view.text_gui.delete(
                1.0,
                tk.END
        )
    for line in docs_marked_lines:
        first_doc_edit_type = line[0][0]
        first_doc_line_content = line[0][1]
        if first_doc_line_content is not None:
            first_view.text_gui.insert(
                    tk.END,
                    first_doc_line_content
            )
        else:
            first_view.text_gui.insert(
                    tk.END,
                    "----\n",
                    ["dummy"]
            )

        for view_nr, view, other_doc_line in zip(range(1000), views[1:], line[1:]):
            other_doc_edit_type = other_doc_line[0]
            other_doc_line_content = other_doc_line[1]
            if other_doc_line_content is not None:
                if other_doc_edit_type == "e":
                    view.text_gui.insert(
                            tk.END,
                            other_doc_line_content,
                            "hi" + str(view_nr)
                    )
                else:
                    view.text_gui.insert(
                            tk.END,
                            other_doc_line_content,
                    )
            else:
                view.text_gui.insert(
                        tk.END,
                        "----\n",
                        ["dummy"]
                )
    first_view.text_gui.config(
            state=tk.DISABLED
    )
    for view in views[1:]:
        view.text_gui.config(
                state=tk.DISABLED
        )

def dump_lines(
        line_nr,
        docs_marked_lines,
        last_matching_line,
        b,
        view_nr,
):
    # skip dummy lines
    if line_nr < len(docs_marked_lines):
        while docs_marked_lines[line_nr][0][1] is None:
            line_nr += 1
    # how many lines does the other text exceed the first one?
    diff_lines = (last_matching_line + len(b)) - line_nr + 1
    # do we need dummy lines in the previous docs?
    for _ in range( diff_lines ):
        docs_marked_lines.insert(
                line_nr,
                [("=", None) for _ in range(view_nr)]
        )
        line_nr += 1
    # print( f"difflines: {diff_lines}" )
    # do we need dummy lines in the other doc?
    for _ in range( -diff_lines ):
        b.append(
                ("=", None)
        )
    for index in range(0, len(b)):
        docs_marked_lines[last_matching_line+1+index].append(
                b[index]
        )
    return line_nr

def on_scroll( *args):
    for view in views:
        view.text_gui.yview( *args )

def add_view():
    # global main_frames
    view = View(root)
    views.append( view )
    set_output()

def del_view():
    if len(views) > 1:
        view = views.pop()
        view.pack_forget()
        view.grid_forget()


if __name__ == "__main__":

    root = tk.Tk()
    root.title("Explore a polymorphic document")

    frame_view_buttons = tk.Frame(
            root,
            relief = tk.RIDGE,
            borderwidth = 2
    )
    frame_view_buttons.pack(
            fill = tk.X,
            # expand = True
    )

    button_del_view = tk.Button(
            frame_view_buttons,
            text = "-",
            command = del_view
    )
    button_del_view.pack(
            side = tk.LEFT
    )
    button_add_view = tk.Button(
            frame_view_buttons,
            text = "+",
            command = add_view
    )
    button_add_view.pack(
            side = tk.LEFT
    )

    add_view()

    root.mainloop()
