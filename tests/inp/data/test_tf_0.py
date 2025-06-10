import pymcnp
from ... import _utils


class Test_Tf_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Tf_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.TfBuilder_0
        EXAMPLES_VALID = [
            {
                'suffix': _utils.string.type.INTEGER,
                'if1': _utils.string.type.INTEGER,
                'id1': _utils.string.type.INTEGER,
                'iu1': _utils.string.type.INTEGER,
                'is1': _utils.string.type.INTEGER,
                'im1': _utils.string.type.INTEGER,
                'ic1': _utils.string.type.INTEGER,
                'ie1': _utils.string.type.INTEGER,
                'it1': _utils.string.type.INTEGER,
            },
            {'suffix': 1, 'if1': 1, 'id1': 1, 'iu1': 1, 'is1': 1, 'im1': 1, 'ic1': 1, 'ie1': 1, 'it1': 1},
            {
                'suffix': _utils.ast.type.INTEGER,
                'if1': _utils.ast.type.INTEGER,
                'id1': _utils.ast.type.INTEGER,
                'iu1': _utils.ast.type.INTEGER,
                'is1': _utils.ast.type.INTEGER,
                'im1': _utils.ast.type.INTEGER,
                'ic1': _utils.ast.type.INTEGER,
                'ie1': _utils.ast.type.INTEGER,
                'it1': _utils.ast.type.INTEGER,
            },
            {
                'suffix': _utils.string.type.INTEGER,
                'if1': None,
                'id1': _utils.string.type.INTEGER,
                'iu1': _utils.string.type.INTEGER,
                'is1': _utils.string.type.INTEGER,
                'im1': _utils.string.type.INTEGER,
                'ic1': _utils.string.type.INTEGER,
                'ie1': _utils.string.type.INTEGER,
                'it1': _utils.string.type.INTEGER,
            },
            {
                'suffix': _utils.string.type.INTEGER,
                'if1': _utils.string.type.INTEGER,
                'id1': None,
                'iu1': _utils.string.type.INTEGER,
                'is1': _utils.string.type.INTEGER,
                'im1': _utils.string.type.INTEGER,
                'ic1': _utils.string.type.INTEGER,
                'ie1': _utils.string.type.INTEGER,
                'it1': _utils.string.type.INTEGER,
            },
            {
                'suffix': _utils.string.type.INTEGER,
                'if1': _utils.string.type.INTEGER,
                'id1': _utils.string.type.INTEGER,
                'iu1': None,
                'is1': _utils.string.type.INTEGER,
                'im1': _utils.string.type.INTEGER,
                'ic1': _utils.string.type.INTEGER,
                'ie1': _utils.string.type.INTEGER,
                'it1': _utils.string.type.INTEGER,
            },
            {
                'suffix': _utils.string.type.INTEGER,
                'if1': _utils.string.type.INTEGER,
                'id1': _utils.string.type.INTEGER,
                'iu1': _utils.string.type.INTEGER,
                'is1': None,
                'im1': _utils.string.type.INTEGER,
                'ic1': _utils.string.type.INTEGER,
                'ie1': _utils.string.type.INTEGER,
                'it1': _utils.string.type.INTEGER,
            },
            {
                'suffix': _utils.string.type.INTEGER,
                'if1': _utils.string.type.INTEGER,
                'id1': _utils.string.type.INTEGER,
                'iu1': _utils.string.type.INTEGER,
                'is1': _utils.string.type.INTEGER,
                'im1': None,
                'ic1': _utils.string.type.INTEGER,
                'ie1': _utils.string.type.INTEGER,
                'it1': _utils.string.type.INTEGER,
            },
            {
                'suffix': _utils.string.type.INTEGER,
                'if1': _utils.string.type.INTEGER,
                'id1': _utils.string.type.INTEGER,
                'iu1': _utils.string.type.INTEGER,
                'is1': _utils.string.type.INTEGER,
                'im1': _utils.string.type.INTEGER,
                'ic1': None,
                'ie1': _utils.string.type.INTEGER,
                'it1': _utils.string.type.INTEGER,
            },
            {
                'suffix': _utils.string.type.INTEGER,
                'if1': _utils.string.type.INTEGER,
                'id1': _utils.string.type.INTEGER,
                'iu1': _utils.string.type.INTEGER,
                'is1': _utils.string.type.INTEGER,
                'im1': _utils.string.type.INTEGER,
                'ic1': _utils.string.type.INTEGER,
                'ie1': None,
                'it1': _utils.string.type.INTEGER,
            },
            {
                'suffix': _utils.string.type.INTEGER,
                'if1': _utils.string.type.INTEGER,
                'id1': _utils.string.type.INTEGER,
                'iu1': _utils.string.type.INTEGER,
                'is1': _utils.string.type.INTEGER,
                'im1': _utils.string.type.INTEGER,
                'ic1': _utils.string.type.INTEGER,
                'ie1': _utils.string.type.INTEGER,
                'it1': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'suffix': None,
                'if1': _utils.string.type.INTEGER,
                'id1': _utils.string.type.INTEGER,
                'iu1': _utils.string.type.INTEGER,
                'is1': _utils.string.type.INTEGER,
                'im1': _utils.string.type.INTEGER,
                'ic1': _utils.string.type.INTEGER,
                'ie1': _utils.string.type.INTEGER,
                'it1': _utils.string.type.INTEGER,
            }
        ]
