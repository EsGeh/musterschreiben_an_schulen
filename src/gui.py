#!/usr/bin/env python3

from doc_utils import Options, Bundesland, set_skip, print_err
import document

import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext


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
        self.set_output()
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
        self.vsb = tk.Scrollbar(
                self,
                orient="vertical",
                # command=self.on_scroll
        )
        self.vsb.pack(side="right",fill="y")
        self.vsb.config(
                # command = self.text_gui.yview
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

    '''
    def on_scroll(self, *args):
        # print( args )
        self.text_gui.yview( *args )
    '''

    def set_output(self):
        self.text_gui.delete(
                1.0,
                tk.END
        )
        doc = document.generate(
            options = self.options,
            glaubhaftmachung = self.glaubhaftmachung,
            bundesland = self.bundesland
        )
        self.text_gui.insert(
                tk.END,
                doc
        )

    def set_bundesland( self, event ):
        self.bundesland = Bundesland[ self.bundesland_gui.get() ]
        print( self.bundesland )
        self.set_output()

    def set_options(self):
        self.options = Options(self.options_var.get())
        print( self.options )
        self.set_output()

    def set_glaubhaftmachung(self):
        self.glaubhaftmachung = bool(self.glaubhaftmachung_var.get())
        print( self.glaubhaftmachung )
        self.set_output()

def on_scroll( *args):
    for view in views:
        view.text_gui.yview( *args )

def add_view():
    # global main_frames
    view = View(root)
    views.append( view )

def del_view():
    if len(views) > 1:
        view = views.pop()
        view.pack_forget()
        view.grid_forget()

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
