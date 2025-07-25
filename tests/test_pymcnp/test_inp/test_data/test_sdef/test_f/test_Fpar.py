import pymcnp
from ...... import consts
from ...... import classes


class Test_Fpar:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.f.Fpar
        EXAMPLES_VALID = [{'distribution': consts.string.types.DISTRIBUTION}, {'distribution': consts.ast.types.DISTRIBUTION}]
        EXAMPLES_INVALID = [{'distribution': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.f.Fpar
        EXAMPLES_VALID = [consts.string.inp.data.sdef.f.FPAR]
        EXAMPLES_INVALID = ['hello']
