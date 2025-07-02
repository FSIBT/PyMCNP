import pymcnp
from .... import consts
from .... import classes


class Test_Fmesh:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Fmesh
        EXAMPLES_VALID = [
            {'suffix': consts.ast.type.INTEGER, 'designator': consts.ast.type.DESIGNATOR, 'options': [consts.ast.inp.data.fmesh.AXS]},
            {'suffix': consts.ast.type.INTEGER, 'designator': consts.ast.type.DESIGNATOR, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.ast.type.DESIGNATOR, 'options': [consts.ast.inp.data.fmesh.AXS]},
            {'suffix': consts.ast.type.INTEGER, 'designator': None, 'options': [consts.ast.inp.data.fmesh.AXS]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Fmesh
        EXAMPLES_VALID = [consts.string.inp.data.FMESH]
        EXAMPLES_INVALID = ['hello']


class Test_FmeshBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.FmeshBuilder
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'options': [consts.string.inp.data.fmesh.AXS]},
            {'suffix': 1, 'designator': consts.string.type.DESIGNATOR, 'options': [consts.builder.inp.data.fmesh.AXS]},
            {'suffix': consts.ast.type.INTEGER, 'designator': consts.ast.type.DESIGNATOR, 'options': [consts.ast.inp.data.fmesh.AXS]},
            {'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.string.type.DESIGNATOR, 'options': [consts.string.inp.data.fmesh.AXS]},
            {'suffix': consts.string.type.INTEGER, 'designator': None, 'options': [consts.string.inp.data.fmesh.AXS]},
        ]
