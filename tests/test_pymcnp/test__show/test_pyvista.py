import numpy
import pytest

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


SHAPE_NAMES = (
    'Box',
    'ConeTruncated',
    'ConeUnbounded',
    'CylinderCircular',
    'CylinderElliptical',
    'CylinderHexagonal',
    'CylinderUnbounded',
    'Ellipsoid',
    'Empty',
    'Parallelipiped',
    'Plane',
    'Sphere',
    'Torus',
    'Wedge',
)

POINTS = numpy.random.default_rng(0).uniform(-2, 2, (50, 3))


def _shape(request: pytest.FixtureRequest, name: str) -> pymcnp._show.pyvista.Visualization:
    show = pymcnp._show.pyvista

    if name == 'inverted sphere':
        return ~show.Sphere(1)
    if name == 'rotated box':
        return show.Box(1, 1.5, 2).rotate(axis=[0, 0, 1], angle=30, center=[0, 0, 0])

    return request.getfixturevalue('pyvista_shapes')[name]


@pytest.mark.parametrize('name', (*SHAPE_NAMES, 'inverted sphere', 'rotated box'))
def test_cell_is_vectorized(request: pytest.FixtureRequest, name: str) -> None:
    mask = _shape(request, name).cell(POINTS)

    assert isinstance(mask, numpy.ndarray)
    assert mask.shape == (50,)
    assert mask.dtype == bool


def test_cell_shapes_cover_every_class(pyvista_shapes: dict[str, pymcnp._show.pyvista.Visualization]) -> None:
    assert set(pyvista_shapes) == set(SHAPE_NAMES)


def test_cell_values() -> None:
    show = pymcnp._show.pyvista
    inside = numpy.array([[0.5, 0.5, 0.5], [2, 0.5, 0.5], [-0.1, 0.5, 0.5]])

    assert show.Box(1, 1, 1).cell(inside).tolist() == [True, False, False]
    assert show.Parallelipiped(0, 1, 0, 1, 0, 1).cell(inside).tolist() == [True, False, False]
    assert show.Sphere(1).cell(numpy.array([[0, 0, 0], [2, 0, 0]])).tolist() == [True, False]
    assert show.Empty().cell(inside).tolist() == [False, False, False]
    assert show.Wedge(1, 1, 1).cell(numpy.array([[0.1, 0.1, 0.5], [0.9, 0.9, 0.5], [2, 0, 0]])).tolist() == [True, False, False]
    assert show.CylinderHexagonal(1, 1, 1, 1).cell(numpy.array([[0, 0, 0.5], [0, 0, 2], [5, 0, 0.5]])).tolist() == [True, False, False]
    assert show.ConeTruncated(2, 1, 0.5).cell(numpy.array([[0.9, 0, 0], [0.9, 0, 2], [0.7, 0, 1], [0.8, 0, 1]])).tolist() == [True, False, True, False]
    assert show.ConeUnbounded(1, 1).cell(numpy.array([[0.5, 0, 1], [2, 0, 1], [0.5, 0, -1]])).tolist() == [True, False, False]
    assert show.Torus(0.5, 0.5, 2).cell(numpy.array([[2, 0, 0], [0, 0, 0], [0, 2, 0.4]])).tolist() == [True, False, True]
    assert show.Plane(1, 0, 0, 1).cell(numpy.array([[0, 0, 0], [2, 0, 0]])).tolist() == [True, False]


def test_rotate_matches_pointwise() -> None:
    show = pymcnp._show.pyvista
    box = show.Box(1, 1.5, 2)
    rotated = box.rotate(axis=[0, 0, 1], angle=30, center=[0, 0, 0])

    mask = rotated.cell(POINTS)
    assert mask.tolist() == [rotated.cell(POINTS[i : i + 1])[0] for i in range(50)]

    # Numeric check against the scalar Rodrigues formula (inverse angle).
    theta = numpy.radians(-30)
    c, s = numpy.cos(theta), numpy.sin(theta)
    rot = numpy.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    assert mask.tolist() == box.cell(POINTS @ rot.T).tolist()

    inside = numpy.array([[0.5, 0.5, 1.0]])
    assert box.cell(inside)[0]
    th = numpy.radians(30)
    forward = numpy.array([[numpy.cos(th), -numpy.sin(th), 0], [numpy.sin(th), numpy.cos(th), 0], [0, 0, 1]])
    assert rotated.cell(inside @ forward.T)[0]


def test_rotate_about_center() -> None:
    show = pymcnp._show.pyvista
    rotated = show.Box(1, 1, 1).rotate(axis=numpy.array([0, 1, 0]), angle=90, center=numpy.array([5.0, 0, 0]))

    # +90 degrees about y around (5, 0, 0) maps (0.5, 0.5, 0.5) to (5.5, 0.5, 4.5).
    assert rotated.cell(numpy.array([[5.5, 0.5, 4.5], [0.5, 0.5, 0.5]])).tolist() == [True, False]


def test_complement() -> None:
    show = pymcnp._show.pyvista

    assert (~show.Sphere(1)).cell(numpy.array([[0, 0, 0], [2, 0, 0]])).tolist() == [False, True]
