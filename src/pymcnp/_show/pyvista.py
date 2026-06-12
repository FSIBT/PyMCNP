from __future__ import annotations

import math
import typing
import dataclasses

import numpy
import pyvista

from .. import abc


BOUND: typing.Final[float] = 100
RESOLUTION: typing.Final[int] = 256


@dataclasses.dataclass
class Visualization(abc.Visualization):
    """
    Represents PyVista visualizations.
    """

    def __post_init__(self) -> None:
        """
        Initializes PyVista visualizations.
        """

        pass

    def __add__(a, b: abc.Visualization) -> Visualization:
        """
        Merges PyVista visualizations, `a` and `b`.

        Parameters:
            a: PyVista visualization #1.
            b: PyVista visualization #2.

        Returns:
            Merged PyVista visualization.
        """

        assert isinstance(b, Visualization)

        vis = Visualization()
        vis.surface = a.surface.merge(b.surface)
        vis.cell = lambda p: a.cell(p) | b.cell(p)

        return vis

    def __and__(a, b: abc.Visualization) -> Visualization:
        """
        Intersects PyVista visualizations, `a` and `b`.

        Parameters:
            a: PyVista visualization #1.
            b: PyVista visualization #2.

        Returns:
            Intersection of PyVista visualizations.
        """

        assert isinstance(b, Visualization)

        vis = Visualization()
        vis.surface = a.surface.merge(b.surface)
        vis.cell = lambda p: a.cell(p) & b.cell(p)

        return vis

    def __or__(a, b: abc.Visualization) -> Visualization:
        """
        Unites PyVista visualizations, `a` and `b`.

        Parameters:
            a: PyVista visualization #1.
            b: PyVista visualization #2.

        Returns:
            Union of PyVista visualizations.
        """

        assert isinstance(b, Visualization)

        vis = Visualization()
        vis.surface = a.surface.merge(b.surface)
        vis.cell = lambda p: a.cell(p) | b.cell(p)

        return vis

    def __invert__(self) -> Visualization:
        """
        Negates PyVista visualizations.

        Returns:
            Complement of PyVista visualization.
        """

        vis = Visualization()
        vis.surface = self.surface
        vis.cell = lambda p: ~self.cell(p)

        return vis

    def rotate(self, axis: numpy.ndarray, angle: float, center: numpy.ndarray) -> Visualization:
        """
        Rotates PyVista visualizations.

        Parameters:
            axis: Axis of rotation.
            angle: Angle of rotation.
            center: Center of rotation.

        Returns:
            Rotated PyVista visualization.
        """

        if axis[0] or axis[1] or axis[2]:
            axis = axis / numpy.linalg.norm(axis)

        vis = Visualization()
        vis.surface = self.surface.rotate_vector(vector=(axis[0], axis[1], axis[2]), angle=angle, point=center)
        vis.cell = lambda p: self.cell(p) if angle and not (axis == 0).all() else self

        return vis

    def translate(self, vector: numpy.ndarray) -> Visualization:
        """
        Translates PyVista visualizations.

        Parameters:
            vector: Vector of translation.

        Returns:
            Translated PyVista visualizations.
        """

        vis = Visualization()
        vis.surface = self.surface.translate(xyz=(vector[0], vector[1], vector[2]))
        vis.cell = lambda p: self.cell(p - vector)

        return vis


@dataclasses.dataclass
class Box(abc.Box, Visualization):
    """
    Represents PyVista boxes.
    """

    def __post_init__(self) -> None:
        """
        Initializes PyVista boxes.

        Parameters:
            a: Side #1 length.
            b: Side #2 length.
            c: Side #3 length.
        """

        self.surface = pyvista.Box((0, self.a, 0, self.b, 0, self.c))
        self.cell = lambda p: ~numpy.all((p >= 0) & (p <= [self.a, self.b, self.c]), axis=1)


@dataclasses.dataclass
class ConeTruncated(abc.ConeTruncated, Visualization):
    """
    Represents PyVista truncated cones.
    """

    def __post_init__(self) -> None:
        """
        Initializes PyVista truncated cones.

        Parameters:
            h: Truncated cone height.
            r1: Truncated cone radius #1.
            r2: Truncated cone radius #2.
        """

        self.surface = (
            pyvista.UnstructuredGrid([4, 0, 1, 2, 3], [pyvista.CellType.QUAD], [[0, 0, 0], [self.r1, 0, 0], [self.r2, 0, self.h], [0, 0, self.h]])
            .extract_surface()
            .extrude_rotate(capping=True, resolution=RESOLUTION)
        )
        self.cell = lambda p: ~(p[:, 2] <= self.h) & (p[:, 2] >= 0) & (p[:, 0] ** 2 + p[:, 1] ** 2 <= (self.r1 + p[:, 2] / self.h * (self.r2 - self.r1)) ** 2)


@dataclasses.dataclass
class ConeUnbounded(abc.ConeUnbounded, Visualization):
    """
    Represents PyVista unbounded cones.
    """

    def __post_init__(self) -> None:
        """
        Initializes PyVista unbounded cones.

        Parameters:
            m: Cone slope.
            sign: Cone sheet.
        """

        self.surface = (
            pyvista.UnstructuredGrid([2, 0, 1], [pyvista.CellType.LINE], [(0, 0, 0), (BOUND, 0, BOUND * self.sign / self.m)]).extract_surface().extrude_rotate(resolution=RESOLUTION, capping=False)
        )
        self.cell = lambda p: ~(p[:, 0] ** 2 + p[:, 1] ** 2 == self.sign * self.m**2 * p[:, 2] ** 2)


@dataclasses.dataclass
class CylinderCircular(abc.CylinderCircular, Visualization):
    """
    Represents PyVista circular cylinders.
    """

    def __post_init__(self) -> None:
        """
        Initializes PyVista circular cylinders.

        Paremeters:
            r: Circular cylinder radius.
            h: Circular cylinder height.
        """

        self.surface = pyvista.Cylinder(radius=self.r, height=self.h, direction=(0.0, 0.0, 1.0))
        self.cell = lambda p: ~((p[:, 2] >= 0) & (p[:, 2] <= self.h) & (p[:, 0] ** 2 + p[:, 1] ** 2 <= self.r**2))


@dataclasses.dataclass
class CylinderElliptical(abc.CylinderElliptical, Visualization):
    """
    Represents PyVista elliptical cylinders.
    """

    def __post_init__(self) -> None:
        """
        Initializes PyVista elliptical cylinders.

        Paremeters:
            a: Elliptical cylinder major axis length.
            b: Elliptical cylinder minor axis length.
            h: Elliptical cylinder height.
        """

        self.surface = pyvista.ParametricSuperEllipsoid(xradius=self.a, yradius=self.b, zradius=self.h, n1=0.001)
        self.cell = lambda p: ~((p[:, 2] >= 0) & (p[:, 2] <= self.h) & ((p[:, 0] / self.a) ** 2 + (p[:, 1] / self.b) ** 2 <= 1))


@dataclasses.dataclass
class CylinderHexagonal(abc.CylinderHexagonal, Visualization):
    """
    Represents PyVista hexagonal cylinders.
    """

    def __post_init__(self) -> None:
        """
        Initializes PyVista hexagonal cylinders.

        Paremeters:
            a: Hexagon apothem length #1.
            b: Hexagon apothem length #2.
            c: Hexagon apothem length #3.
            h: Hexagon height.
        """

        points = [
            [self.a * math.cos((math.pi / 3) * 0), self.a * math.sin((math.pi / 3) * 0), 0],
            [self.a * math.cos((math.pi / 3) * 1), self.a * math.sin((math.pi / 3) * 1), 0],
            [self.b * math.cos((math.pi / 3) * 2), self.b * math.sin((math.pi / 3) * 2), 0],
            [self.b * math.cos((math.pi / 3) * 3), self.b * math.sin((math.pi / 3) * 3), 0],
            [self.c * math.cos((math.pi / 3) * 4), self.c * math.sin((math.pi / 3) * 4), 0],
            [self.c * math.cos((math.pi / 3) * 5), self.c * math.sin((math.pi / 3) * 5), 0],
            [self.a * math.cos((math.pi / 3) * 0), self.a * math.sin((math.pi / 3) * 0), self.h],
            [self.a * math.cos((math.pi / 3) * 1), self.a * math.sin((math.pi / 3) * 1), self.h],
            [self.b * math.cos((math.pi / 3) * 2), self.b * math.sin((math.pi / 3) * 2), self.h],
            [self.b * math.cos((math.pi / 3) * 3), self.b * math.sin((math.pi / 3) * 3), self.h],
            [self.c * math.cos((math.pi / 3) * 4), self.c * math.sin((math.pi / 3) * 4), self.h],
            [self.c * math.cos((math.pi / 3) * 5), self.c * math.sin((math.pi / 3) * 5), self.h],
        ]
        cells = [len(points), *list(range(len(points)))]

        self.surface = pyvista.UnstructuredGrid(cells, [pyvista.CellType.HEXAGONAL_PRISM], points)
        self.cell = lambda p: 0 <= p[:, 2] <= self.h and all(abs(p[:, 0] * math.cos(i * math.pi / 3) + p[:, 1] * math.sin(i * math.pi / 3)) <= (self.a, self.b, self.c)[i % 3] for i in range(6))


@dataclasses.dataclass
class CylinderUnbounded(abc.CylinderUnbounded, Visualization):
    """
    Represents PyVista unbounded cylinders.
    """

    def __post_init__(self) -> None:
        """
        Initializes PyVista unbounded cylinders.

        Paremeters:
            radius: Circular cylinder radius.
        """

        self.surface = pyvista.Cylinder(radius=self.radius, height=BOUND, direction=(0, 0, 1), capping=False)
        self.cell = lambda points: points[:, 0] ** 2 + points[:, 1] ** 2 <= self.radius**2


@dataclasses.dataclass
class Ellipsoid(abc.Ellipsoid, Visualization):
    """
    Represents PyVista ellipsoids.
    """

    def __post_init__(self) -> None:
        """
        Initializes PyVista ellipsoids.

        Paremeters:
            a: Ellipsoid major axis length.
            b: Ellipsoid minor axis length.
        """

        self.surface = pyvista.ParametricEllipsoid(xradius=self.a, yradius=self.b, zradius=self.b)
        self.cell = lambda p: (p[:, 0] / self.a) ** 2 + (p[:, 1] / self.b) ** 2 + (p[:, 2] / self.b) ** 2 <= 1


@dataclasses.dataclass
class Empty(abc.Empty, Visualization):
    """
    Represents PyVista empty shapes.
    """

    def __post_init__(self) -> None:
        """
        Initializes PyVista empty shapes.
        """

        self.surface = pyvista.PolyData()
        self.cell = lambda p: False


@dataclasses.dataclass
class Parallelipiped(abc.Parallelipiped, Visualization):
    """
    Represents PyVista parallelipipeds.
    """

    def __post_init__(self) -> None:
        """
        Initializes PyVista parallelipipeds.

        Paremeters:
            xmin: Parllelipied lower x bound.
            xmax: Parllelipied upper x bound.
            ymin: Parllelipied lower y bound.
            ymax: Parllelipied upper y bound.
            zmin: Parllelipied lower z bound.
            zmax: Parllelipied upper z bound.
        """

        self.surface = pyvista.Box(bounds=(self.xmin, self.xmax, self.ymin, self.ymax, self.zmin, self.zmax))
        self.cell = lambda p: ~numpy.all((p >= [self.xmin, self.ymin, self.zmin]) & (p <= [self.xmax, self.ymax, self.zmax]), axis=1)


@dataclasses.dataclass
class Plane(abc.Plane, Visualization):
    """
    Represents PyVista planes.
    """

    def __post_init__(self) -> None:
        """
        Initializes PyVista planes.

        Paremeters:
            a: Plane equation parameter #1.
            b: Plane equation parameter #2.
            c: Plane equation parameter #3.
            d: Plane equation parameter #4.
        """

        if self.c == 0 and self.b == 0:
            point = (self.d / self.a, 0, 0)
        elif self.c == 0 and self.a == 0:
            point = (0, self.d / self.b, 0)
        elif self.a == 0 and self.b == 0:
            point = (0, 0, self.d / self.c)
        elif self.a == 0:
            point = (0, 0, self.d / self.c)
        elif self.b == 0:
            point = (0, 0, self.d / self.c)
        elif self.c == 0:
            point = (0, self.d / self.b, 0)
        else:
            point = (0, 0, self.d)

        self.surface = pyvista.Plane(center=point, i_size=int(BOUND), j_size=int(BOUND), direction=(self.a, self.b, self.c))
        self.cell = lambda p: self.a * p[:, 0] + self.b * p[:, 1] + self.c * p[:, 2] - self.d > 0


@dataclasses.dataclass
class Sphere(abc.Sphere, Visualization):
    """
    Represents PyVista spheres.
    """

    def __post_init__(self) -> None:
        """
        Initializes PyVista spheres.

        Paremeters:
            r: Sphere radius.
        """

        self.surface = pyvista.Sphere(radius=self.r, center=numpy.zeros(3))
        self.cell = lambda p: ~(p[:, 0] ** 2 + p[:, 1] ** 2 + p[:, 2] ** 2 <= self.r**2)


@dataclasses.dataclass
class Torus(abc.Torus, Visualization):
    """
    Represents PyVista tori.
    """

    def __post_init__(self) -> None:
        """
        Initializes PyVista tori.

        Parameters:
            a: Torus tube semi-major axis length.
            b: Torus tube semi-minor axis length.
            r: Torus ring radius.
        """

        alpha = 2 * math.pi / RESOLUTION
        points = [[self.a * math.cos(alpha * i) + self.r, 0, self.b * math.sin(alpha * i)] for i in range(RESOLUTION)]
        ellipse = pyvista.UnstructuredGrid([len(points), *list(range(len(points)))], [pyvista.CellType.POLYGON], points)

        self.surface = ellipse.extract_surface().extrude_rotate(capping=False, resolution=RESOLUTION)
        self.cell = lambda p: (p[:, 0] ** 2 + (self.a - (p[:, 1] ** 2 / self.a**2 + p[:, 2] ** 2 / self.b**2) ** 0.5 * self.a) ** 2 - self.r**2) ** 2


@dataclasses.dataclass
class Wedge(abc.Wedge, Visualization):
    """
    Represents PyVista wedges.
    """

    def __post_init__(self) -> None:
        """
        Initializes PyVista wedges.

        Parameters:
            a: Wedge triangle base small side #1.
            b: Wedge triangle base small side #2.
            h: Wedge height.
        """

        points = [
            [0, 0, 0],
            [self.a, 0, 0],
            [0, self.b, 0],
            [0, 0, self.h],
            [self.a, 0, self.h],
            [0, self.b, self.h],
        ]

        self.surface = pyvista.UnstructuredGrid([len(points), *list(range(len(points)))], [pyvista.CellType.WEDGE], points)
        self.cell = lambda p: 0 <= p[:, 0] <= self.a and 0 <= p[:, 1] <= self.b and 0 <= p[:, 2] <= self.h and p[:, 0] / self.a + p[:1] / self.b <= 1


endpoint = abc.Endpoint(
    BOUND=BOUND,
    RESOLUTION=RESOLUTION,
    Visualization=Visualization,
    Box=Box,
    ConeTruncated=ConeTruncated,
    ConeUnbounded=ConeUnbounded,
    CylinderCircular=CylinderCircular,
    CylinderElliptical=CylinderElliptical,
    CylinderHexagonal=CylinderHexagonal,
    CylinderUnbounded=CylinderUnbounded,
    Ellipsoid=Ellipsoid,
    Empty=Empty,
    Parallelipiped=Parallelipiped,
    Plane=Plane,
    Sphere=Sphere,
    Torus=Torus,
    Wedge=Wedge,
)
