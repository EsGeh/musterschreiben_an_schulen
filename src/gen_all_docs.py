#!/usr/bin/env python3

import document
from doc_utils import Options, Bundesland, set_skip

import argparse
from pathlib import Path
import sys


def print_err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument(
            '-s', '--skip',
            action='store_true',
            default=False,
            help=''
    )
    parser.add_argument(
            '-!', '--overwrite',
            action='store_true',
            default=False,
            help=''
    )
    parser.add_argument(
            'output_dir',
            default="output",
            nargs='?',
            type=Path,
            help='where to store all generated output files'
    )
    args = parser.parse_args()

    if args.skip:
        set_skip( True )
    output_dir = args.output_dir
    overwrite = args.overwrite
    if output_dir.is_dir() and output_dir.exists() and not(overwrite):
        sys.exit( f"directory {output_dir} already exists!")
    if not(output_dir.is_dir()) and not(output_dir.exists()):
        output_dir.mkdir()
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
            filename = output_dir / filename
            print_err( f"  writing: {filename}" )
            with open(filename, 'w') as f:
                f.write( doc )
