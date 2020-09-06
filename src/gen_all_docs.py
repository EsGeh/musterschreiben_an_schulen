#!/usr/bin/env python3

import document
from doc_utils import Options, Bundesland, set_skip, print_err

import argparse
from pathlib import Path
import sys
import subprocess
import shutil


output_formats = ['txt', 'docx', 'pdf']

def convert_file(
        input,
        output
):
    subprocess.run(
            ["pandoc", "--pdf-engine=xelatex", "-o", output, input]
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument(
            '-s', '--skip',
            action='store_true',
            default=False,
            help="in output, abbreviate long text blocks with ..."
    )
    parser.add_argument(
            '-!', '--overwrite',
            action='store_true',
            default=False,
            help='overwrite output directory, if existing'
    )
    parser.add_argument(
            'output_dir',
            default="output",
            metavar="OUPUT_DIR",
            nargs='?',
            type=Path,
            help='where to store all generated output files'
    )
    parser.add_argument(
            '-f', '--format',
            action='append',
            help="output documents in some additional format: 'txt', 'doxc', 'pdf'. default: <all formats>"
    )
    args = parser.parse_args()

    if args.skip:
        set_skip( True )
    overwrite = args.overwrite
    output_dir = args.output_dir
    output_formats = args.format if args.format else output_formats
    if output_dir.is_dir() and output_dir.exists() and overwrite:
        shutil.rmtree( output_dir )
    if output_dir.is_dir() and output_dir.exists():
        sys.exit( f"directory {output_dir} already exists!")
    if not(output_dir.is_dir()) and not(output_dir.exists()):
        output_dir.mkdir()
        for file_format in output_formats + ['md']:
            (output_dir / file_format) . mkdir()
    for bundesland in Bundesland:
        doc_dict = {}
        # collect all documents for this bundesland:
        for options in Options:
            for glaubhaftmachung in (False, True):
                doc = document.generate(
                        options = options,
                        glaubhaftmachung = glaubhaftmachung,
                        bundesland = bundesland
                )
                if doc not in doc_dict:
                    doc_dict[ doc ] = [(options, glaubhaftmachung)]
                else:
                    doc_dict[ doc ].append((options, glaubhaftmachung))
        # write all documents for this bundesland to file:
        print_err( "Bundesland: " + bundesland.name )
        for doc, opts_and_glaubhaft in doc_dict.items():
            filename = f"{bundesland.name}"
            # print( f"opts: {opts_and_glaubhaft}" )
            for options in Options:
                if all(x[0] == options for x in opts_and_glaubhaft):
                    filename += ('_' + options.name)
            for glaubhaft in (False,True):
                if all(x[1] == glaubhaft for x in opts_and_glaubhaft):
                    filename += ('_glaubhaft' if glaubhaft else '')
            filename_markdown = (output_dir / 'md' / filename) . with_suffix( '.md' )
            with open(filename_markdown, 'w') as f:
                print_err( f"  writing: {filename_markdown}" )
                f.write( doc )
            for file_format in output_formats:
                filename_current = (output_dir / file_format / filename ) . with_suffix( '.' + file_format)
                print_err( f"  writing: {filename_current}" )
                convert_file( filename_markdown, filename_current )
