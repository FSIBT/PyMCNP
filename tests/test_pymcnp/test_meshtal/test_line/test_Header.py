import pymcnp
from .... import classes


class Test_Header(classes.Test_Nonterminal):
    element = pymcnp.meshtal.line.Header
    EXAMPLES_VALID = ['mcnp   version 6     ld=02/20/18  probid =  11/01/24 10:26:01 ']
    EXAMPLES_INVALID = [
        'hello',
    ]
