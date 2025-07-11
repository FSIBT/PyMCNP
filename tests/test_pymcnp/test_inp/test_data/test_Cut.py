import pymcnp
from .... import consts
from .... import classes


class Test_Cut:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Cut
        EXAMPLES_VALID = [
            {
                'designator': consts.string.type.DESIGNATOR,
                'time_cutoff': consts.string.type.REAL,
                'energy_cutoff': consts.string.type.REAL,
                'weight_cutoff1': consts.string.type.REAL,
                'weight_cutoff2': consts.string.type.REAL,
                'source_weight': consts.string.type.REAL,
            },
            {'designator': consts.string.type.DESIGNATOR, 'time_cutoff': 3.1, 'energy_cutoff': 3.1, 'weight_cutoff1': 3.1, 'weight_cutoff2': 3.1, 'source_weight': 3.1},
            {
                'designator': consts.ast.type.DESIGNATOR,
                'time_cutoff': consts.ast.type.REAL,
                'energy_cutoff': consts.ast.type.REAL,
                'weight_cutoff1': consts.ast.type.REAL,
                'weight_cutoff2': consts.ast.type.REAL,
                'source_weight': consts.ast.type.REAL,
            },
            {
                'designator': consts.string.type.DESIGNATOR,
                'time_cutoff': None,
                'energy_cutoff': consts.string.type.REAL,
                'weight_cutoff1': consts.string.type.REAL,
                'weight_cutoff2': consts.string.type.REAL,
                'source_weight': consts.string.type.REAL,
            },
            {
                'designator': consts.string.type.DESIGNATOR,
                'time_cutoff': consts.string.type.REAL,
                'energy_cutoff': None,
                'weight_cutoff1': consts.string.type.REAL,
                'weight_cutoff2': consts.string.type.REAL,
                'source_weight': consts.string.type.REAL,
            },
            {
                'designator': consts.string.type.DESIGNATOR,
                'time_cutoff': consts.string.type.REAL,
                'energy_cutoff': consts.string.type.REAL,
                'weight_cutoff1': None,
                'weight_cutoff2': consts.string.type.REAL,
                'source_weight': consts.string.type.REAL,
            },
            {
                'designator': consts.string.type.DESIGNATOR,
                'time_cutoff': consts.string.type.REAL,
                'energy_cutoff': consts.string.type.REAL,
                'weight_cutoff1': consts.string.type.REAL,
                'weight_cutoff2': None,
                'source_weight': consts.string.type.REAL,
            },
            {
                'designator': consts.string.type.DESIGNATOR,
                'time_cutoff': consts.string.type.REAL,
                'energy_cutoff': consts.string.type.REAL,
                'weight_cutoff1': consts.string.type.REAL,
                'weight_cutoff2': consts.string.type.REAL,
                'source_weight': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'designator': None,
                'time_cutoff': consts.string.type.REAL,
                'energy_cutoff': consts.string.type.REAL,
                'weight_cutoff1': consts.string.type.REAL,
                'weight_cutoff2': consts.string.type.REAL,
                'source_weight': consts.string.type.REAL,
            }
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Cut
        EXAMPLES_VALID = [consts.string.inp.data.CUT]
        EXAMPLES_INVALID = ['hello']
