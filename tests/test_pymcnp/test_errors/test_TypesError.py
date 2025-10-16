import pymcnp


class Test_TypesError:
    def test__str__(self):
        str(pymcnp.errors.TypesError(pymcnp.errors.TypesCode.SYNTAX_TYPE, 'Hi'))
        str(pymcnp.errors.TypesError(pymcnp.errors.TypesCode.SEMANTICS_TYPE, 'Hi'))
