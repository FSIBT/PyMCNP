"""
``_cadquery`` contains classes and methods for generating Cadquery code.

``_cadquery`` packages the ``CqVector`` class and adder methods, providing
private helper functions for generating Cadquery by abstracting Cadquery
patterns.
"""

from __future__ import annotations
import math

import numpy as np


class CqVector:
    """
    ``CqVector`` represents vectors in Cadquery workplanes.

    ``CqVector`` abstracts the vectors used in constructing, translating, and
    rotating Cadquery workplanes and INP visualizations.

    Attributes:
        x: Vector x component.
        y: Vector y component.
        z: Vector z component.
    """

    def __init__(self, x: float, y: float, z: float):
        """
        ``__init__`` initializes ``CqVector``.
        """

        self.x: float = x
        self.y: float = y
        self.z: float = z

    def norm(self) -> float:
        """
        ``norm`` computes vector norms.

        ``norm`` calculates the length of``CqVector`` vectors using the
        ``numpy`` package.

        Returns:
            Length of the ``CqVector`` vector.
        """

        return np.linalg.norm([self.x, self.y, self.z])

    def apothem(self) -> float:
        """
        ``apothem`` computes vector apothems.

        ``apothem`` calculates the apothem, i.e. the length of the line
        from the center of a polygon to its side given the vector points from
        the center of a polygon to a corner using the ``numpy`` package.

        Returns:
            Length of the apothem associated with the ``CqVector`` vector.
        """

        return np.linalg.norm([self.x, self.y, self.z]) * 2 / math.sqrt(3)

    @staticmethod
    def cross(a: CqVector, b: CqVector):
        """
        ``cross`` computes cross products of two vectors.

        ``cross`` calculates the cross products of the given ``CqVector``
        vectors using the ``numpy`` package.

        Parameters:
            a: Operand ``CqVector`` vector #1.
            b: Operand ``CqVector`` vector #2.

        Returns:
            ``CqVector`` cross product of ``a`` and ``b``.
        """

        return CqVector(*np.cross([a.x, a.y, a.z], [b.x, b.y, b.z]))

    @staticmethod
    def angle(a: CqVector, b: CqVector) -> float:
        """
        ``angle`` computes angles between vectors.

        ``angle`` calculates the angle between the given ``CqVector`` vectors
        using the ``numpy`` package.

        Parameters:
            a: Operand ``CqVector`` vector #1.
            b: Operand ``CqVector`` vector #2.

        Returns:
            Angle between ``a`` and ``b`` in degrees.
        """

        return np.degrees(np.arccos(np.dot([a.x, a.y, a.z], [b.x, b.y, b.z])))


def add_box(a: CqVector, b: CqVector, c: CqVector) -> str:
    """
    ``add_box`` adds boxes to Cadquery workplanes.

    ``add_box`` writes Cadquery to represent an arbitrarily oriented
    othogonal boxs given three orthogonal ``CqVector`` vectors representing
    a path along the box edges the in order ``a``, ``b``, ``c``. It substitutes
    vector endpoints into calls of the Cadquery ``polyline`` method which adds
    squares to the Cadquery workplane. ``add_box`` includes calls to ``loft``
    and ``close`` in its output to turn the sqaures into surfaces and loft them
    into boxs.

    Paremeters
        a: Operand ``CqVector`` vector #1.
        b: Operand ``CqVector`` vector #2.
        c: Operand ``CqVector`` vector #3.

    Returns:
        Cadquery representing an arbitrarily oriented othogonal box.
    """

    return (
        f'.polyline(['
        f'(0, 0, 0), '
        f'({a.x}, {a.y}, {a.z}), '
        f'({a.x + b.x}, {a.y + b.y}, {a.z + b.z}), '
        f'({b.x}, {b.y}, {b.z}), '
        f']).close()'
        f'.polyline(['
        f'({c.x}, {c.y}, {c.z}), '
        f'({a.x + c.x}, {a.y + c.y}, {a.z + c.z}), '
        f'({a.x + b.x + c.x}, {a.y + b.y + c.y}, {a.z + b.z + c.z}), '
        f'({b.x + c.x}, {b.y + c.y}, {b.z + c.z}), '
        f']).close()'
        f'.loft()'
    )


def add_sphere(r: float) -> str:
    """
    ``add_sphere`` adds shperes to Cadquery workplanes.

    ``add_sphere`` writes Cadquery to represent spheres given radii. It
    substitutes radii values into calls of the Cadquery ``sphere`` method which
    adds spheres to the Cadquery workplane.

    Paremeters
        r: Sphere radius.

    Returns:
        Cadquery representing a sphere.
    """

    return f'.sphere({r})'


def add_cylinder_circle(h: float, r: float) -> str:
    """
    ``add_cylinder_circle`` adds circular cylinders to Cadquery workplanes.

    ``add_cylinder_circle`` writes Cadquery to represent circular cylinder given
    radii and heights. It substitutes the these values into calls of the
    Cadquery ``cylinder`` method which adds cylidners to the workplane.

    Paremeters
        r: Circular cylinder radius.
        h: Circular cylinder height.

    Returns:
        Cadquery representing a circular cylinder.
    """

    return f'.cylinder({h}, {r})'


def add_prism_polygon(h: float, a: float, n: int = 6) -> str:
    """
    ``add_prism_polygon`` adds polygonal prisms to Cadquery workplanes.

    ``add_prism_polygon`` writes Cadquery to represent n-sided polygonal
    prisms given apothem lengths and heights. It substitutes the these values
    into calls of the Cadquery ``regularPolygon`` method which sketches these
    polygons in the Cadquery workplane. ``add_prism_polygon`` includes calls to
    ``sketch``, ``finalize``, and ``extrude`` to transform the polygon sketches
    into surfaces and extend them into polgyonal prisms.

    Paremeters
        a: n-Sided polygonal prism apothem length.
        h: n-Sided polygonal prism height.
        n: Number of sides of the polygon.

    Returns:
        Cadquery representing a n-polygonal prism.
    """

    return f'.sketch().regularPolygon({a}, {n}).finalize().extrude({h})'


def add_cylinder_ellipse(h: float, a: float, b: float) -> str:
    """
    ``add_cylinder_ellipse`` adds elliptical cylinders to Cadquery workplanes.

    ``add_cylinder_ellipse`` writes Cadquery to represent elliptical cylinder
    given minor and major axis length and heights. It substitutes these values
    into calls of the Cadquery ``ellipse`` method which adds ellipses to the
    Cadquery workplane. ``add_cylinder_ellipse`` includes calls to ``extrude``
    in its output to extend the ellipses into elliptical cylinders.

    Paremeters
        a: Elliptical cylinder major axis length.
        b: Elliptical cylinder minor axis length.
        h: Elliptical cylinder height.

    Returns:
        Cadquery representing an elliptical cylinder.
    """

    return f'.ellipse({a}, {b}).extrude({h})'


def add_cone_truncated(h: float, r1: float, r2: float) -> str:
    """
    ``add_cone_truncated`` adds truncated cones to Cadquery workplanes.

    ``add_cone_truncated`` writes Cadquery to represent truncated cones given
    two radii and heights. It substitutes these values into calls of the
    Cadquery ``circle`` method which adds circles to the Cadquery workplane.
    ``add_cone_truncated`` includes calls to ``loft`` in its output to loft the
    circles into truncated cones.

    Paremeters
        h: Truncated cone height.
        r1: Truncated cone radius #1.
        r2: Truncated cone radius #2.

    Returns:
        Cadquery representing a truncated cone.
    """

    return f'.circle({r1}).workplane(offset={h}).circle({r2}).loft()'


def add_ellipsoid(a: float, b: float) -> str:
    """
    ``add_ellipsoid`` adds ellipsoids to Cadquery workplanes.

    ``add_ellipsoid`` writes Cadquery to represent ellipsoids given minor and
    major axis length. It substitutes these values into calls of the Cadquery
    ``ellipseArc`` method which adds ellipsoids to the Cadquery workplane.
    ``add_cylinder_ellipse`` includes calls to ``revolove`` in its output to
    build a complete ellipsoid from an ellipse.

    Paremeters
        a: Ellipsoid major axis length.
        b: Ellipsoid minor axis length.

    Returns:
        Cadquery representing an ellispoid.
    """

    return f'.ellipseArc({a}, {b}, -90, 90).close().revolve(axisStart=(0, -{a}, 0), axisEnd=(0, {a}, 0))'


def add_wedge(a: CqVector, b: CqVector, c: CqVector) -> str:
    """
    ``add_wedge`` adds wedges to Cadquery workplanes.

    ``add_wedge`` writes Cadquery to represent wedges given three vectors. It
    substitutes these values into calls of the Cadquery ``polyline`` method
    which adds a sketchs wedges to the Cadquery workplane. ``add_wedge``
    includes calls to ``loft`` in its output to loft the polylines in to shape.

    Paremeters
        a: Wedge vector #1.
        b: Wedge vector #2.
        c: Wedge vector #3.

    Returns:
        Cadquery representing a wedge.
    """

    return (
        f'.polyline([({a.x}, {a.y}, {a.z}), (0, 0, 0), ({b.x}, {b.y}, {b.z})]).close().'
        'polyline([({a.x + c.x}, {a.y + c.y}, {a.z + c.z}), ({c.x}, {c.y}, {c.z}), ({b.x + c.x}, {b.y + c.y}, {b.z + c.z})]).'
        'close().loft()'
    )


def add_translation(v: CqVector) -> str:
    """
    ``add_translation`` adds translations to Cadquey workplanes.

    ``add_translation`` writes Cadquery to translate Cadquery workplanes given
    vectors specifiying the trasformation. It substitutes vectors' components
    into calls of the Cadquery ``translate`` method which moves the workplane
    based on the given vector.

    Parameters:
        v: Vector specifying the translation.

    Returns:
        Cadquery representing a truncated cone.
    """

    return f'.translate(({v.x}, {v.y}, {v.z}))'


def add_rotation(axis: CqVector, angle: float) -> str:
    """
    ``add_rotation`` adds rotations to Cadquey workplanes.

    ``add_rotation`` writes Cadquery to rotate Cadquery workplanes given axeses
    of rotation and angles. It substitutes axes' components and the angles into
    calls of the Cadquery ``rotate`` method which moves the workplane based
    on the given axis and angle.

    Parameters:
        v: Vector specifying the translation.
    """

    return f'.rotate(({-axis.x}, {-axis.y}, {-axis.z}), ({axis.x}, {axis.y}, {axis.z}), {angle})'
