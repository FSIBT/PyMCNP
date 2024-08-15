"""
'_cadquery'
"""


import math

import numpy as np


class cqVector:
    def __init__(self, x, y, z):
        """
        '__init__' initializes 'cqVector'
        """

        self.x = x
        self.y = y
        self.z = z

    def norm(self) -> float:
        """
        'norm' computes vectors' norm.
        """

        return np.linalg.norm([self.x, self.y, self.z])

    def apothem(self) -> float:
        """
        'apothem' computes vectors' apothem
        """

        return np.linalg.norm([self.x, self.y, self.z]) * 2 / math.sqrt(3)

    @staticmethod
    def cross(a: cqVector, b: cqVector) -> cqVector:
        """
        'cross' computes cross products.
        """

        return cqVector(np.cross([a.x, a.y, a.z], [b.x, b.y, b.z]))

    @staticmethod
    def angle(a: cqVector, b: cqVector) -> float:
        """
        'angle' computes angles between vectors.
        """

        return np.degrees(np.arccos(np.dot(a, b)))


def add_box(a: cqVector, b: cqVector, c: cqVector) -> str:
    """
    'add_box' adds boxes to Cadquery workplanes.
    """

    return (
        f".polyline(["
        f"(0, 0, 0), "
        f"({a.x}, {a.y}, {a.z}), "
        f"({a.x + b.x}, {a.y + b.y}, {a.z + b.z}), "
        f"({b.x}, {b.y}, {b.z}), "
        f"]).close()"
        f".polyline(["
        f"({c.x}, {c.y}, {c.z}), "
        f"({a.x + c.x}, {a.y + c.y}, {a.z + c.z}), "
        f"({a.x + b.x + c.x}, {a.y + b.y + c.y}, {a.z + b.z + c.z}), "
        f"({b.x + c.x}, {b.y + c.y}, {b.z + c.z}), "
        f"]).close()"
        f".loft()"
    )


def add_sphere(r: float) -> str:
    """
    'add_sphere' adds spheres to Cadquery workplanes.
    """

    return f".sphere({r})"


def add_cylinderCircle(h: float, r: float) -> str:
    """
    'add_cylinder' adds circular cylinders to Cadquery workplanes.
    """

    return f".cylinder({h}, {r})"


def add_cylinderPolygon(h: float, a: float) -> str:
    """
    'add_prism' adds ploygonal cylinders to Cadquery workplanes.
    """

    return f".sketch().regularPolygon({a}, 6).finalize().extrude({h})"


def add_cylinderEllipse(h: float, a: float, b: float) -> str:
    """
    'add_cylinderEllipse' adds elliptical cylinders to Cadquery workplanes.
    """

    return f".ellipse({a}, {b}.extrude({h}))"


def add_trancatedCone(h: float, r1: float, r2: float) -> str:
    """
    'add_trancatedCone' adds trancated cone to Cadquery workplanes.
    """

    return f".circle({r1})" f".workplane(offset={h})" f"/circle({r2})" f".loft()"


def add_ellipse() -> str:
    """
    'add_ellipse' adds ellipses to Cadquery workplanes.
    """

    return f".ellipseArc({b}, {a}, -90, 90).close().revolve(axisStart=(0, -{a}, 0), axisEnd=(0, {a}, 0))"


def add_translation(v: cqVector) -> str:
    return f".translate(({v.x}, {v.y}, {v.z}))"


def add_rotation(axis: cqVector, angle: float) -> str:
    return f".rotate(({-axis.x}, {-axis.y}, {-axis.z}), ({axis.x}, {axis.y}, {axis.z}), {angle})\n"
