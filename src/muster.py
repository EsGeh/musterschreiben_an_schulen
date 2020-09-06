#!/usr/bin/env python3

import document
from doc_utils import Options, Bundesland, set_skip, print_err

import argparse
import sys


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument(
            '-s', '--skip',
            action='store_true',
            default=False,
            help="in output, abbreviate long text blocks with ..."
    )
    parser.add_argument(
            '-o', '--opt',
            required=True,
            help='one of '+ ', '.join(f"'{x.name}'" for x in Options)
    )
    parser.add_argument(
            '-g', '--glaubhaftmachung',
            action='store_true',
            default=False,
            help='glaubhaftmachung'
    )
    parser.add_argument(
            'bundesland',
            help='one of '+ ', '.join(f"'{x.name}'" for x in Bundesland)
    )
    args = parser.parse_args()

    if args.skip:
        set_skip( True )
    try:
        options = Options[args.opt]
    except KeyError:
        sys.exit("invalid option")
    try:
        bundesland = Bundesland[args.bundesland]
    except KeyError:
        sys.exit("invalid Bundesland")
    print_err( f"Bundesland: {bundesland.name}" )
    print_err( f"options: {options.name}" )
    print_err( f"glaubhaftmachung: {args.glaubhaftmachung}" )
    print_err( f"---------------------------------------------" )

    print(
            document.generate(
                options = options,
                glaubhaftmachung = args.glaubhaftmachung,
                bundesland = bundesland
            )
    )
