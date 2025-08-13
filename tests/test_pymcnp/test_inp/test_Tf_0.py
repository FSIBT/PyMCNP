import pymcnp
from ... import consts
from ... import classes


class Test_Tf_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Tf_0
        EXAMPLES_VALID = [
            {
                'suffix': consts.string.types.INTEGER,
                'if1': consts.string.types.INTEGER,
                'id1': consts.string.types.INTEGER,
                'iu1': consts.string.types.INTEGER,
                'is1': consts.string.types.INTEGER,
                'im1': consts.string.types.INTEGER,
                'ic1': consts.string.types.INTEGER,
                'ie1': consts.string.types.INTEGER,
                'it1': consts.string.types.INTEGER,
            },
            {'suffix': 1, 'if1': 1, 'id1': 1, 'iu1': 1, 'is1': 1, 'im1': 1, 'ic1': 1, 'ie1': 1, 'it1': 1},
            {
                'suffix': consts.ast.types.INTEGER,
                'if1': consts.ast.types.INTEGER,
                'id1': consts.ast.types.INTEGER,
                'iu1': consts.ast.types.INTEGER,
                'is1': consts.ast.types.INTEGER,
                'im1': consts.ast.types.INTEGER,
                'ic1': consts.ast.types.INTEGER,
                'ie1': consts.ast.types.INTEGER,
                'it1': consts.ast.types.INTEGER,
            },
            {
                'suffix': consts.string.types.INTEGER,
                'if1': None,
                'id1': consts.string.types.INTEGER,
                'iu1': consts.string.types.INTEGER,
                'is1': consts.string.types.INTEGER,
                'im1': consts.string.types.INTEGER,
                'ic1': consts.string.types.INTEGER,
                'ie1': consts.string.types.INTEGER,
                'it1': consts.string.types.INTEGER,
            },
            {
                'suffix': consts.string.types.INTEGER,
                'if1': consts.string.types.INTEGER,
                'id1': None,
                'iu1': consts.string.types.INTEGER,
                'is1': consts.string.types.INTEGER,
                'im1': consts.string.types.INTEGER,
                'ic1': consts.string.types.INTEGER,
                'ie1': consts.string.types.INTEGER,
                'it1': consts.string.types.INTEGER,
            },
            {
                'suffix': consts.string.types.INTEGER,
                'if1': consts.string.types.INTEGER,
                'id1': consts.string.types.INTEGER,
                'iu1': None,
                'is1': consts.string.types.INTEGER,
                'im1': consts.string.types.INTEGER,
                'ic1': consts.string.types.INTEGER,
                'ie1': consts.string.types.INTEGER,
                'it1': consts.string.types.INTEGER,
            },
            {
                'suffix': consts.string.types.INTEGER,
                'if1': consts.string.types.INTEGER,
                'id1': consts.string.types.INTEGER,
                'iu1': consts.string.types.INTEGER,
                'is1': None,
                'im1': consts.string.types.INTEGER,
                'ic1': consts.string.types.INTEGER,
                'ie1': consts.string.types.INTEGER,
                'it1': consts.string.types.INTEGER,
            },
            {
                'suffix': consts.string.types.INTEGER,
                'if1': consts.string.types.INTEGER,
                'id1': consts.string.types.INTEGER,
                'iu1': consts.string.types.INTEGER,
                'is1': consts.string.types.INTEGER,
                'im1': None,
                'ic1': consts.string.types.INTEGER,
                'ie1': consts.string.types.INTEGER,
                'it1': consts.string.types.INTEGER,
            },
            {
                'suffix': consts.string.types.INTEGER,
                'if1': consts.string.types.INTEGER,
                'id1': consts.string.types.INTEGER,
                'iu1': consts.string.types.INTEGER,
                'is1': consts.string.types.INTEGER,
                'im1': consts.string.types.INTEGER,
                'ic1': None,
                'ie1': consts.string.types.INTEGER,
                'it1': consts.string.types.INTEGER,
            },
            {
                'suffix': consts.string.types.INTEGER,
                'if1': consts.string.types.INTEGER,
                'id1': consts.string.types.INTEGER,
                'iu1': consts.string.types.INTEGER,
                'is1': consts.string.types.INTEGER,
                'im1': consts.string.types.INTEGER,
                'ic1': consts.string.types.INTEGER,
                'ie1': None,
                'it1': consts.string.types.INTEGER,
            },
            {
                'suffix': consts.string.types.INTEGER,
                'if1': consts.string.types.INTEGER,
                'id1': consts.string.types.INTEGER,
                'iu1': consts.string.types.INTEGER,
                'is1': consts.string.types.INTEGER,
                'im1': consts.string.types.INTEGER,
                'ic1': consts.string.types.INTEGER,
                'ie1': consts.string.types.INTEGER,
                'it1': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'suffix': None,
                'if1': consts.string.types.INTEGER,
                'id1': consts.string.types.INTEGER,
                'iu1': consts.string.types.INTEGER,
                'is1': consts.string.types.INTEGER,
                'im1': consts.string.types.INTEGER,
                'ic1': consts.string.types.INTEGER,
                'ie1': consts.string.types.INTEGER,
                'it1': consts.string.types.INTEGER,
            }
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Tf_0
        EXAMPLES_VALID = [consts.string.inp.TF_0]
        EXAMPLES_INVALID = ['hello']
