import numpy
import pytest
import pyvista

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


@pytest.mark.parametrize('abc_', [(1.0, 1.0, 1.0), (1.0, 2.0, 1.5)])
def test_hexagonal_mask_matches_mesh(abc_: tuple[float, float, float]) -> None:
    """
    Probes just inside and just outside every face (and the 30 degree directions) against the mesh.
    """

    shape = pymcnp._show.pyvista.CylinderHexagonal(*abc_, 1.0)
    vertices = shape.surface.points[:6, :2]
    inner, expected = [], []

    for k in range(6):
        mid = (vertices[k] + vertices[(k + 1) % 6]) / 2
        for scale, flag in ((0.98, True), (1.02, False)):
            inner.append([*(mid * scale), 0.5])
            expected.append(flag)
    points = numpy.array(inner)

    assert shape.cell(points).tolist() == expected

    surface = shape.surface.extract_surface(algorithm='dataset_surface').triangulate().clean()
    enclosed = pyvista.PolyData(points).select_interior_points(surface, check_surface=False)
    assert enclosed['selected_points'].astype(bool).tolist() == expected

    assert not shape.cell(numpy.array([[0, 0, -0.1], [0, 0, 1.1]])).any()


# Every combination of zero and non-zero plane coefficients, since the drawn plane's center depends on which are zero.
PLANES = [
    (0.5, 0, 0, 0),
    (0.5, 0, 0, 0.5),
    (0.5, 0, 0.5, 0),
    (0.5, 0, 0.5, 0.5),
    (0.5, 0.5, 0, 0),
    (0.5, 0.5, 0, 0.5),
    (0.5, 0.5, 0.5, 0),
    pytest.param(0.5, 0.5, 0.5, 0.5, marks=pytest.mark.xfail(strict=True, reason='Plane draws its surface at (0, 0, d), off the plane, when a, b and c are all non-zero and c != 1')),
    (0, 0, 0.5, 0),
    (0, 0, 0.5, 0.5),
    (0, 0.5, 0, 0),
    (0, 0.5, 0, 0.5),
    (0, 0.5, 0.5, 0),
    (0, 0.5, 0.5, 0.5),
]


@pytest.mark.parametrize(('a', 'b', 'c', 'd'), PLANES)
def test_plane(a: float, b: float, c: float, d: float) -> None:
    plane = pymcnp._show.pyvista.Plane(a, b, c, d)

    assert plane.cell(POINTS).tolist() == (a * POINTS[:, 0] + b * POINTS[:, 1] + c * POINTS[:, 2] < d).tolist()
    assert numpy.dot((a, b, c), plane.surface.center) == pytest.approx(d)
