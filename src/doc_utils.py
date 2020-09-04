from enum import Enum


SKIP = False

class Options(Enum):
    ATTEST = 1
    NO_ATTEST = 2
    LIST = 3

def print_skip( s ):
    lines = s.split('\n')
    if SKIP and len( lines ) > 3:
        print( lines[0] + '\n...\n' + lines[-1], end='')
    else:
        print( '\n'.join(lines), end='')

def set_skip( skip ):
    global SKIP
    SKIP=skip
