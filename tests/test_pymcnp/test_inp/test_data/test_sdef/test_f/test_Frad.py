import pymcnp
from ...... import consts
from ...... import classes


class Test_Frad:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.f.Frad
        EXAMPLES_VALID = [{'distribution': consts.string.types.DISTRIBUTION}, {'distribution': consts.ast.types.DISTRIBUTION}]
        EXAMPLES_INVALID = [{'distribution': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.f.Frad
        EXAMPLES_VALID = [consts.string.inp.data.sdef.f.FRAD]
        EXAMPLES_INVALID = ['hello']
