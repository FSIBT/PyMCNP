import pymcnp
from ... import _utils


class Test_Phys_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Phys_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.PhysBuilder_0
        EXAMPLES_VALID = [
            {
                'emax': _utils.string.type.REAL,
                'emcnf': _utils.string.type.REAL,
                'iunr': _utils.string.type.INTEGER,
                'coilf': _utils.string.type.REAL,
                'cutn': _utils.string.type.INTEGER,
                'ngam': _utils.string.type.INTEGER,
                'i_int_model': _utils.string.type.INTEGER,
                'i_els_model': _utils.string.type.INTEGER,
            },
            {'emax': 3.1, 'emcnf': 3.1, 'iunr': 1, 'coilf': 3.1, 'cutn': 1, 'ngam': 1, 'i_int_model': 1, 'i_els_model': 1},
            {
                'emax': _utils.ast.type.REAL,
                'emcnf': _utils.ast.type.REAL,
                'iunr': _utils.ast.type.INTEGER,
                'coilf': _utils.ast.type.REAL,
                'cutn': _utils.ast.type.INTEGER,
                'ngam': _utils.ast.type.INTEGER,
                'i_int_model': _utils.ast.type.INTEGER,
                'i_els_model': _utils.ast.type.INTEGER,
            },
            {
                'emax': None,
                'emcnf': _utils.string.type.REAL,
                'iunr': _utils.string.type.INTEGER,
                'coilf': _utils.string.type.REAL,
                'cutn': _utils.string.type.INTEGER,
                'ngam': _utils.string.type.INTEGER,
                'i_int_model': _utils.string.type.INTEGER,
                'i_els_model': _utils.string.type.INTEGER,
            },
            {
                'emax': _utils.string.type.REAL,
                'emcnf': None,
                'iunr': _utils.string.type.INTEGER,
                'coilf': _utils.string.type.REAL,
                'cutn': _utils.string.type.INTEGER,
                'ngam': _utils.string.type.INTEGER,
                'i_int_model': _utils.string.type.INTEGER,
                'i_els_model': _utils.string.type.INTEGER,
            },
            {
                'emax': _utils.string.type.REAL,
                'emcnf': _utils.string.type.REAL,
                'iunr': None,
                'coilf': _utils.string.type.REAL,
                'cutn': _utils.string.type.INTEGER,
                'ngam': _utils.string.type.INTEGER,
                'i_int_model': _utils.string.type.INTEGER,
                'i_els_model': _utils.string.type.INTEGER,
            },
            {
                'emax': _utils.string.type.REAL,
                'emcnf': _utils.string.type.REAL,
                'iunr': _utils.string.type.INTEGER,
                'coilf': None,
                'cutn': _utils.string.type.INTEGER,
                'ngam': _utils.string.type.INTEGER,
                'i_int_model': _utils.string.type.INTEGER,
                'i_els_model': _utils.string.type.INTEGER,
            },
            {
                'emax': _utils.string.type.REAL,
                'emcnf': _utils.string.type.REAL,
                'iunr': _utils.string.type.INTEGER,
                'coilf': _utils.string.type.REAL,
                'cutn': None,
                'ngam': _utils.string.type.INTEGER,
                'i_int_model': _utils.string.type.INTEGER,
                'i_els_model': _utils.string.type.INTEGER,
            },
            {
                'emax': _utils.string.type.REAL,
                'emcnf': _utils.string.type.REAL,
                'iunr': _utils.string.type.INTEGER,
                'coilf': _utils.string.type.REAL,
                'cutn': _utils.string.type.INTEGER,
                'ngam': None,
                'i_int_model': _utils.string.type.INTEGER,
                'i_els_model': _utils.string.type.INTEGER,
            },
            {
                'emax': _utils.string.type.REAL,
                'emcnf': _utils.string.type.REAL,
                'iunr': _utils.string.type.INTEGER,
                'coilf': _utils.string.type.REAL,
                'cutn': _utils.string.type.INTEGER,
                'ngam': _utils.string.type.INTEGER,
                'i_int_model': None,
                'i_els_model': _utils.string.type.INTEGER,
            },
            {
                'emax': _utils.string.type.REAL,
                'emcnf': _utils.string.type.REAL,
                'iunr': _utils.string.type.INTEGER,
                'coilf': _utils.string.type.REAL,
                'cutn': _utils.string.type.INTEGER,
                'ngam': _utils.string.type.INTEGER,
                'i_int_model': _utils.string.type.INTEGER,
                'i_els_model': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'emax': _utils.string.type.REAL,
                'emcnf': _utils.string.type.REAL,
                'iunr': -9999,
                'coilf': _utils.string.type.REAL,
                'cutn': _utils.string.type.INTEGER,
                'ngam': _utils.string.type.INTEGER,
                'i_int_model': _utils.string.type.INTEGER,
                'i_els_model': _utils.string.type.INTEGER,
            },
            {
                'emax': _utils.string.type.REAL,
                'emcnf': _utils.string.type.REAL,
                'iunr': _utils.string.type.INTEGER,
                'coilf': _utils.string.type.REAL,
                'cutn': _utils.string.type.INTEGER,
                'ngam': -9999,
                'i_int_model': _utils.string.type.INTEGER,
                'i_els_model': _utils.string.type.INTEGER,
            },
            {
                'emax': _utils.string.type.REAL,
                'emcnf': _utils.string.type.REAL,
                'iunr': _utils.string.type.INTEGER,
                'coilf': _utils.string.type.REAL,
                'cutn': _utils.string.type.INTEGER,
                'ngam': _utils.string.type.INTEGER,
                'i_int_model': -9999,
                'i_els_model': _utils.string.type.INTEGER,
            },
            {
                'emax': _utils.string.type.REAL,
                'emcnf': _utils.string.type.REAL,
                'iunr': _utils.string.type.INTEGER,
                'coilf': _utils.string.type.REAL,
                'cutn': _utils.string.type.INTEGER,
                'ngam': _utils.string.type.INTEGER,
                'i_int_model': _utils.string.type.INTEGER,
                'i_els_model': -9999,
            },
        ]
