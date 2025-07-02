import pymcnp
from ..... import consts
from ..... import classes


class Test_Subtitle:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Subtitle
        EXAMPLES_VALID = [{'x': consts.ast.type.INTEGER, 'y': consts.ast.type.INTEGER, 'aa': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [
            {'x': None, 'y': consts.ast.type.INTEGER, 'aa': consts.ast.type.STRING},
            {'x': consts.ast.type.INTEGER, 'y': None, 'aa': consts.ast.type.STRING},
            {'x': consts.ast.type.INTEGER, 'y': consts.ast.type.INTEGER, 'aa': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Subtitle
        EXAMPLES_VALID = [consts.string.inp.data.mplot.SUBTITLE]
        EXAMPLES_INVALID = ['hello']


class Test_SubtitleBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.SubtitleBuilder
        EXAMPLES_VALID = [
            {'x': consts.string.type.INTEGER, 'y': consts.string.type.INTEGER, 'aa': consts.string.type.STRING},
            {'x': 1, 'y': 1, 'aa': consts.string.type.STRING},
            {'x': consts.ast.type.INTEGER, 'y': consts.ast.type.INTEGER, 'aa': consts.ast.type.STRING},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': consts.string.type.INTEGER, 'aa': consts.string.type.STRING},
            {'x': consts.string.type.INTEGER, 'y': None, 'aa': consts.string.type.STRING},
            {'x': consts.string.type.INTEGER, 'y': consts.string.type.INTEGER, 'aa': None},
        ]
