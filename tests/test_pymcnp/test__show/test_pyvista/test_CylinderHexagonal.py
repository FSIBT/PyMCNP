import pymcnp


class Test_CylinderHexagonal:
    def test___init___valid(self) -> None:
        pymcnp._show.pyvista.CylinderHexagonal(0.5, 0.5, 0.5, 0.5)
