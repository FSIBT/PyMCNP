import pymcnp
from ..... import classes


class Test_Ft(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Ft
    EXAMPLES_VALID = [
        'FRV 3.1 3.1 3.1',
        'GEB 3.1 3.1 3.1',
        'TMC 3.1 3.1',
        'INC',
        'ICD',
        'SCX 1',
        'SCD',
        'ELC 1',
        'CAP',
        'TAG 1',
        'LET',
        'ROC 3.1',
        'PDS 1',
        'FFT 0101',
        'COM 1 1',
        'MGC 3.1',
        'MGC',
        'FNS 1',
        'FNS',
        'LCS 3.1',
        'LCS',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
