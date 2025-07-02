import pymcnp
from ..... import consts
from ..... import classes


class Test_Jints:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.fmesh.Jints
        EXAMPLES_VALID = [{'count': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'count': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.fmesh.Jints
        EXAMPLES_VALID = [consts.string.inp.data.fmesh.JINTS]
        EXAMPLES_INVALID = ['hello']


class Test_JintsBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.fmesh.JintsBuilder
        EXAMPLES_VALID = [{'count': [consts.string.type.INTEGER]}, {'count': [1]}, {'count': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'count': None}]
