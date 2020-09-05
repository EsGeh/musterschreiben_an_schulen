from enum import Enum
import itertools


SKIP = False

_OPTIONS = dict(zip(range(0,100), [
        ['attest', 'ATTEST'],
        ['no_attest', 'NO_ATTEST'],
        ['list', 'LIST'],
    ] ))

Options = Enum(
        value = "Options",
        names=itertools.chain.from_iterable(
            itertools.product(v, [k]) for k, v in _OPTIONS.items()
        )
)

_BUNDESLAND = dict(zip(range(0,100), [
        ['Baden-Württemberg', 'BW'],
        ['Bayern', 'BY'],
        ['Berlin', 'BE'],
        ['Brandenburg', 'BB'],
        ['Bremen', 'HB'],
        ['Hamburg', 'HH'],
        ['Hessen', 'HE'],
        ['Mecklenburg-Vorpommern', 'MV'],
        ['Niedersachsen', 'NI'],
        ['Nordrhein-Westfalen', 'NW'],
        ['Rheinland-Pfalz', 'RP'],
        ['Saarland', 'SL'],
        ['Sachsen', 'SN'],
        ['Sachsen-Anhalt', 'ST'],
        ['Schleswig-Holstein', 'SH'],
        ['Thüringen', 'TH'],
    ] ))

Bundesland = Enum(
        value = "Bundesland",
        names=itertools.chain.from_iterable(
            itertools.product(v, [k]) for k, v in _BUNDESLAND.items()
        )
)

doc_str = ""

def print_doc( s ):
    global doc_str
    lines = s.split('\n')
    if SKIP and len( lines ) > 3:
        doc_str = doc_str + lines[0] + '\n...\n' + lines[-1]
    else:
        doc_str = doc_str + '\n'.join(lines)

def return_doc():
    global doc_str
    doc_str_copy = doc_str
    doc_str = ""
    return doc_str_copy

def set_skip( skip ):
    global SKIP
    SKIP=skip
