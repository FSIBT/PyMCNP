import pymcnp


class Test_CylinderUnbounded:
    def test___init___valid(self) -> None:
        pymcnp._show.pyvista.CylinderUnbounded(0.5)
