#!/usr/bin/env python3

from enum import Enum


skip = False

class Options(Enum):
    ATTEST = 1
    NO_ATTEST = 2
    LIST = 3

def print_skip( s ):
    lines = s.split('\n')
    if skip and len( lines ) > 3:
        print( lines[0] + '\n...\n' + lines[-1], end='')
    else:
        print( '\n'.join(lines), end='')
