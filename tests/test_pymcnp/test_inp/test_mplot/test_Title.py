import pymcnp
from .... import consts
from .... import classes


class Test_Title:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Title
        EXAMPLES_VALID = [
            {'n': consts.string.types.INTEGER, 'aa': consts.string.types.STRING},
            {'n': 1, 'aa': consts.string.types.STRING},
            {'n': consts.ast.types.INTEGER, 'aa': consts.ast.types.STRING},
        ]
        EXAMPLES_INVALID = [{'n': None, 'aa': consts.string.types.STRING}, {'n': consts.string.types.INTEGER, 'aa': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Title
        EXAMPLES_VALID = [consts.string.inp.mplot.TITLE]
        EXAMPLES_INVALID = ['hello']
