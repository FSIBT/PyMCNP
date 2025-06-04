import pymcnp
from .... import _utils


class Test_Cell:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kpert.Cell
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kpert.CellBuilder
        EXAMPLES_VALID = [{'numbers': ['1']}, {'numbers': [1]}, {'numbers': [_utils.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]


class Test_Mat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kpert.Mat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kpert.MatBuilder
        EXAMPLES_VALID = [{'numbers': ['1']}, {'numbers': [1]}, {'numbers': [_utils.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]


class Test_Rho:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kpert.Rho
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kpert.RhoBuilder
        EXAMPLES_VALID = [{'densities': ['001001']}, {'densities': [_utils.ZAID]}]
        EXAMPLES_INVALID = [{'densities': None}]


class Test_Iso:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kpert.Iso
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kpert.IsoBuilder
        EXAMPLES_VALID = [{'zaids': ['000203']}, {'zaids': [_utils.ZAID]}]
        EXAMPLES_INVALID = [{'zaids': None}]


class Test_Rxn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kpert.Rxn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kpert.RxnBuilder
        EXAMPLES_VALID = [{'numbers': ['1']}, {'numbers': [1]}, {'numbers': [_utils.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]


class Test_Erg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kpert.Erg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kpert.ErgBuilder
        EXAMPLES_VALID = [{'energies': ['1.0']}, {'energies': [1.0]}, {'energies': [_utils.REAL]}]
        EXAMPLES_INVALID = [{'energies': None}]


class Test_Linear:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kpert.Linear
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kpert.LinearBuilder
        EXAMPLES_VALID = [
            {'setting': 'no'},
            {'setting': pymcnp.utils.types.String('no')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]
