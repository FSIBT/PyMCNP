import pymcnp
from ..... import classes


class Test_Dbrc(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Dbrc
    EXAMPLES_VALID = [
        'emax=3.1',
        'endf=71',
        'endf 80',
        'isos=001001 001001',
    ]
    EXAMPLES_INVALID = [
        'endf 1hello',
    ]
