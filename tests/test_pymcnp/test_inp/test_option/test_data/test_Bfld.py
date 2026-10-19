import pymcnp
from ..... import classes


class Test_Bfld(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Bfld
    EXAMPLES_VALID = [
        'field 3.1',
        'vec 3.1 3.1 3.1',
        'mxdeflc 3.1',
        'maxstep 3.1',
        'axs 3.1 3.1 3.1',
        'ffedges 1 1 1',
        'refpnt 3.1 3.1 3.1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]
