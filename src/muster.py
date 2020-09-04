#!/usr/bin/env python3

import document
from doc_utils import Options, set_skip

import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument(
            '-s', '--skip',
            action='store_true',
            default=False,
            help=''
    )
    parser.add_argument(
            '-o', '--opt',
            type=int,
            required=True,
            help='1: attest, 2: no attest, 3: list'
    )
    parser.add_argument(
            '-g', '--glaubhaftmachung',
            action='store_true',
            default=False,
            help='glaubhaftmachung'
    )
    parser.add_argument(
            'bundesland',
            help=''
    )
    args = parser.parse_args()

    if args.opt == 1:
        options = Options.ATTEST
    elif args.opt == 2:
        options = Options.NO_ATTEST
    else:
        print( f"opt: {args.opt}" )
        options = Options.LIST
    if args.skip:
        set_skip( True )
    print( f"options: {options}" )
    print( f"glaubhaftmachung: {args.glaubhaftmachung}" )
    print( f"DOCUMENT:" )
    print( f"-------------------------------" )

    document.generate(
            options = options,
            glaubhaftmachung = args.glaubhaftmachung,
            bundesland = args.bundesland
    )
