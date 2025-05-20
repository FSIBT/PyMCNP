import pymcnp
from .... import _utils


class Test_Embed:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.Embed
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embee.EmbedBuilder
        EXAMPLES_VALID = [{'number': '1'}, {'number': 1}, {'number': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]


class Test_Energy:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.Energy
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embee.EnergyBuilder
        EXAMPLES_VALID = [{'factor': '1.0'}, {'factor': 1.0}, {'factor': _utils.REAL}]
        EXAMPLES_INVALID = [{'factor': None}]


class Test_Time:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.Time
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embee.TimeBuilder
        EXAMPLES_VALID = [{'factor': '1.0'}, {'factor': 1.0}, {'factor': _utils.REAL}]
        EXAMPLES_INVALID = [{'factor': None}]


class Test_Atom:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.Atom
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embee.AtomBuilder
        EXAMPLES_VALID = [{'setting': 'yes'}, {'setting': pymcnp.utils.types.String('yes')}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Factor:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.Factor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embee.FactorBuilder
        EXAMPLES_VALID = [{'constant': '1.0'}, {'constant': 1.0}, {'constant': _utils.REAL}]
        EXAMPLES_INVALID = [{'constant': None}]


class Test_List:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.List
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embee.ListBuilder
        EXAMPLES_VALID = [{'reactions': '1.0'}, {'reactions': 1.0}, {'reactions': _utils.REAL}]
        EXAMPLES_INVALID = [{'reactions': None}]


class Test_Mat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.Mat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embee.MatBuilder
        EXAMPLES_VALID = [{'number': '1'}, {'number': 1}, {'number': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]


class Test_Mtype:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.Mtype
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embee.MtypeBuilder
        EXAMPLES_VALID = [{'kind': 'flux'}, {'kind': pymcnp.utils.types.String('flux')}]
        EXAMPLES_INVALID = [{'kind': None}]
