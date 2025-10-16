import pymcnp


class Test_OutpError:
    def test__str__(self):
        str(pymcnp.errors.OutpError(pymcnp.errors.OutpCode.SYNTAX_FILE, 'Hi'))
        str(pymcnp.errors.OutpError(pymcnp.errors.OutpCode.SYNTAX_TABLE, 'Hi'))
        str(pymcnp.errors.OutpError(pymcnp.errors.OutpCode.SEMANTICS_FILE, 'Hi'))
        str(pymcnp.errors.OutpError(pymcnp.errors.OutpCode.SEMANTICS_TABLE, 'Hi'))
