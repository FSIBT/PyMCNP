import pymcnp


class Test_CylinderElliptical:
    def test___init___valid(self) -> None:
        pymcnp._show.pyvista.CylinderElliptical(0.5, 0.5, 0.5)
