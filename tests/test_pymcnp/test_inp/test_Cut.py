import pymcnp
from ... import consts
from ... import classes


class Test_Cut:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Cut
        EXAMPLES_VALID = [
            {
                'designator': consts.string.types.DESIGNATOR,
                'time_cutoff': consts.string.types.REAL,
                'energy_cutoff': consts.string.types.REAL,
                'weight_cutoff1': consts.string.types.REAL,
                'weight_cutoff2': consts.string.types.REAL,
                'source_weight': consts.string.types.REAL,
            },
            {'designator': consts.string.types.DESIGNATOR, 'time_cutoff': 3.1, 'energy_cutoff': 3.1, 'weight_cutoff1': 3.1, 'weight_cutoff2': 3.1, 'source_weight': 3.1},
            {
                'designator': consts.ast.types.DESIGNATOR,
                'time_cutoff': consts.ast.types.REAL,
                'energy_cutoff': consts.ast.types.REAL,
                'weight_cutoff1': consts.ast.types.REAL,
                'weight_cutoff2': consts.ast.types.REAL,
                'source_weight': consts.ast.types.REAL,
            },
            {
                'designator': consts.string.types.DESIGNATOR,
                'time_cutoff': None,
                'energy_cutoff': consts.string.types.REAL,
                'weight_cutoff1': consts.string.types.REAL,
                'weight_cutoff2': consts.string.types.REAL,
                'source_weight': consts.string.types.REAL,
            },
            {
                'designator': consts.string.types.DESIGNATOR,
                'time_cutoff': consts.string.types.REAL,
                'energy_cutoff': None,
                'weight_cutoff1': consts.string.types.REAL,
                'weight_cutoff2': consts.string.types.REAL,
                'source_weight': consts.string.types.REAL,
            },
            {
                'designator': consts.string.types.DESIGNATOR,
                'time_cutoff': consts.string.types.REAL,
                'energy_cutoff': consts.string.types.REAL,
                'weight_cutoff1': None,
                'weight_cutoff2': consts.string.types.REAL,
                'source_weight': consts.string.types.REAL,
            },
            {
                'designator': consts.string.types.DESIGNATOR,
                'time_cutoff': consts.string.types.REAL,
                'energy_cutoff': consts.string.types.REAL,
                'weight_cutoff1': consts.string.types.REAL,
                'weight_cutoff2': None,
                'source_weight': consts.string.types.REAL,
            },
            {
                'designator': consts.string.types.DESIGNATOR,
                'time_cutoff': consts.string.types.REAL,
                'energy_cutoff': consts.string.types.REAL,
                'weight_cutoff1': consts.string.types.REAL,
                'weight_cutoff2': consts.string.types.REAL,
                'source_weight': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'designator': None,
                'time_cutoff': consts.string.types.REAL,
                'energy_cutoff': consts.string.types.REAL,
                'weight_cutoff1': consts.string.types.REAL,
                'weight_cutoff2': consts.string.types.REAL,
                'source_weight': consts.string.types.REAL,
            }
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Cut
        EXAMPLES_VALID = [consts.string.inp.CUT]
        EXAMPLES_INVALID = ['hello']
