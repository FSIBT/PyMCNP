import pymcnp


class Test_Plane:
    def test___init___valid(self) -> None:
        pymcnp._show.pyvista.Plane(0.5, 0, 0, 0)
        pymcnp._show.pyvista.Plane(0.5, 0, 0, 0.5)
        pymcnp._show.pyvista.Plane(0.5, 0, 0.5, 0)
        pymcnp._show.pyvista.Plane(0.5, 0, 0.5, 0.5)
        pymcnp._show.pyvista.Plane(0.5, 0.5, 0, 0)
        pymcnp._show.pyvista.Plane(0.5, 0.5, 0, 0.5)
        pymcnp._show.pyvista.Plane(0.5, 0.5, 0.5, 0)
        pymcnp._show.pyvista.Plane(0.5, 0.5, 0.5, 0.5)
        # pymcnp._show.pyvista.Plane(0, 0, 0, 0)
        # pymcnp._show.pyvista.Plane(0, 0, 0, 0.5)
        pymcnp._show.pyvista.Plane(0, 0, 0.5, 0)
        pymcnp._show.pyvista.Plane(0, 0, 0.5, 0.5)
        pymcnp._show.pyvista.Plane(0, 0.5, 0, 0)
        pymcnp._show.pyvista.Plane(0, 0.5, 0, 0.5)
        pymcnp._show.pyvista.Plane(0, 0.5, 0.5, 0)
        pymcnp._show.pyvista.Plane(0, 0.5, 0.5, 0.5)
