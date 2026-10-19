import pymcnp


class Test_Torus:
    def test___init___valid(self) -> None:
        pymcnp._show.pyvista.Torus(0.5, 0.5, 0.5)
