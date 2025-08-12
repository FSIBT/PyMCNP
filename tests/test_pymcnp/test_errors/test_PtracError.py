import pymcnp


class Test_PtracError:
    def test__str__(self):
        str(pymcnp.errors.PtracError(pymcnp.errors.PtracCode.SYNTAX_FILE, 'Hi'))
        str(pymcnp.errors.PtracError(pymcnp.errors.PtracCode.SYNTAX_BLOCK, 'Hi'))
        str(pymcnp.errors.PtracError(pymcnp.errors.PtracCode.SYNTAX_LINE, 'Hi'))
        str(pymcnp.errors.PtracError(pymcnp.errors.PtracCode.SYNTAX_KEYWORD, 'Hi'))
        str(pymcnp.errors.PtracError(pymcnp.errors.PtracCode.SEMANTICS_FILE, 'Hi'))
        str(pymcnp.errors.PtracError(pymcnp.errors.PtracCode.SEMANTICS_BLOCK, 'Hi'))
        str(pymcnp.errors.PtracError(pymcnp.errors.PtracCode.SEMANTICS_LINE, 'Hi'))
        str(pymcnp.errors.PtracError(pymcnp.errors.PtracCode.SEMANTICS_KEYWORD, 'Hi'))
