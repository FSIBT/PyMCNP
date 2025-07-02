import pymcnp
from ..... import consts
from ..... import classes


class Test_Geom:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.fmesh.Geom
        EXAMPLES_VALID = [{'geometry': pymcnp.types.String('xyz')}]
        EXAMPLES_INVALID = [{'geometry': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.fmesh.Geom
        EXAMPLES_VALID = [consts.string.inp.data.fmesh.GEOM]
        EXAMPLES_INVALID = ['hello']


class Test_GeomBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.fmesh.GeomBuilder
        EXAMPLES_VALID = [{'geometry': 'xyz'}, {'geometry': pymcnp.types.String('xyz')}]
        EXAMPLES_INVALID = [{'geometry': None}, {'geometry': 'hello'}]
