import pymcnp


class Test_CylinderCircular:
    def test___init___valid(self) -> None:
        pymcnp._show.pyvista.CylinderCircular(0.5, 0.5)
