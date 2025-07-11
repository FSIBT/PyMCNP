import pymcnp
from .... import consts
from .... import classes


class Test_Phys_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Phys_1
        EXAMPLES_VALID = [
            {
                'emcpf': consts.string.type.REAL,
                'ides': consts.string.type.INTEGER,
                'nocoh': consts.string.type.INTEGER,
                'ispn': consts.string.type.INTEGER,
                'nodop': consts.string.type.INTEGER,
                'fism': consts.string.type.INTEGER,
            },
            {'emcpf': 3.1, 'ides': 1, 'nocoh': 1, 'ispn': 1, 'nodop': 1, 'fism': 1},
            {
                'emcpf': consts.ast.type.REAL,
                'ides': consts.ast.type.INTEGER,
                'nocoh': consts.ast.type.INTEGER,
                'ispn': consts.ast.type.INTEGER,
                'nodop': consts.ast.type.INTEGER,
                'fism': consts.ast.type.INTEGER,
            },
            {
                'emcpf': None,
                'ides': consts.string.type.INTEGER,
                'nocoh': consts.string.type.INTEGER,
                'ispn': consts.string.type.INTEGER,
                'nodop': consts.string.type.INTEGER,
                'fism': consts.string.type.INTEGER,
            },
            {
                'emcpf': consts.string.type.REAL,
                'ides': None,
                'nocoh': consts.string.type.INTEGER,
                'ispn': consts.string.type.INTEGER,
                'nodop': consts.string.type.INTEGER,
                'fism': consts.string.type.INTEGER,
            },
            {
                'emcpf': consts.string.type.REAL,
                'ides': consts.string.type.INTEGER,
                'nocoh': None,
                'ispn': consts.string.type.INTEGER,
                'nodop': consts.string.type.INTEGER,
                'fism': consts.string.type.INTEGER,
            },
            {
                'emcpf': consts.string.type.REAL,
                'ides': consts.string.type.INTEGER,
                'nocoh': consts.string.type.INTEGER,
                'ispn': None,
                'nodop': consts.string.type.INTEGER,
                'fism': consts.string.type.INTEGER,
            },
            {
                'emcpf': consts.string.type.REAL,
                'ides': consts.string.type.INTEGER,
                'nocoh': consts.string.type.INTEGER,
                'ispn': consts.string.type.INTEGER,
                'nodop': None,
                'fism': consts.string.type.INTEGER,
            },
            {
                'emcpf': consts.string.type.REAL,
                'ides': consts.string.type.INTEGER,
                'nocoh': consts.string.type.INTEGER,
                'ispn': consts.string.type.INTEGER,
                'nodop': consts.string.type.INTEGER,
                'fism': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'emcpf': consts.string.type.REAL,
                'ides': -9999,
                'nocoh': consts.string.type.INTEGER,
                'ispn': consts.string.type.INTEGER,
                'nodop': consts.string.type.INTEGER,
                'fism': consts.string.type.INTEGER,
            },
            {
                'emcpf': consts.string.type.REAL,
                'ides': consts.string.type.INTEGER,
                'nocoh': -9999,
                'ispn': consts.string.type.INTEGER,
                'nodop': consts.string.type.INTEGER,
                'fism': consts.string.type.INTEGER,
            },
            {
                'emcpf': consts.string.type.REAL,
                'ides': consts.string.type.INTEGER,
                'nocoh': consts.string.type.INTEGER,
                'ispn': -9999,
                'nodop': consts.string.type.INTEGER,
                'fism': consts.string.type.INTEGER,
            },
            {
                'emcpf': consts.string.type.REAL,
                'ides': consts.string.type.INTEGER,
                'nocoh': consts.string.type.INTEGER,
                'ispn': consts.string.type.INTEGER,
                'nodop': -9999,
                'fism': consts.string.type.INTEGER,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Phys_1
        EXAMPLES_VALID = [consts.string.inp.data.PHYS_1]
        EXAMPLES_INVALID = ['hello']
