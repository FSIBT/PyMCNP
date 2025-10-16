import pymcnp
from .... import consts
from .... import classes


class Test_Type:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.fmesh.Type
        EXAMPLES_VALID = [{'setting': 'flux'}, {'setting': pymcnp.types.String('flux')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.fmesh.Type
        EXAMPLES_VALID = [consts.string.inp.fmesh.TYPE]
        EXAMPLES_INVALID = ['hello']
