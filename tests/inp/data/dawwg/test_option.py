import pymcnp
from .... import _utils


class Test_Points:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.Points
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.PointsBuilder
        EXAMPLES_VALID = [{'name': 'a'}, {'name': 'a'}, {'name': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'name': None}]


class Test_Xsec:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.Xsec
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.XsecBuilder
        EXAMPLES_VALID = [{'count': '1'}, {'count': 1}, {'count': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'count': None}]


class Test_Block:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.Block
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.BlockBuilder
        EXAMPLES_VALID = [
            {'setting': '1', 'options': None},
            {'setting': '1', 'options': None},
            {'setting': 1, 'options': None},
            {'setting': _utils.INTEGER, 'options': None},
        ]
        EXAMPLES_INVALID = [{'setting': None, 'options': None}]
