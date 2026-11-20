import numpy

import pymcnp


class Test_Visualization:
    def test___add__(self, pyvista_visualizations: tuple[pymcnp._show.pyvista.Visualization, ...]) -> None:
        """
        Tests `__add__` on `pyvista_visualizations`.
        """

        for a in pyvista_visualizations:
            for b in pyvista_visualizations:
                a + b

    def test___and__(self, pyvista_visualizations: tuple[pymcnp._show.pyvista.Visualization, ...]) -> None:
        """
        Tests `__and__` on `pyvista_visualizations`.
        """

        for a in pyvista_visualizations:
            for b in pyvista_visualizations:
                a & b

    def test___or__(self, pyvista_visualizations: tuple[pymcnp._show.pyvista.Visualization, ...]) -> None:
        """
        Tests `__or__` on `pyvista_visualizations`.
        """

        for a in pyvista_visualizations:
            for b in pyvista_visualizations:
                a | b

    def test___invert__(self, pyvista_visualizations: tuple[pymcnp._show.pyvista.Visualization, ...]) -> None:
        """
        Tests `__invert__` on `pyvista_visualizations`.
        """

        for a in pyvista_visualizations:
            _ = ~a

    def test_rotate(self, pyvista_visualizations: tuple[pymcnp._show.pyvista.Visualization, ...]) -> None:
        """
        Tests `rotate` on `pyvista_visualizations`.
        """

        for a in pyvista_visualizations:
            a.rotate(numpy.array((1, 1, 1)), 0.5, numpy.array((1, 1, 1)))
            a.rotate(numpy.array((1, 1, 1)), 0, numpy.array((1, 1, 1)))

    def test_translate(self, pyvista_visualizations: tuple[pymcnp._show.pyvista.Visualization, ...]) -> None:
        """
        Tests `translate` on `pyvista_visualizations`.
        """

        for a in pyvista_visualizations:
            a.translate(numpy.array((1, 1, 1)))


class Test_Box:
    def test___post_init__(self) -> None:
        pymcnp._show.pyvista.Box(0.5, 0.5, 0.5)


class Test_ConeTruncated:
    def test___post_init__(self) -> None:
        pymcnp._show.pyvista.ConeTruncated(0.5, 0.5, 0.5)


class Test_ConeUnbounded:
    def test___post_init__(self) -> None:
        pymcnp._show.pyvista.ConeUnbounded(0.5, 1)


class Test_CylinderCircular:
    def test___post_init__(self) -> None:
        pymcnp._show.pyvista.CylinderCircular(0.5, 0.5)


class Test_CylinderElliptical:
    def test___post_init__(self) -> None:
        pymcnp._show.pyvista.CylinderElliptical(0.5, 0.5, 0.5)


class Test_CylinderHexagonal:
    def test___post_init__(self) -> None:
        pymcnp._show.pyvista.CylinderHexagonal(0.5, 0.5, 0.5, 0.5)


class Test_CylinderUnbounded:
    def test___post_init__(self) -> None:
        pymcnp._show.pyvista.CylinderUnbounded(0.5)


class Test_Ellipsoid:
    def test___post_init__(self) -> None:
        pymcnp._show.pyvista.Ellipsoid(0.5, 0.5)


class Test_Empty:
    def test___post_init__(self) -> None:
        pymcnp._show.pyvista.Empty()


class Test_Parallelipiped:
    def test___post_init__(self) -> None:
        pymcnp._show.pyvista.Parallelipiped(0.5, 0.5, 0.5, 0.5, 0.5, 0.5)


class Test_Plane:
    def test___post_init__(self) -> None:
        pymcnp._show.pyvista.Plane(0.5, 0, 0, 0)
        pymcnp._show.pyvista.Plane(0.5, 0, 0, 0.5)
        pymcnp._show.pyvista.Plane(0.5, 0, 0.5, 0)
        pymcnp._show.pyvista.Plane(0.5, 0, 0.5, 0.5)
        pymcnp._show.pyvista.Plane(0.5, 0.5, 0, 0)
        pymcnp._show.pyvista.Plane(0.5, 0.5, 0, 0.5)
        pymcnp._show.pyvista.Plane(0.5, 0.5, 0.5, 0)
        pymcnp._show.pyvista.Plane(0.5, 0.5, 0.5, 0.5)
        pymcnp._show.pyvista.Plane(0, 0, 0.5, 0)
        pymcnp._show.pyvista.Plane(0, 0, 0.5, 0.5)
        pymcnp._show.pyvista.Plane(0, 0.5, 0, 0)
        pymcnp._show.pyvista.Plane(0, 0.5, 0, 0.5)
        pymcnp._show.pyvista.Plane(0, 0.5, 0.5, 0)
        pymcnp._show.pyvista.Plane(0, 0.5, 0.5, 0.5)


class Test_Sphere:
    def test___post_init__(self) -> None:
        pymcnp._show.pyvista.Sphere(0.5)


class Test_Torus:
    def test___post_init__(self) -> None:
        pymcnp._show.pyvista.Torus(0.5, 0.5, 0.5)


class Test_Wedge:
    def test___post_init__(self) -> None:
        pymcnp._show.pyvista.Wedge(0.5, 0.5, 0.5)
