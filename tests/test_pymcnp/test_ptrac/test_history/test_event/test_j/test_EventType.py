import pymcnp
from ...... import consts
from ...... import classes


class Test_J_3:
    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.ptrac.history.event.j.EventType
        EXAMPLES_VALID = [consts.ast.ptrac.history.event.j.EVENT_TYPE]
        EXAMPLES_INVALID = ['hello']
