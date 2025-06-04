import pymcnp
from .... import _utils


class Test_Iso:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Iso
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ksen.IsoBuilder
        EXAMPLES_VALID = [{'zaids': ['000203']}, {'zaids': [_utils.ZAID]}]
        EXAMPLES_INVALID = [{'zaids': None}]


class Test_Rxn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Rxn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ksen.RxnBuilder
        EXAMPLES_VALID = [{'numbers': ['1']}, {'numbers': [1]}, {'numbers': [_utils.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]


class Test_Mt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Mt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ksen.MtBuilder
        EXAMPLES_VALID = [{'numbers': ['1']}, {'numbers': [1]}, {'numbers': [_utils.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]


class Test_Erg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Erg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ksen.ErgBuilder
        EXAMPLES_VALID = [{'energies': ['1.0']}, {'energies': [1.0]}, {'energies': [_utils.REAL]}]
        EXAMPLES_INVALID = [{'energies': None}]


class Test_Ein:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Ein
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ksen.EinBuilder
        EXAMPLES_VALID = [{'energies': ['1.0']}, {'energies': [1.0]}, {'energies': [_utils.REAL]}]
        EXAMPLES_INVALID = [{'energies': None}]


class Test_Legendre:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Legendre
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ksen.LegendreBuilder
        EXAMPLES_VALID = [{'number': '1'}, {'number': 1}, {'number': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]


class Test_Cos:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Cos
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ksen.CosBuilder
        EXAMPLES_VALID = [{'cosines': ['1.0']}, {'cosines': [1.0]}, {'cosines': [_utils.REAL]}]
        EXAMPLES_INVALID = [{'cosines': None}]


class Test_Constrain:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Constrain
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ksen.ConstrainBuilder
        EXAMPLES_VALID = [
            {'setting': 'no'},
            {'setting': pymcnp.utils.types.String('no')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]
