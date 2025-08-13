import pymcnp
from ..... import consts
from ..... import classes


class Test_Fccc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.f.Fccc
        EXAMPLES_VALID = [{'distribution': consts.string.types.DISTRIBUTION}, {'distribution': consts.ast.types.DISTRIBUTION}]
        EXAMPLES_INVALID = [{'distribution': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.f.Fccc
        EXAMPLES_VALID = [consts.string.inp.sdef.f.FCCC]
        EXAMPLES_INVALID = ['hello']
