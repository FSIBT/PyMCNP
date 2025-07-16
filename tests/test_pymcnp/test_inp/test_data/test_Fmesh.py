import pymcnp
from .... import consts
from .... import classes


class Test_Fmesh:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Fmesh
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'options': [consts.string.inp.data.fmesh.AXS]},
            {'suffix': 1, 'designator': consts.string.types.DESIGNATOR, 'options': [consts.ast.inp.data.fmesh.AXS]},
            {'suffix': consts.ast.types.INTEGER, 'designator': consts.ast.types.DESIGNATOR, 'options': [consts.ast.inp.data.fmesh.AXS]},
            {'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.string.types.DESIGNATOR, 'options': [consts.string.inp.data.fmesh.AXS]},
            {'suffix': consts.string.types.INTEGER, 'designator': None, 'options': [consts.string.inp.data.fmesh.AXS]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Fmesh
        EXAMPLES_VALID = [consts.string.inp.data.FMESH]
        EXAMPLES_INVALID = ['hello']
