import pymcnp


class Test_Wedge:
    def test___init___valid(self) -> None:
        pymcnp._show.pyvista.Wedge(0.5, 0.5, 0.5)
