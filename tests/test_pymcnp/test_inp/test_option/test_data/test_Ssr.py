import pymcnp
from ..... import classes


class Test_Ssr(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Ssr
    EXAMPLES_VALID = [
        'axs 3.1 3.1 3.1',
        'bcw 3.1 3.0 3.1',
        'cel 1 1 1 1',
        'col 1',
        'ext d1',
        'new 1 1 1 1',
        'old 1 1 1 1',
        'poa 3.1',
        'psc 1',
        'pty @ _ #',
        'tr 1',
        'tr d1',
        'wgt 1',
    ]
    EXAMPLES_INVALID = [
        'cel 0 -1 1',
        'col 2 1 1',
        'old 0 1 1',
        'bcw 3.1 200 3.1',
        'hello',
    ]
