import pymcnp


class Test_ConeTruncated:
    def test___init___valid(self) -> None:
        pymcnp._show.pyvista.ConeTruncated(0.5, 0.5, 0.5)
