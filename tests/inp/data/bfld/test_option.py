import pymcnp
from .... import _utils


class Test_Field:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Field
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.bfld.FieldBuilder
        EXAMPLES_VALID = [
            {'strength_gradient': '1.0'},
            {'strength_gradient': 1.0},
            {'strength_gradient': _utils.REAL},
        ]
        EXAMPLES_INVALID = [{'strength_gradient': None}]


class Test_Vec:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Vec
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.bfld.VecBuilder
        EXAMPLES_VALID = [{'vector': ['1.0']}, {'vector': [1.0]}, {'vector': [_utils.REAL]}]
        EXAMPLES_INVALID = [{'vector': None}]


class Test_Maxdeflc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Maxdeflc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.bfld.MaxdeflcBuilder
        EXAMPLES_VALID = [{'angle': '1.0'}, {'angle': 1.0}, {'angle': _utils.REAL}]
        EXAMPLES_INVALID = [{'angle': None}]


class Test_Maxstep:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Maxstep
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.bfld.MaxstepBuilder
        EXAMPLES_VALID = [{'size': '1.0'}, {'size': 1.0}, {'size': _utils.REAL}]
        EXAMPLES_INVALID = [{'size': None}]


class Test_Axs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Axs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.bfld.AxsBuilder
        EXAMPLES_VALID = [{'vector': ['1.0']}, {'vector': [1.0]}, {'vector': [_utils.REAL]}]
        EXAMPLES_INVALID = [{'vector': None}]


class Test_Ffedges:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Ffedges
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.bfld.FfedgesBuilder
        EXAMPLES_VALID = [{'numbers': ['1.0']}, {'numbers': [1.0]}, {'numbers': [_utils.REAL]}]
        EXAMPLES_INVALID = [{'numbers': None}]


class Test_Refpnt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Refpnt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.bfld.RefpntBuilder
        EXAMPLES_VALID = [{'point': ['1.0']}, {'point': [1.0]}, {'point': [_utils.REAL]}]
        EXAMPLES_INVALID = [{'point': None}]
