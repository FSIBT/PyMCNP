import pymcnp


class Test_InpError:
    def test__str__(self):
        str(pymcnp.errors.InpError(pymcnp.errors.InpCode.SYNTAX_FILE, 'Hi'))
        str(pymcnp.errors.InpError(pymcnp.errors.InpCode.SYNTAX_CARD, 'Hi'))
        str(pymcnp.errors.InpError(pymcnp.errors.InpCode.SYNTAX_OPTION, 'Hi'))
        str(pymcnp.errors.InpError(pymcnp.errors.InpCode.SYNTAX_ENTRY, 'Hi'))
        str(pymcnp.errors.InpError(pymcnp.errors.InpCode.SEMANTICS_FILE, 'Hi'))
        str(pymcnp.errors.InpError(pymcnp.errors.InpCode.SEMANTICS_CARD, 'Hi'))
        str(pymcnp.errors.InpError(pymcnp.errors.InpCode.SEMANTICS_OPTION, 'Hi'))
        str(pymcnp.errors.InpError(pymcnp.errors.InpCode.SEMANTICS_ENTRY, 'Hi'))
