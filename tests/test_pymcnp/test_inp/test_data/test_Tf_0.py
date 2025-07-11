import pymcnp
from .... import consts
from .... import classes


class Test_Tf_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Tf_0
        EXAMPLES_VALID = [
            {
                'suffix': consts.string.type.INTEGER,
                'if1': consts.string.type.INTEGER,
                'id1': consts.string.type.INTEGER,
                'iu1': consts.string.type.INTEGER,
                'is1': consts.string.type.INTEGER,
                'im1': consts.string.type.INTEGER,
                'ic1': consts.string.type.INTEGER,
                'ie1': consts.string.type.INTEGER,
                'it1': consts.string.type.INTEGER,
            },
            {'suffix': 1, 'if1': 1, 'id1': 1, 'iu1': 1, 'is1': 1, 'im1': 1, 'ic1': 1, 'ie1': 1, 'it1': 1},
            {
                'suffix': consts.ast.type.INTEGER,
                'if1': consts.ast.type.INTEGER,
                'id1': consts.ast.type.INTEGER,
                'iu1': consts.ast.type.INTEGER,
                'is1': consts.ast.type.INTEGER,
                'im1': consts.ast.type.INTEGER,
                'ic1': consts.ast.type.INTEGER,
                'ie1': consts.ast.type.INTEGER,
                'it1': consts.ast.type.INTEGER,
            },
            {
                'suffix': consts.string.type.INTEGER,
                'if1': None,
                'id1': consts.string.type.INTEGER,
                'iu1': consts.string.type.INTEGER,
                'is1': consts.string.type.INTEGER,
                'im1': consts.string.type.INTEGER,
                'ic1': consts.string.type.INTEGER,
                'ie1': consts.string.type.INTEGER,
                'it1': consts.string.type.INTEGER,
            },
            {
                'suffix': consts.string.type.INTEGER,
                'if1': consts.string.type.INTEGER,
                'id1': None,
                'iu1': consts.string.type.INTEGER,
                'is1': consts.string.type.INTEGER,
                'im1': consts.string.type.INTEGER,
                'ic1': consts.string.type.INTEGER,
                'ie1': consts.string.type.INTEGER,
                'it1': consts.string.type.INTEGER,
            },
            {
                'suffix': consts.string.type.INTEGER,
                'if1': consts.string.type.INTEGER,
                'id1': consts.string.type.INTEGER,
                'iu1': None,
                'is1': consts.string.type.INTEGER,
                'im1': consts.string.type.INTEGER,
                'ic1': consts.string.type.INTEGER,
                'ie1': consts.string.type.INTEGER,
                'it1': consts.string.type.INTEGER,
            },
            {
                'suffix': consts.string.type.INTEGER,
                'if1': consts.string.type.INTEGER,
                'id1': consts.string.type.INTEGER,
                'iu1': consts.string.type.INTEGER,
                'is1': None,
                'im1': consts.string.type.INTEGER,
                'ic1': consts.string.type.INTEGER,
                'ie1': consts.string.type.INTEGER,
                'it1': consts.string.type.INTEGER,
            },
            {
                'suffix': consts.string.type.INTEGER,
                'if1': consts.string.type.INTEGER,
                'id1': consts.string.type.INTEGER,
                'iu1': consts.string.type.INTEGER,
                'is1': consts.string.type.INTEGER,
                'im1': None,
                'ic1': consts.string.type.INTEGER,
                'ie1': consts.string.type.INTEGER,
                'it1': consts.string.type.INTEGER,
            },
            {
                'suffix': consts.string.type.INTEGER,
                'if1': consts.string.type.INTEGER,
                'id1': consts.string.type.INTEGER,
                'iu1': consts.string.type.INTEGER,
                'is1': consts.string.type.INTEGER,
                'im1': consts.string.type.INTEGER,
                'ic1': None,
                'ie1': consts.string.type.INTEGER,
                'it1': consts.string.type.INTEGER,
            },
            {
                'suffix': consts.string.type.INTEGER,
                'if1': consts.string.type.INTEGER,
                'id1': consts.string.type.INTEGER,
                'iu1': consts.string.type.INTEGER,
                'is1': consts.string.type.INTEGER,
                'im1': consts.string.type.INTEGER,
                'ic1': consts.string.type.INTEGER,
                'ie1': None,
                'it1': consts.string.type.INTEGER,
            },
            {
                'suffix': consts.string.type.INTEGER,
                'if1': consts.string.type.INTEGER,
                'id1': consts.string.type.INTEGER,
                'iu1': consts.string.type.INTEGER,
                'is1': consts.string.type.INTEGER,
                'im1': consts.string.type.INTEGER,
                'ic1': consts.string.type.INTEGER,
                'ie1': consts.string.type.INTEGER,
                'it1': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'suffix': None,
                'if1': consts.string.type.INTEGER,
                'id1': consts.string.type.INTEGER,
                'iu1': consts.string.type.INTEGER,
                'is1': consts.string.type.INTEGER,
                'im1': consts.string.type.INTEGER,
                'ic1': consts.string.type.INTEGER,
                'ie1': consts.string.type.INTEGER,
                'it1': consts.string.type.INTEGER,
            }
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Tf_0
        EXAMPLES_VALID = [consts.string.inp.data.TF_0]
        EXAMPLES_INVALID = ['hello']
