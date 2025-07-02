import pymcnp
from ..... import consts
from ..... import classes


class Test_Title:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Title
        EXAMPLES_VALID = [{'n': consts.ast.type.INTEGER, 'aa': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'n': None, 'aa': consts.ast.type.STRING}, {'n': consts.ast.type.INTEGER, 'aa': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Title
        EXAMPLES_VALID = [consts.string.inp.data.mplot.TITLE]
        EXAMPLES_INVALID = ['hello']


class Test_TitleBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.TitleBuilder
        EXAMPLES_VALID = [{'n': consts.string.type.INTEGER, 'aa': consts.string.type.STRING}, {'n': 1, 'aa': consts.string.type.STRING}, {'n': consts.ast.type.INTEGER, 'aa': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'n': None, 'aa': consts.string.type.STRING}, {'n': consts.string.type.INTEGER, 'aa': None}]
