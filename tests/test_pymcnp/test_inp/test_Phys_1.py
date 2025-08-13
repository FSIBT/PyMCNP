import pymcnp
from ... import consts
from ... import classes


class Test_Phys_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Phys_1
        EXAMPLES_VALID = [
            {
                'emcpf': consts.string.types.REAL,
                'ides': consts.string.types.INTEGER,
                'nocoh': consts.string.types.INTEGER,
                'ispn': consts.string.types.INTEGER,
                'nodop': consts.string.types.INTEGER,
                'fism': consts.string.types.INTEGER,
            },
            {'emcpf': 3.1, 'ides': 1, 'nocoh': 1, 'ispn': 1, 'nodop': 1, 'fism': 1},
            {
                'emcpf': consts.ast.types.REAL,
                'ides': consts.ast.types.INTEGER,
                'nocoh': consts.ast.types.INTEGER,
                'ispn': consts.ast.types.INTEGER,
                'nodop': consts.ast.types.INTEGER,
                'fism': consts.ast.types.INTEGER,
            },
            {
                'emcpf': None,
                'ides': consts.string.types.INTEGER,
                'nocoh': consts.string.types.INTEGER,
                'ispn': consts.string.types.INTEGER,
                'nodop': consts.string.types.INTEGER,
                'fism': consts.string.types.INTEGER,
            },
            {
                'emcpf': consts.string.types.REAL,
                'ides': None,
                'nocoh': consts.string.types.INTEGER,
                'ispn': consts.string.types.INTEGER,
                'nodop': consts.string.types.INTEGER,
                'fism': consts.string.types.INTEGER,
            },
            {
                'emcpf': consts.string.types.REAL,
                'ides': consts.string.types.INTEGER,
                'nocoh': None,
                'ispn': consts.string.types.INTEGER,
                'nodop': consts.string.types.INTEGER,
                'fism': consts.string.types.INTEGER,
            },
            {
                'emcpf': consts.string.types.REAL,
                'ides': consts.string.types.INTEGER,
                'nocoh': consts.string.types.INTEGER,
                'ispn': None,
                'nodop': consts.string.types.INTEGER,
                'fism': consts.string.types.INTEGER,
            },
            {
                'emcpf': consts.string.types.REAL,
                'ides': consts.string.types.INTEGER,
                'nocoh': consts.string.types.INTEGER,
                'ispn': consts.string.types.INTEGER,
                'nodop': None,
                'fism': consts.string.types.INTEGER,
            },
            {
                'emcpf': consts.string.types.REAL,
                'ides': consts.string.types.INTEGER,
                'nocoh': consts.string.types.INTEGER,
                'ispn': consts.string.types.INTEGER,
                'nodop': consts.string.types.INTEGER,
                'fism': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'emcpf': consts.string.types.REAL,
                'ides': -9999,
                'nocoh': consts.string.types.INTEGER,
                'ispn': consts.string.types.INTEGER,
                'nodop': consts.string.types.INTEGER,
                'fism': consts.string.types.INTEGER,
            },
            {
                'emcpf': consts.string.types.REAL,
                'ides': consts.string.types.INTEGER,
                'nocoh': -9999,
                'ispn': consts.string.types.INTEGER,
                'nodop': consts.string.types.INTEGER,
                'fism': consts.string.types.INTEGER,
            },
            {
                'emcpf': consts.string.types.REAL,
                'ides': consts.string.types.INTEGER,
                'nocoh': consts.string.types.INTEGER,
                'ispn': -9999,
                'nodop': consts.string.types.INTEGER,
                'fism': consts.string.types.INTEGER,
            },
            {
                'emcpf': consts.string.types.REAL,
                'ides': consts.string.types.INTEGER,
                'nocoh': consts.string.types.INTEGER,
                'ispn': consts.string.types.INTEGER,
                'nodop': -9999,
                'fism': consts.string.types.INTEGER,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Phys_1
        EXAMPLES_VALID = [consts.string.inp.PHYS_1]
        EXAMPLES_INVALID = ['hello']
