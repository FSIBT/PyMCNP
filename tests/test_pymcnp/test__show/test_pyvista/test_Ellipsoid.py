import pymcnp


class Test_Ellipsoid:
    def test___init___valid(self) -> None:
        pymcnp._show.pyvista.Ellipsoid(0.5, 0.5)
