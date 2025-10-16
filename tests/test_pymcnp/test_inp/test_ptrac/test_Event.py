import pymcnp
from .... import consts
from .... import classes


class Test_Event:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ptrac.Event
        EXAMPLES_VALID = [{'settings': [consts.string.types.STRING]}, {'settings': [consts.ast.types.STRING]}]
        EXAMPLES_INVALID = [{'settings': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ptrac.Event
        EXAMPLES_VALID = [consts.string.inp.ptrac.EVENT]
        EXAMPLES_INVALID = ['hello']
