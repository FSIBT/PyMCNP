import pymcnp
from ... import consts
from ... import classes


class Test_Phys_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Phys_0
        EXAMPLES_VALID = [
            {
                'emax': consts.string.types.REAL,
                'emcnf': consts.string.types.REAL,
                'iunr': consts.string.types.INTEGER,
                'coilf': consts.string.types.REAL,
                'cutn': consts.string.types.INTEGER,
                'ngam': consts.string.types.INTEGER,
                'i_int_model': consts.string.types.INTEGER,
                'i_els_model': consts.string.types.INTEGER,
            },
            {'emax': 3.1, 'emcnf': 3.1, 'iunr': 1, 'coilf': 3.1, 'cutn': 1, 'ngam': 1, 'i_int_model': 1, 'i_els_model': 1},
            {
                'emax': consts.ast.types.REAL,
                'emcnf': consts.ast.types.REAL,
                'iunr': consts.ast.types.INTEGER,
                'coilf': consts.ast.types.REAL,
                'cutn': consts.ast.types.INTEGER,
                'ngam': consts.ast.types.INTEGER,
                'i_int_model': consts.ast.types.INTEGER,
                'i_els_model': consts.ast.types.INTEGER,
            },
            {
                'emax': None,
                'emcnf': consts.string.types.REAL,
                'iunr': consts.string.types.INTEGER,
                'coilf': consts.string.types.REAL,
                'cutn': consts.string.types.INTEGER,
                'ngam': consts.string.types.INTEGER,
                'i_int_model': consts.string.types.INTEGER,
                'i_els_model': consts.string.types.INTEGER,
            },
            {
                'emax': consts.string.types.REAL,
                'emcnf': None,
                'iunr': consts.string.types.INTEGER,
                'coilf': consts.string.types.REAL,
                'cutn': consts.string.types.INTEGER,
                'ngam': consts.string.types.INTEGER,
                'i_int_model': consts.string.types.INTEGER,
                'i_els_model': consts.string.types.INTEGER,
            },
            {
                'emax': consts.string.types.REAL,
                'emcnf': consts.string.types.REAL,
                'iunr': None,
                'coilf': consts.string.types.REAL,
                'cutn': consts.string.types.INTEGER,
                'ngam': consts.string.types.INTEGER,
                'i_int_model': consts.string.types.INTEGER,
                'i_els_model': consts.string.types.INTEGER,
            },
            {
                'emax': consts.string.types.REAL,
                'emcnf': consts.string.types.REAL,
                'iunr': consts.string.types.INTEGER,
                'coilf': None,
                'cutn': consts.string.types.INTEGER,
                'ngam': consts.string.types.INTEGER,
                'i_int_model': consts.string.types.INTEGER,
                'i_els_model': consts.string.types.INTEGER,
            },
            {
                'emax': consts.string.types.REAL,
                'emcnf': consts.string.types.REAL,
                'iunr': consts.string.types.INTEGER,
                'coilf': consts.string.types.REAL,
                'cutn': None,
                'ngam': consts.string.types.INTEGER,
                'i_int_model': consts.string.types.INTEGER,
                'i_els_model': consts.string.types.INTEGER,
            },
            {
                'emax': consts.string.types.REAL,
                'emcnf': consts.string.types.REAL,
                'iunr': consts.string.types.INTEGER,
                'coilf': consts.string.types.REAL,
                'cutn': consts.string.types.INTEGER,
                'ngam': None,
                'i_int_model': consts.string.types.INTEGER,
                'i_els_model': consts.string.types.INTEGER,
            },
            {
                'emax': consts.string.types.REAL,
                'emcnf': consts.string.types.REAL,
                'iunr': consts.string.types.INTEGER,
                'coilf': consts.string.types.REAL,
                'cutn': consts.string.types.INTEGER,
                'ngam': consts.string.types.INTEGER,
                'i_int_model': None,
                'i_els_model': consts.string.types.INTEGER,
            },
            {
                'emax': consts.string.types.REAL,
                'emcnf': consts.string.types.REAL,
                'iunr': consts.string.types.INTEGER,
                'coilf': consts.string.types.REAL,
                'cutn': consts.string.types.INTEGER,
                'ngam': consts.string.types.INTEGER,
                'i_int_model': consts.string.types.INTEGER,
                'i_els_model': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'emax': consts.string.types.REAL,
                'emcnf': consts.string.types.REAL,
                'iunr': -9999,
                'coilf': consts.string.types.REAL,
                'cutn': consts.string.types.INTEGER,
                'ngam': consts.string.types.INTEGER,
                'i_int_model': consts.string.types.INTEGER,
                'i_els_model': consts.string.types.INTEGER,
            },
            {
                'emax': consts.string.types.REAL,
                'emcnf': consts.string.types.REAL,
                'iunr': consts.string.types.INTEGER,
                'coilf': consts.string.types.REAL,
                'cutn': consts.string.types.INTEGER,
                'ngam': -9999,
                'i_int_model': consts.string.types.INTEGER,
                'i_els_model': consts.string.types.INTEGER,
            },
            {
                'emax': consts.string.types.REAL,
                'emcnf': consts.string.types.REAL,
                'iunr': consts.string.types.INTEGER,
                'coilf': consts.string.types.REAL,
                'cutn': consts.string.types.INTEGER,
                'ngam': consts.string.types.INTEGER,
                'i_int_model': -9999,
                'i_els_model': consts.string.types.INTEGER,
            },
            {
                'emax': consts.string.types.REAL,
                'emcnf': consts.string.types.REAL,
                'iunr': consts.string.types.INTEGER,
                'coilf': consts.string.types.REAL,
                'cutn': consts.string.types.INTEGER,
                'ngam': consts.string.types.INTEGER,
                'i_int_model': consts.string.types.INTEGER,
                'i_els_model': -9999,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Phys_0
        EXAMPLES_VALID = [consts.string.inp.PHYS_0]
        EXAMPLES_INVALID = ['hello']
