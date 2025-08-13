import pymcnp
from .... import consts
from .... import classes


class Test_Enorm:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.fmesh.Enorm
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.fmesh.Enorm
        EXAMPLES_VALID = [consts.string.inp.fmesh.ENORM]
        EXAMPLES_INVALID = ['hello']
