import pymcnp


class Test_Parallelipiped:
    def test___init___valid(self) -> None:
        pymcnp._show.pyvista.Parallelipiped(0.5, 0.5, 0.5, 0.5, 0.5, 0.5)
