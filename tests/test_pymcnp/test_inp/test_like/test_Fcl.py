import pymcnp
from .... import consts
from .... import classes


class Test_Fcl:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Fcl
        EXAMPLES_VALID = [{'designator': consts.ast.type.DESIGNATOR, 'control': pymcnp.types.Real(0.8)}]
        EXAMPLES_INVALID = [{'designator': None, 'control': pymcnp.types.Real(0.8)}, {'designator': consts.ast.type.DESIGNATOR, 'control': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Fcl
        EXAMPLES_VALID = [consts.string.inp.like.FCL]
        EXAMPLES_INVALID = ['hello']


class Test_FclBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.like.FclBuilder
        EXAMPLES_VALID = [
            {'designator': consts.string.type.DESIGNATOR, 'control': '0.8'},
            {'designator': consts.string.type.DESIGNATOR, 'control': 0.8},
            {'designator': consts.ast.type.DESIGNATOR, 'control': pymcnp.types.Real(0.8)},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'control': '0.8'}, {'designator': consts.string.type.DESIGNATOR, 'control': None}, {'designator': consts.string.type.DESIGNATOR, 'control': '3.1'}]
