import pymcnp


class Test_Sphere:
    def test___init___valid(self) -> None:
        pymcnp._show.pyvista.Sphere(0.5)
