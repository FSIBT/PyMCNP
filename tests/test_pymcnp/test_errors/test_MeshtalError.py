import pymcnp


class Test_MeshtalError:
    def test__str__(self):
        str(pymcnp.errors.MeshtalError(pymcnp.errors.MeshtalCode.SYNTAX_FILE, 'Hi'))
        str(pymcnp.errors.MeshtalError(pymcnp.errors.MeshtalCode.SYNTAX_BLOCK, 'Hi'))
        str(pymcnp.errors.MeshtalError(pymcnp.errors.MeshtalCode.SYNTAX_LINE, 'Hi'))
        str(pymcnp.errors.MeshtalError(pymcnp.errors.MeshtalCode.SEMANTICS_FILE, 'Hi'))
        str(pymcnp.errors.MeshtalError(pymcnp.errors.MeshtalCode.SEMANTICS_BLOCK, 'Hi'))
        str(pymcnp.errors.MeshtalError(pymcnp.errors.MeshtalCode.SEMANTICS_LINE, 'Hi'))
