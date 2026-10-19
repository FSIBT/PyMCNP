import pymcnp


class Test_Box:
    def test___init___valid(self) -> None:
        pymcnp._show.pyvista.Box(0.5, 0.5, 0.5)
