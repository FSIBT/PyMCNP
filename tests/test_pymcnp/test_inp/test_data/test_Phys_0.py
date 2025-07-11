import pymcnp
from .... import consts
from .... import classes


class Test_Phys_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Phys_0
        EXAMPLES_VALID = [
            {
                'emax': consts.string.type.REAL,
                'emcnf': consts.string.type.REAL,
                'iunr': consts.string.type.INTEGER,
                'coilf': consts.string.type.REAL,
                'cutn': consts.string.type.INTEGER,
                'ngam': consts.string.type.INTEGER,
                'i_int_model': consts.string.type.INTEGER,
                'i_els_model': consts.string.type.INTEGER,
            },
            {'emax': 3.1, 'emcnf': 3.1, 'iunr': 1, 'coilf': 3.1, 'cutn': 1, 'ngam': 1, 'i_int_model': 1, 'i_els_model': 1},
            {
                'emax': consts.ast.type.REAL,
                'emcnf': consts.ast.type.REAL,
                'iunr': consts.ast.type.INTEGER,
                'coilf': consts.ast.type.REAL,
                'cutn': consts.ast.type.INTEGER,
                'ngam': consts.ast.type.INTEGER,
                'i_int_model': consts.ast.type.INTEGER,
                'i_els_model': consts.ast.type.INTEGER,
            },
            {
                'emax': None,
                'emcnf': consts.string.type.REAL,
                'iunr': consts.string.type.INTEGER,
                'coilf': consts.string.type.REAL,
                'cutn': consts.string.type.INTEGER,
                'ngam': consts.string.type.INTEGER,
                'i_int_model': consts.string.type.INTEGER,
                'i_els_model': consts.string.type.INTEGER,
            },
            {
                'emax': consts.string.type.REAL,
                'emcnf': None,
                'iunr': consts.string.type.INTEGER,
                'coilf': consts.string.type.REAL,
                'cutn': consts.string.type.INTEGER,
                'ngam': consts.string.type.INTEGER,
                'i_int_model': consts.string.type.INTEGER,
                'i_els_model': consts.string.type.INTEGER,
            },
            {
                'emax': consts.string.type.REAL,
                'emcnf': consts.string.type.REAL,
                'iunr': None,
                'coilf': consts.string.type.REAL,
                'cutn': consts.string.type.INTEGER,
                'ngam': consts.string.type.INTEGER,
                'i_int_model': consts.string.type.INTEGER,
                'i_els_model': consts.string.type.INTEGER,
            },
            {
                'emax': consts.string.type.REAL,
                'emcnf': consts.string.type.REAL,
                'iunr': consts.string.type.INTEGER,
                'coilf': None,
                'cutn': consts.string.type.INTEGER,
                'ngam': consts.string.type.INTEGER,
                'i_int_model': consts.string.type.INTEGER,
                'i_els_model': consts.string.type.INTEGER,
            },
            {
                'emax': consts.string.type.REAL,
                'emcnf': consts.string.type.REAL,
                'iunr': consts.string.type.INTEGER,
                'coilf': consts.string.type.REAL,
                'cutn': None,
                'ngam': consts.string.type.INTEGER,
                'i_int_model': consts.string.type.INTEGER,
                'i_els_model': consts.string.type.INTEGER,
            },
            {
                'emax': consts.string.type.REAL,
                'emcnf': consts.string.type.REAL,
                'iunr': consts.string.type.INTEGER,
                'coilf': consts.string.type.REAL,
                'cutn': consts.string.type.INTEGER,
                'ngam': None,
                'i_int_model': consts.string.type.INTEGER,
                'i_els_model': consts.string.type.INTEGER,
            },
            {
                'emax': consts.string.type.REAL,
                'emcnf': consts.string.type.REAL,
                'iunr': consts.string.type.INTEGER,
                'coilf': consts.string.type.REAL,
                'cutn': consts.string.type.INTEGER,
                'ngam': consts.string.type.INTEGER,
                'i_int_model': None,
                'i_els_model': consts.string.type.INTEGER,
            },
            {
                'emax': consts.string.type.REAL,
                'emcnf': consts.string.type.REAL,
                'iunr': consts.string.type.INTEGER,
                'coilf': consts.string.type.REAL,
                'cutn': consts.string.type.INTEGER,
                'ngam': consts.string.type.INTEGER,
                'i_int_model': consts.string.type.INTEGER,
                'i_els_model': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'emax': consts.string.type.REAL,
                'emcnf': consts.string.type.REAL,
                'iunr': -9999,
                'coilf': consts.string.type.REAL,
                'cutn': consts.string.type.INTEGER,
                'ngam': consts.string.type.INTEGER,
                'i_int_model': consts.string.type.INTEGER,
                'i_els_model': consts.string.type.INTEGER,
            },
            {
                'emax': consts.string.type.REAL,
                'emcnf': consts.string.type.REAL,
                'iunr': consts.string.type.INTEGER,
                'coilf': consts.string.type.REAL,
                'cutn': consts.string.type.INTEGER,
                'ngam': -9999,
                'i_int_model': consts.string.type.INTEGER,
                'i_els_model': consts.string.type.INTEGER,
            },
            {
                'emax': consts.string.type.REAL,
                'emcnf': consts.string.type.REAL,
                'iunr': consts.string.type.INTEGER,
                'coilf': consts.string.type.REAL,
                'cutn': consts.string.type.INTEGER,
                'ngam': consts.string.type.INTEGER,
                'i_int_model': -9999,
                'i_els_model': consts.string.type.INTEGER,
            },
            {
                'emax': consts.string.type.REAL,
                'emcnf': consts.string.type.REAL,
                'iunr': consts.string.type.INTEGER,
                'coilf': consts.string.type.REAL,
                'cutn': consts.string.type.INTEGER,
                'ngam': consts.string.type.INTEGER,
                'i_int_model': consts.string.type.INTEGER,
                'i_els_model': -9999,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Phys_0
        EXAMPLES_VALID = [consts.string.inp.data.PHYS_0]
        EXAMPLES_INVALID = ['hello']
