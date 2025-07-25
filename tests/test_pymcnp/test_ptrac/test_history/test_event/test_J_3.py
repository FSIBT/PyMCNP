import pymcnp
from ..... import consts
from ..... import classes


class Test_J_3:
    class Test_Init(classes.Test_Init):
        element = pymcnp.ptrac.history.event.J_3
        EXAMPLES_VALID = [
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'node': consts.ast.types.INTEGER,
                'nsx_nsf_nter': consts.ast.types.REAL,
                'ntyn_mtp_angle_branch': consts.ast.types.INTEGER,
                'ipt': consts.ast.types.INTEGER,
                'ncl': consts.ast.types.INTEGER,
                'mat': consts.ast.types.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'next_type': None,
                'node': consts.ast.types.INTEGER,
                'nsx_nsf_nter': consts.ast.types.REAL,
                'ntyn_mtp_angle_branch': consts.ast.types.INTEGER,
                'ipt': consts.ast.types.INTEGER,
                'ncl': consts.ast.types.INTEGER,
                'mat': consts.ast.types.INTEGER,
            },
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'node': None,
                'nsx_nsf_nter': consts.ast.types.REAL,
                'ntyn_mtp_angle_branch': consts.ast.types.INTEGER,
                'ipt': consts.ast.types.INTEGER,
                'ncl': consts.ast.types.INTEGER,
                'mat': consts.ast.types.INTEGER,
            },
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'node': consts.ast.types.INTEGER,
                'nsx_nsf_nter': None,
                'ntyn_mtp_angle_branch': consts.ast.types.INTEGER,
                'ipt': consts.ast.types.INTEGER,
                'ncl': consts.ast.types.INTEGER,
                'mat': consts.ast.types.INTEGER,
            },
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'node': consts.ast.types.INTEGER,
                'nsx_nsf_nter': consts.ast.types.REAL,
                'ntyn_mtp_angle_branch': None,
                'ipt': consts.ast.types.INTEGER,
                'ncl': consts.ast.types.INTEGER,
                'mat': consts.ast.types.INTEGER,
            },
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'node': consts.ast.types.INTEGER,
                'nsx_nsf_nter': consts.ast.types.REAL,
                'ntyn_mtp_angle_branch': consts.ast.types.INTEGER,
                'ipt': None,
                'ncl': consts.ast.types.INTEGER,
                'mat': consts.ast.types.INTEGER,
            },
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'node': consts.ast.types.INTEGER,
                'nsx_nsf_nter': consts.ast.types.REAL,
                'ntyn_mtp_angle_branch': consts.ast.types.INTEGER,
                'ipt': consts.ast.types.INTEGER,
                'ncl': None,
                'mat': consts.ast.types.INTEGER,
            },
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'node': consts.ast.types.INTEGER,
                'nsx_nsf_nter': consts.ast.types.REAL,
                'ntyn_mtp_angle_branch': consts.ast.types.INTEGER,
                'ipt': consts.ast.types.INTEGER,
                'ncl': consts.ast.types.INTEGER,
                'mat': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.ptrac.history.event.J_3
        EXAMPLES_VALID = [consts.string.ptrac.history.event.J_3]
        EXAMPLES_INVALID = ['hello']
