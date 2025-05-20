import pymcnp
from .... import _utils


class Test_Gen:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.rand.Gen
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.rand.GenBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Seed:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.rand.Seed
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.rand.SeedBuilder
        EXAMPLES_VALID = [{'seed': '1'}, {'seed': 1}, {'seed': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'seed': None}]


class Test_Stride:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.rand.Stride
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.rand.StrideBuilder
        EXAMPLES_VALID = [{'stride': '1'}, {'stride': 1}, {'stride': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'stride': None}]


class Test_Hist:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.rand.Hist
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.rand.HistBuilder
        EXAMPLES_VALID = [{'hist': '1'}, {'hist': 1}, {'hist': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'hist': None}]
