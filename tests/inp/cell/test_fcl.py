import pymcnp
from ... import _utils


class Test_Fcl:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fcl
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.FclBuilder
        EXAMPLES_VALID = [
            {'designator': _utils.string.type.DESIGNATOR, 'control': '0.8'},
            {'designator': _utils.string.type.DESIGNATOR, 'control': 0.8},
            {'designator': _utils.ast.type.DESIGNATOR, 'control': pymcnp.utils.types.Real(0.8)},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'control': '0.8'}, {'designator': _utils.string.type.DESIGNATOR, 'control': None}, {'designator': _utils.string.type.DESIGNATOR, 'control': '3.1'}]
