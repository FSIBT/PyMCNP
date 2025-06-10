import pymcnp
from ... import _utils


class Test_Cut:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Cut
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.CutBuilder
        EXAMPLES_VALID = [
            {
                'designator': _utils.string.type.DESIGNATOR,
                'time_cutoff': _utils.string.type.REAL,
                'energy_cutoff': _utils.string.type.REAL,
                'weight_cutoff1': _utils.string.type.REAL,
                'weight_cutoff2': _utils.string.type.REAL,
                'source_weight': _utils.string.type.REAL,
            },
            {'designator': _utils.string.type.DESIGNATOR, 'time_cutoff': 3.1, 'energy_cutoff': 3.1, 'weight_cutoff1': 3.1, 'weight_cutoff2': 3.1, 'source_weight': 3.1},
            {
                'designator': _utils.ast.type.DESIGNATOR,
                'time_cutoff': _utils.ast.type.REAL,
                'energy_cutoff': _utils.ast.type.REAL,
                'weight_cutoff1': _utils.ast.type.REAL,
                'weight_cutoff2': _utils.ast.type.REAL,
                'source_weight': _utils.ast.type.REAL,
            },
            {
                'designator': _utils.string.type.DESIGNATOR,
                'time_cutoff': None,
                'energy_cutoff': _utils.string.type.REAL,
                'weight_cutoff1': _utils.string.type.REAL,
                'weight_cutoff2': _utils.string.type.REAL,
                'source_weight': _utils.string.type.REAL,
            },
            {
                'designator': _utils.string.type.DESIGNATOR,
                'time_cutoff': _utils.string.type.REAL,
                'energy_cutoff': None,
                'weight_cutoff1': _utils.string.type.REAL,
                'weight_cutoff2': _utils.string.type.REAL,
                'source_weight': _utils.string.type.REAL,
            },
            {
                'designator': _utils.string.type.DESIGNATOR,
                'time_cutoff': _utils.string.type.REAL,
                'energy_cutoff': _utils.string.type.REAL,
                'weight_cutoff1': None,
                'weight_cutoff2': _utils.string.type.REAL,
                'source_weight': _utils.string.type.REAL,
            },
            {
                'designator': _utils.string.type.DESIGNATOR,
                'time_cutoff': _utils.string.type.REAL,
                'energy_cutoff': _utils.string.type.REAL,
                'weight_cutoff1': _utils.string.type.REAL,
                'weight_cutoff2': None,
                'source_weight': _utils.string.type.REAL,
            },
            {
                'designator': _utils.string.type.DESIGNATOR,
                'time_cutoff': _utils.string.type.REAL,
                'energy_cutoff': _utils.string.type.REAL,
                'weight_cutoff1': _utils.string.type.REAL,
                'weight_cutoff2': _utils.string.type.REAL,
                'source_weight': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'designator': None,
                'time_cutoff': _utils.string.type.REAL,
                'energy_cutoff': _utils.string.type.REAL,
                'weight_cutoff1': _utils.string.type.REAL,
                'weight_cutoff2': _utils.string.type.REAL,
                'source_weight': _utils.string.type.REAL,
            }
        ]
