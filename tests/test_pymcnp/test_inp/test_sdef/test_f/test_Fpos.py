import pymcnp
from ..... import consts
from ..... import classes


class Test_Fpos:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.f.Fpos
        EXAMPLES_VALID = [{'distribution': consts.string.types.DISTRIBUTION}, {'distribution': consts.ast.types.DISTRIBUTION}]
        EXAMPLES_INVALID = [{'distribution': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.f.Fpos
        EXAMPLES_VALID = [consts.string.inp.sdef.f.FPOS]
        EXAMPLES_INVALID = ['hello']
