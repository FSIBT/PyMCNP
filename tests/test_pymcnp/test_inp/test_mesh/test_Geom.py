import pymcnp
from .... import consts
from .... import classes


class Test_Geom:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mesh.Geom
        EXAMPLES_VALID = [{'geometry': 'xyz'}, {'geometry': pymcnp.types.String('xyz')}]
        EXAMPLES_INVALID = [{'geometry': None}, {'geometry': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mesh.Geom
        EXAMPLES_VALID = [consts.string.inp.mesh.GEOM]
        EXAMPLES_INVALID = ['hello']
