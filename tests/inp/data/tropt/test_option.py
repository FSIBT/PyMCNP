import pymcnp
from .... import _utils


class Test_Mcscat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.tropt.Mcscat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.tropt.McscatBuilder
        EXAMPLES_VALID = [
            {'setting': 'off'},
            {'setting': pymcnp.utils.types.String('off')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Eloss:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.tropt.Eloss
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.tropt.ElossBuilder
        EXAMPLES_VALID = [
            {'setting': 'off'},
            {'setting': pymcnp.utils.types.String('off')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Nreact:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.tropt.Nreact
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.tropt.NreactBuilder
        EXAMPLES_VALID = [
            {'setting': 'off'},
            {'setting': pymcnp.utils.types.String('off')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Nescat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.tropt.Nescat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.tropt.NescatBuilder
        EXAMPLES_VALID = [
            {'setting': 'off'},
            {'setting': pymcnp.utils.types.String('off')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Genxs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.tropt.Genxs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.tropt.GenxsBuilder
        EXAMPLES_VALID = [
            {'filename': 'a'},
            {'filename': None},
            {'filename': pymcnp.utils.types.String('a')},
        ]
        EXAMPLES_INVALID = []
