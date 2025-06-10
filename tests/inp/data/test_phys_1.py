import pymcnp
from ... import _utils


class Test_Phys_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Phys_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.PhysBuilder_1
        EXAMPLES_VALID = [
            {
                'emcpf': _utils.string.type.REAL,
                'ides': _utils.string.type.INTEGER,
                'nocoh': _utils.string.type.INTEGER,
                'ispn': _utils.string.type.INTEGER,
                'nodop': _utils.string.type.INTEGER,
                'fism': _utils.string.type.INTEGER,
            },
            {'emcpf': 3.1, 'ides': 1, 'nocoh': 1, 'ispn': 1, 'nodop': 1, 'fism': 1},
            {
                'emcpf': _utils.ast.type.REAL,
                'ides': _utils.ast.type.INTEGER,
                'nocoh': _utils.ast.type.INTEGER,
                'ispn': _utils.ast.type.INTEGER,
                'nodop': _utils.ast.type.INTEGER,
                'fism': _utils.ast.type.INTEGER,
            },
            {
                'emcpf': None,
                'ides': _utils.string.type.INTEGER,
                'nocoh': _utils.string.type.INTEGER,
                'ispn': _utils.string.type.INTEGER,
                'nodop': _utils.string.type.INTEGER,
                'fism': _utils.string.type.INTEGER,
            },
            {
                'emcpf': _utils.string.type.REAL,
                'ides': None,
                'nocoh': _utils.string.type.INTEGER,
                'ispn': _utils.string.type.INTEGER,
                'nodop': _utils.string.type.INTEGER,
                'fism': _utils.string.type.INTEGER,
            },
            {
                'emcpf': _utils.string.type.REAL,
                'ides': _utils.string.type.INTEGER,
                'nocoh': None,
                'ispn': _utils.string.type.INTEGER,
                'nodop': _utils.string.type.INTEGER,
                'fism': _utils.string.type.INTEGER,
            },
            {
                'emcpf': _utils.string.type.REAL,
                'ides': _utils.string.type.INTEGER,
                'nocoh': _utils.string.type.INTEGER,
                'ispn': None,
                'nodop': _utils.string.type.INTEGER,
                'fism': _utils.string.type.INTEGER,
            },
            {
                'emcpf': _utils.string.type.REAL,
                'ides': _utils.string.type.INTEGER,
                'nocoh': _utils.string.type.INTEGER,
                'ispn': _utils.string.type.INTEGER,
                'nodop': None,
                'fism': _utils.string.type.INTEGER,
            },
            {
                'emcpf': _utils.string.type.REAL,
                'ides': _utils.string.type.INTEGER,
                'nocoh': _utils.string.type.INTEGER,
                'ispn': _utils.string.type.INTEGER,
                'nodop': _utils.string.type.INTEGER,
                'fism': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'emcpf': _utils.string.type.REAL,
                'ides': -9999,
                'nocoh': _utils.string.type.INTEGER,
                'ispn': _utils.string.type.INTEGER,
                'nodop': _utils.string.type.INTEGER,
                'fism': _utils.string.type.INTEGER,
            },
            {
                'emcpf': _utils.string.type.REAL,
                'ides': _utils.string.type.INTEGER,
                'nocoh': -9999,
                'ispn': _utils.string.type.INTEGER,
                'nodop': _utils.string.type.INTEGER,
                'fism': _utils.string.type.INTEGER,
            },
            {
                'emcpf': _utils.string.type.REAL,
                'ides': _utils.string.type.INTEGER,
                'nocoh': _utils.string.type.INTEGER,
                'ispn': -9999,
                'nodop': _utils.string.type.INTEGER,
                'fism': _utils.string.type.INTEGER,
            },
            {
                'emcpf': _utils.string.type.REAL,
                'ides': _utils.string.type.INTEGER,
                'nocoh': _utils.string.type.INTEGER,
                'ispn': _utils.string.type.INTEGER,
                'nodop': -9999,
                'fism': _utils.string.type.INTEGER,
            },
        ]
