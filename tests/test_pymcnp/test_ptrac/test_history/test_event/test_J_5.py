import pymcnp
from ..... import consts
from ..... import classes


class Test_J_5:
    class Test_Init(classes.Test_Init):
        element = pymcnp.ptrac.history.event.J_5
        EXAMPLES_VALID = [
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'node': consts.ast.types.INTEGER,
                'nsx_nsf_nter': consts.ast.types.INTEGER,
                'ntyn_mtp_angle_branch': consts.ast.types.INTEGER,
                'ncl': consts.ast.types.INTEGER,
                'mat': consts.ast.types.INTEGER,
                'ncp': consts.ast.types.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'next_type': None,
                'node': consts.ast.types.INTEGER,
                'nsx_nsf_nter': consts.ast.types.INTEGER,
                'ntyn_mtp_angle_branch': consts.ast.types.INTEGER,
                'ncl': consts.ast.types.INTEGER,
                'mat': consts.ast.types.INTEGER,
                'ncp': consts.ast.types.INTEGER,
            },
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'node': None,
                'nsx_nsf_nter': consts.ast.types.INTEGER,
                'ntyn_mtp_angle_branch': consts.ast.types.INTEGER,
                'ncl': consts.ast.types.INTEGER,
                'mat': consts.ast.types.INTEGER,
                'ncp': consts.ast.types.INTEGER,
            },
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'node': consts.ast.types.INTEGER,
                'nsx_nsf_nter': None,
                'ntyn_mtp_angle_branch': consts.ast.types.INTEGER,
                'ncl': consts.ast.types.INTEGER,
                'mat': consts.ast.types.INTEGER,
                'ncp': consts.ast.types.INTEGER,
            },
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'node': consts.ast.types.INTEGER,
                'nsx_nsf_nter': consts.ast.types.INTEGER,
                'ntyn_mtp_angle_branch': None,
                'ncl': consts.ast.types.INTEGER,
                'mat': consts.ast.types.INTEGER,
                'ncp': consts.ast.types.INTEGER,
            },
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'node': consts.ast.types.INTEGER,
                'nsx_nsf_nter': consts.ast.types.INTEGER,
                'ntyn_mtp_angle_branch': consts.ast.types.INTEGER,
                'ncl': None,
                'mat': consts.ast.types.INTEGER,
                'ncp': consts.ast.types.INTEGER,
            },
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'node': consts.ast.types.INTEGER,
                'nsx_nsf_nter': consts.ast.types.INTEGER,
                'ntyn_mtp_angle_branch': consts.ast.types.INTEGER,
                'ncl': consts.ast.types.INTEGER,
                'mat': None,
                'ncp': consts.ast.types.INTEGER,
            },
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'node': consts.ast.types.INTEGER,
                'nsx_nsf_nter': consts.ast.types.INTEGER,
                'ntyn_mtp_angle_branch': consts.ast.types.INTEGER,
                'ncl': consts.ast.types.INTEGER,
                'mat': consts.ast.types.INTEGER,
                'ncp': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.ptrac.history.event.J_5
        EXAMPLES_VALID = [consts.string.ptrac.history.event.J_5]
        EXAMPLES_INVALID = ['hello']
