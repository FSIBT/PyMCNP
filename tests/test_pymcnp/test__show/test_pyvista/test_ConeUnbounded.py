import pymcnp


class Test_ConeUnbounded:
    def test___init___valid(self) -> None:
        pymcnp._show.pyvista.ConeUnbounded(0.5, 1)
