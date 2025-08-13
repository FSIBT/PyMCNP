import pymcnp
from .... import consts
from .... import classes


class Test_Subtitle:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Subtitle
        EXAMPLES_VALID = [
            {'x': consts.string.types.INTEGER, 'y': consts.string.types.INTEGER, 'aa': consts.string.types.STRING},
            {'x': 1, 'y': 1, 'aa': consts.string.types.STRING},
            {'x': consts.ast.types.INTEGER, 'y': consts.ast.types.INTEGER, 'aa': consts.ast.types.STRING},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': consts.string.types.INTEGER, 'aa': consts.string.types.STRING},
            {'x': consts.string.types.INTEGER, 'y': None, 'aa': consts.string.types.STRING},
            {'x': consts.string.types.INTEGER, 'y': consts.string.types.INTEGER, 'aa': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Subtitle
        EXAMPLES_VALID = [consts.string.inp.mplot.SUBTITLE]
        EXAMPLES_INVALID = ['hello']
