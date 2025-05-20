import pymcnp
from .... import _utils


class Test_Fission:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Fission
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.FissionBuilder
        EXAMPLES_VALID = [{'kind': 'none'}, {'kind': pymcnp.utils.types.String('none')}]
        EXAMPLES_INVALID = [{'kind': None}]


class Test_Nonfiss:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Nonfiss
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.NonfissBuilder
        EXAMPLES_VALID = [{'kind': 'none'}, {'kind': pymcnp.utils.types.String('none')}]
        EXAMPLES_INVALID = [{'kind': None}]


class Test_Dn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Dn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.DnBuilder
        EXAMPLES_VALID = [
            {'source': 'model'},
            {'source': pymcnp.utils.types.String('model')},
        ]
        EXAMPLES_INVALID = [{'source': None}]


class Test_Dg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Dg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.DgBuilder
        EXAMPLES_VALID = [
            {'source': 'line'},
            {'source': pymcnp.utils.types.String('line')},
        ]
        EXAMPLES_INVALID = [{'source': None}]


class Test_Thresh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Thresh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.ThreshBuilder
        EXAMPLES_VALID = [{'fraction': '1.0'}, {'fraction': 1.0}, {'fraction': _utils.REAL}]
        EXAMPLES_INVALID = [{'fraction': None}]


class Test_Dnbais:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Dnbais
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.DnbaisBuilder
        EXAMPLES_VALID = [{'count': '1'}, {'count': 1}, {'count': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'count': None}]


class Test_Nap:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Nap
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.NapBuilder
        EXAMPLES_VALID = [{'count': '1'}, {'count': 1}, {'count': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'count': None}]


class Test_Dneb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Dneb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.DnebBuilder
        EXAMPLES_VALID = [
            {'biases': ['1 2']},
            {'biases': [_utils.BIAS]},
        ]
        EXAMPLES_INVALID = [{'biases': None}]


class Test_Dgeb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Dgeb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.DgebBuilder
        EXAMPLES_VALID = [
            {'biases': ['1 2']},
            {'biases': [_utils.BIAS]},
        ]
        EXAMPLES_INVALID = [{'biases': None}]


class Test_Pecut:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Pecut
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.PecutBuilder
        EXAMPLES_VALID = [{'cutoff': '1.0'}, {'cutoff': 1.0}, {'cutoff': _utils.REAL}]
        EXAMPLES_INVALID = [{'cutoff': None}]


class Test_Hlcut:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Hlcut
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.HlcutBuilder
        EXAMPLES_VALID = [{'cutoff': '1.0'}, {'cutoff': 1.0}, {'cutoff': _utils.REAL}]
        EXAMPLES_INVALID = [{'cutoff': None}]


class Test_Sample:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Sample
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.SampleBuilder
        EXAMPLES_VALID = [
            {'setting': 'correlate'},
            {'setting': pymcnp.utils.types.String('correlate')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]
