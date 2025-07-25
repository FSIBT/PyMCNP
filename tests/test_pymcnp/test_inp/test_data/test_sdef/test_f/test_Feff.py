import pymcnp
from ...... import consts
from ...... import classes


class Test_Feff:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.f.Feff
        EXAMPLES_VALID = [{'distribution': consts.string.types.DISTRIBUTION}, {'distribution': consts.ast.types.DISTRIBUTION}]
        EXAMPLES_INVALID = [{'distribution': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.f.Feff
        EXAMPLES_VALID = [consts.string.inp.data.sdef.f.FEFF]
        EXAMPLES_INVALID = ['hello']
