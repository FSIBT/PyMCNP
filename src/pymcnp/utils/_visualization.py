"""
Contains classes and functions for generating CADQUERY.
"""

import math
import typing

import numpy
import pyvista


_BOUND: typing.Final[float] = 500
_RESOLUTION: typing.Final[int] = 100
_UNBOUNDED_SIZE: typing.Final[float] = 1000

pyvista.global_theme.allow_empty_mesh = True


class Vector:
    """
    ``Vector`` represents vector for PyMCNP visualization.

    Attributes:
        x: Vector x component.
        y: Vector y component.
        z: Vector z component.
    """

    def __init__(self, x: float, y: float, z: float):
        """
        Initializes ``Vector``.
        """

        self.x: typing.Final[float] = x
        self.y: typing.Final[float] = y
        self.z: typing.Final[float] = z

    def norm(self) -> float:
        """
        Computes vector norms.

        Returns:
            Length of the ``Vector`` vector.
        """

        return numpy.linalg.norm([self.x, self.y, self.z])

    def apothem(self) -> float:
        """
        Computes vector apothems.

        Returns:
            Length of the apothem associated with the ``Vector`` vector.
        """

        return numpy.linalg.norm([self.x, self.y, self.z]) * 2 / math.sqrt(3)

    def __eq__(a, b) -> bool:
        """
        Checks for vector equality.

        Parameters:
            a: Operand ``Vector`` vector #1.
            b: Operand ``Vector`` vector #2.

        Returns:
            True/False if vectors are/aren't equal.
        """

        return a.x == b.x and a.y == b.y and a.z == b.z

    def __add__(a, b):
        """
        Computes sum of vectors.

        Parameters:
            a: Operand ``Vector`` vector #1.
            b: Operand ``Vector`` vector #2.

        Returns:
            Vector sum.
        """

        return Vector(a.x + b.x, a.y + b.y, a.z + b.z)

    def __sub__(a, b):
        """
        Computes difference of vectors.

        Parameters:
            a: Operand ``Vector`` vector #1.
            b: Operand ``Vector`` vector #2.

        Returns:
            Vector difference.
        """

        return Vector(a.x - b.x, a.y - b.y, a.z - b.z)

    def __mul__(a, b):
        """
        Computes cross products of vectors.

        Parameters:
            a: Operand ``Vector`` vector #1.
            b: Operand ``Vector`` vector #2.

        Returns:
            Cross product of vectors.
        """

        return Vector(*numpy.cross([a.x, a.y, a.z], [b.x, b.y, b.z]))

    def __matmul__(a, b) -> float:
        """
        Computes dot products of vectors.

        Parameters:
            a: Operand ``Vector`` vector #1.
            b: Operand ``Vector`` vector #2.

        Returns:
            Dot product of vectors.
        """

        return numpy.dot([a.x, a.y, a.z], [b.x, b.y, b.z])

    def __and__(a, b) -> float:
        """
        Computes angles between vectors.

        Parameters:
            a: Operand ``Vector`` vector #1.
            b: Operand ``Vector`` vector #2.

        Returns:
            Angle between vectors in degrees.
        """

        if a * b == Vector(0, 0, 0):
            return 0
        else:
            return numpy.degrees(numpy.arccos(a @ b))


class Visualization:
    """
    Represents PyMCNP visualizations of cells, surfaces, etc.

    ``Visualization`` specifies common methods and attributes for PyMCNP
    visualizations
    """

    def __init__(self, data: pyvista.PolyData = pyvista.PolyData()):
        """
        Initializes ``Visualization``.
        """

        self.data: typing.Final[pyvista.PolyData] = data

    @staticmethod
    def get_plane(a: float, b: float, c: float, d: float):
        """
        Creates PyVISTA planes.

        Paremeters:
            a: Plane equation parameter #1.
            b: Plane equation parameter #2.
            c: Plane equation parameter #3.
            d: Plane equation parameter #4.

        Returns:
            ``Visualization`` plane.
        """

        if c == 0 and b == 0 and a == 0:
            point = (0, 0, d)
        elif c == 0 and b == 0:
            point = (d / a, 0, 0)
        elif c == 0 and a == 0:
            point = (0, d / b, 0)
        elif a == 0 and b == 0:
            point = (0, 0, d / c)
        elif a == 0:
            point = (0, 0, d / c)
        elif b == 0:
            point = (0, 0, d / c)
        elif c == 0:
            point = (0, d / b, 0)
        else:
            point = (0, 0, d)

        return Visualization(
            pyvista.Plane(
                center=point,
                direction=(a, b, c),
                i_size=_UNBOUNDED_SIZE,
                j_size=_UNBOUNDED_SIZE,
            )
        )

    @staticmethod
    def get_box(a: float, b: float, c: float):
        """
        Creates PyVISTA boxes.

        Paremeters:
            a: Box side length #1.
            b: Box side length #2.
            c: Box side length #3.

        Returns:
            ``Visualization`` box.
        """

        return Visualization(
            pyvista.Box(
                bounds=(0, a, 0, b, 0, c),
            )
        )

    @staticmethod
    def get_parallelipiped(
        xmin: float, xmax: float, ymin: float, ymax: float, zmin: float, zmax: float
    ):
        """
        Creates PyVISTA parallelipipeds.

        Paremeters:
            xmin: Parllelipied lower x bound.
            xmax: Parllelipied upper x bound.
            ymin: Parllelipied lower y bound.
            ymax: Parllelipied upper y bound.
            zmin: Parllelipied lower z bound.
            zmax: Parllelipied upper z bound.

        Returns:
            ``Visualization`` parallelipiped.
        """

        return Visualization(
            pyvista.Box(
                bounds=(xmin, xmax, ymin, ymax, zmin, zmax),
            )
        )

    @staticmethod
    def get_sphere(r: float):
        """
        Creates PyVISTA spheres.

        Paremeters:
            r: Sphere radius.

        Returns:
            ``Visualization`` sphere.
        """

        return Visualization(
            pyvista.Sphere(
                radius=r,
                center=(0.0, 0.0, 0.0),
            )
        )

    @staticmethod
    def get_cylinder_unbounded(r: float):
        """
        Creates PyVISTA unbounded circular cylinders.

        Paremeters:
            r: Circular cylinder radius.

        Returns:
            ``Visualization`` circular cylinder.
        """

        return Visualization(
            pyvista.Cylinder(
                radius=r,
                height=_UNBOUNDED_SIZE,
                direction=(0.0, 0.0, 1.0),
                capping=False,
            )
        )

    @staticmethod
    def get_cylinder_circle(h: float, r: float):
        """
        Creates PyVISTA circular cylinders.

        Paremeters:
            r: Circular cylinder radius.
            h: Circular cylinder height.

        Returns:
            ``Visualization`` circular cylinder.
        """

        return Visualization(
            pyvista.Cylinder(
                radius=r,
                height=h,
                direction=(0.0, 0.0, 1.0),
            )
        )

    @staticmethod
    def get_cylinder_ellipse(h: float, a: float, b: float):
        """
        Creates PyVISTA elliptical cylinders.

        Paremeters:
            a: Elliptical cylinder major axis length.
            b: Elliptical cylinder minor axis length.
            h: Elliptical cylinder height.

        Returns:
            ``Visualization`` elliptical cylinder.
        """

        return Visualization(
            pyvista.ParametricSuperEllipsoid(
                xradius=a,
                yradius=b,
                zradius=h,
                n1=0.001,
            )
        )

    @staticmethod
    def get_cylinder_hexagon(h: float, a: float, b: float, c: float):
        """
        Creates PyVISTA hexagonal prism.

        Paremeters:
            a: Hexagon apothem length #1.
            b: Hexagon apothem length #2.
            c: Hexagon apothem length #3.
            h: Hexagon height.

        Returns:
            ``Visualization`` hexagonal prism.
        """

        points = [
            [a * math.cos((math.pi / 3) * 0), a * math.sin((math.pi / 3) * 0), 0.0],
            [a * math.cos((math.pi / 3) * 1), a * math.sin((math.pi / 3) * 1), 0.0],
            [b * math.cos((math.pi / 3) * 2), b * math.sin((math.pi / 3) * 2), 0.0],
            [b * math.cos((math.pi / 3) * 3), b * math.sin((math.pi / 3) * 3), 0.0],
            [c * math.cos((math.pi / 3) * 4), c * math.sin((math.pi / 3) * 4), 0.0],
            [c * math.cos((math.pi / 3) * 5), c * math.sin((math.pi / 3) * 5), 0.0],
            [a * math.cos((math.pi / 3) * 0), a * math.sin((math.pi / 3) * 0), h],
            [a * math.cos((math.pi / 3) * 1), a * math.sin((math.pi / 3) * 1), h],
            [b * math.cos((math.pi / 3) * 2), b * math.sin((math.pi / 3) * 2), h],
            [b * math.cos((math.pi / 3) * 3), b * math.sin((math.pi / 3) * 3), h],
            [c * math.cos((math.pi / 3) * 4), c * math.sin((math.pi / 3) * 4), h],
            [c * math.cos((math.pi / 3) * 5), c * math.sin((math.pi / 3) * 5), h],
        ]

        cells = [len(points), *list(range(len(points)))]

        return Visualization(
            pyvista.UnstructuredGrid(
                cells,
                [pyvista.CellType.HEXAGONAL_PRISM],
                points,
            )
        )

    @staticmethod
    def get_cone(r: float, h: float):
        """
        Creates PyVISTA cones.

        Parameters:
            r: Cone radius.

        Returns:
            ``Visualization`` cone.
        """

        return Visualization(
            pyvista.Cone(
                direction=(0.0, 0.0, 1),
                radius=r,
                height=h,
                resolution=_RESOLUTION,
            )
        )

    @staticmethod
    def get_cone_unbounded(m: float, sign: int):
        """
        Creates PyVISTA unbounded cones.

        Parameters:
            m: Cone slope.
            sign: Cone sheet.

        Returns:
            ``Visualization`` cone.
        """

        points = [(0, 0, 0), (_UNBOUNDED_SIZE, 0, _UNBOUNDED_SIZE * sign / m)]
        cells = [len(points), *list(range(len(points)))]
        line = pyvista.UnstructuredGrid(
            cells,
            [pyvista.CellType.LINE],
            points,
        )

        return Visualization(
            line.extract_surface().extrude_rotate(resolution=_RESOLUTION, capping=False)
        )

    @staticmethod
    def get_cone_truncated(h: float, r1: float, r2: float):
        """
        Creates PyVISTA truncated cones.

        Parameters:
            h: Truncated cone height.
            r1: Truncated cone radius #1.
            r2: Truncated cone radius #2.

        Returns:
            ``Visualization`` truncated cone.
        """

        points = [[0, 0, 0], [r1, 0, 0], [r2, 0, h], [0, 0, h]]
        cells = [len(points), *list(range(len(points)))]
        trapazoid = pyvista.UnstructuredGrid(cells, [pyvista.CellType.QUAD], points)

        return Visualization(
            trapazoid.extract_surface().extrude_rotate(capping=True, resolution=_RESOLUTION)
        )

    @staticmethod
    def get_ellipsoid(a: float, b: float):
        """
        Creates PyVISTA ellipsoids.

        Paremeters:
            a: Ellipsoid major axis length.
            b: Ellipsoid minor axis length.

        Returns:
            ``Visualization`` ellipsoid.
        """

        return Visualization(
            pyvista.ParametricEllipsoid(
                xradius=a,
                yradius=b,
                zradius=b,
            )
        )

    @staticmethod
    def get_wedge(a: float, b: float, h: float):
        """
        Creates PyVISTA wedge.

        Parameters:
            a: Wedge triangle base small side #1.
            b: Wedge triangle base small side #2.
            h: Wedge height.

        Returns:
            ``Visualization`` wedge.
        """

        points = [
            [0, 0, 0],
            [a, 0, 0],
            [0, b, 0],
            [0, 0, h],
            [a, 0, h],
            [0, b, h],
        ]
        cells = [len(points), *list(range(len(points)))]

        return Visualization(
            pyvista.UnstructuredGrid(
                cells,
                [pyvista.CellType.WEDGE],
                points,
            )
        )

    @staticmethod
    def get_polyhedron(vertices: tuple[Vector], faces: tuple[tuple[int]]):
        """
        Creates PyVISTA polyhedron.

        Parameters:
            verticies: List of vertex vectors.
            faces: List of four vertex indicies.

        Returns:
            ``Visualization`` polyhedron.
        """

        vertices = numpy.array([[vertex.x, vertex.y, vertex.z] for vertex in vertices])
        faces = numpy.hstack(
            [[len(face), *[int((side - 1) % len(faces)) for side in face]] for face in faces]
        )

    @staticmethod
    def get_torus(a: float, b: float, r: float):
        """
        Creates PyVISTA tori.

        Parameters:
            a: Torus tube semi-major axis length.
            b: Torus tube semi-minor axis length.
            r: Torus ring radius.
        """

        alpha = 2 * math.pi / _RESOLUTION
        points = [
            [a * math.cos(alpha * i) + r, 0, b * math.sin(alpha * i)] for i in range(_RESOLUTION)
        ]
        cells = [len(points), *list(range(len(points)))]
        ellipse = pyvista.UnstructuredGrid(cells, [pyvista.CellType.POLYGON], points)

        return ellipse.extract_surface().extrude_rotate(
            capping=False,
            resolution=_RESOLUTION,
        )

    def add_translation(self, vector: Vector):
        """
        Translates ``Visualization`` instances.

        Parameters:
            vector: Translation vector.

        Returns:
            Translated ``Visualization``.
        """

        return Visualization(self.data.translate(xyz=(vector.x, vector.y, vector.z)))

    def add_rotation(self, axis: Vector, angle: float, center: tuple[float]):
        """
        Translates ``Visualization`` instances.

        Parameters:
            center: Center of rotation.

        Returns:
            Rotated ``Visualization``.
        """

        if axis.x == 0 and axis.y == 0 and axis.z == 0:
            return self
        else:
            return Visualization(
                self.data.rotate_vector(
                    vector=(axis.x, axis.y, axis.z),
                    angle=angle,
                    point=center,
                )
            )

    def add_bounds(self):
        """
        Bounds ``PyMcnpVisualuzation`` inside the bounding cube.

        Returns:
            Rotated ``Visualization``.
        """

        bound = pyvista.Cube(center=(0, 0, 0), x_length=_BOUND, y_length=_BOUND, z_length=_BOUND)

        return Visualization(self.data.clip_box(bound, invert=False))

    def plot(self):
        """
        Runs ``PyVisualization``.
        """

        plot = pyvista.Plotter()
        plot.add_mesh(self.data)
        plot.show()

    def __add__(a, b):
        """
        Adds ``Visualization`` instances.

        Parameters:
            a: Addend #1.
            b: Addend #2.

        Returns:
            Merged ``Visualization``.
        """

        return Visualization(pyvista.merge([a.data, b.data], merge_points=False))

    def __and__(a, b):
        """
        Unites ``Visualization``.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            ``Visualization`` union.
        """

        return Visualization(pyvista.merge([a.data, b.data], merge_points=True))

    def __or__(a, b):
        """
        Intersects ``Visualization``.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            ``Visualization`` intersection.
        """

        if not a.data.is_all_triangles:
            a.data = a.data.triangulate()
        if not b.data.is_all_triangles:
            b.data = b.data.triangulate()

        return Visualization(a.data.intersection(b.data)[0])

    def __invert__(a):
        """
        Inverts ``Visualization``.

        Parameters:
            a: Operand #1.

        Returns:
            ``Visualization`` complement.
        """

        return Visualization(a.data.flip_normals())
