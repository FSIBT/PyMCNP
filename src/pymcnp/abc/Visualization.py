from __future__ import annotations

import abc
import typing
import dataclasses

import numpy


T = typing.TypeVar('T')


@dataclasses.dataclass
class Visualization(abc.ABC, typing.Generic[T]):
    """
    Represents visualizations.

    Attributes:
        surface: Underlying surface visualization.
        cell: Underlying cell visualization.
    """

    surface: typing.Any = dataclasses.field(init=False)
    cell: typing.Callable[[numpy.ndarray], bool] = dataclasses.field(init=False)

    @abc.abstractmethod
    def __post_init__(self) -> None:
        """
        Initializes visualizations.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def __add__(a: typing.Self, b: typing.Self) -> typing.Self:
        """
        Merges visualizations, `a` and `b`.

        Parameters:
            a: visualization #1.
            b: visualization #2.

        Returns:
            Merged visualization.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def __and__(a: typing.Self, b: typing.Self) -> typing.Self:
        """
        Intersects visualizations, `a` and `b`.

        Parameters:
            a: visualization #1.
            b: visualization #2.

        Returns:
            Intersection of visualizations.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def __or__(a: typing.Self, b: typing.Self) -> typing.Self:
        """
        Unites visualizations, `a` and `b`.

        Parameters:
            a: visualization #1.
            b: visualization #2.

        Returns:
            Union of visualizations.
        """

        raise NotImplementedError

    def __invert__(self) -> typing.Self:
        """
        Negates visualizations.

        Returns:
            Complement of visualization.
        """

        raise NotImplementedError

    def rotate(self, axis: numpy.ndarray, angle: float, center: numpy.ndarray) -> T:
        """
        Rotates visualizations.

        Parameters:
            axis: Axis of rotation.
            angle: Angle of rotation.
            center: Center of rotation.

        Returns:
            Rotated visualization.
        """

        raise NotImplementedError

    def translate(self, vector: numpy.ndarray) -> T:
        """
        Translates visualizations.

        Parameters:
            vector: Vector of translation.

        Returns:
            Translated visualizations.
        """

        raise NotImplementedError


@dataclasses.dataclass
class Box(Visualization):
    """
    Represents boxes.
    """

    a: float
    b: float
    c: float


@dataclasses.dataclass
class ConeTruncated(Visualization):
    """
    Represents truncated cones.
    """

    h: float
    r1: float
    r2: float


@dataclasses.dataclass
class ConeUnbounded(Visualization):
    """
    Represents unbounded cones.
    """

    m: float
    sign: int


@dataclasses.dataclass
class CylinderCircular(Visualization):
    """
    Represents circular cylinders.
    """

    h: float
    r: float


@dataclasses.dataclass
class CylinderElliptical(Visualization):
    """
    Represents elliptical cylinders.
    """

    h: float
    a: float
    b: float


@dataclasses.dataclass
class CylinderHexagonal(Visualization):
    """
    Represents hexagonal cylinders.
    """

    h: float
    a: float
    b: float
    c: float


@dataclasses.dataclass
class CylinderUnbounded(Visualization):
    """
    Represents unbounded cylinders.
    """

    radius: float


@dataclasses.dataclass
class Ellipsoid(Visualization):
    """
    Represents ellipsoids.
    """

    a: float
    b: float


@dataclasses.dataclass
class Empty(Visualization):
    """
    Represents empty shapes.
    """


@dataclasses.dataclass
class Parallelipiped(Visualization):
    """
    Represents parallelipipeds.
    """

    xmin: float
    xmax: float
    ymin: float
    ymax: float
    zmin: float
    zmax: float


@dataclasses.dataclass
class Plane(Visualization):
    """
    Represents planes.
    """

    a: float
    b: float
    c: float
    d: float


@dataclasses.dataclass
class Sphere(Visualization):
    """
    Represents spheres.
    """

    r: float


@dataclasses.dataclass
class Torus(Visualization):
    """
    Represents tori.
    """

    a: float
    b: float
    r: float


@dataclasses.dataclass
class Wedge(Visualization):
    """
    Represents wedges.
    """

    a: float
    b: float
    h: float


@dataclasses.dataclass
class Endpoint(abc.ABC):
    """
    Represents visualization endpoints.

    Attributes:
        BOUND: Endpoint bound setting.
        RESOLUTION: Endpoint resolution setting.
        Box: Endpoint box visualization class.
        ConeTruncated: Endpoint truncated cone visualization class.
        ConeUnbounded: Endpoint unbounded cone visualization class.
        CylinderCircular: Endpoint circular cylinder visualization class.
        CylinderElliptical: Endpoint elliptical cylinder visualization class.
        CylinderHexagonal: Endpoint hexagonal cylinder visualization class.
        CylinderUnbounded: Endpoint unbounded cylinder visualization class.
        Ellipsoid: Endpoint ellipsoid visualization class.
        Empty: Endpoint empty visualization class.
        Parallelipiped: Endpoint parallelipiped visualization class.
        Plane: Endpoint plane visualization class.
        Sphere: Endpoint sphere visualization class.
        Torus: Endpoint torus visualization class.
        Wedge: Endpoint wedge visualization class.
    """

    BOUND: typing.Final[float]
    RESOLUTION: typing.Final[int]
    Visualization: typing.Final[type[Visualization]]
    Box: typing.Final[type[Box]]
    ConeTruncated: typing.Final[type[ConeTruncated]]
    ConeUnbounded: typing.Final[type[ConeUnbounded]]
    CylinderCircular: typing.Final[type[CylinderCircular]]
    CylinderElliptical: typing.Final[type[CylinderElliptical]]
    CylinderHexagonal: typing.Final[type[CylinderHexagonal]]
    CylinderUnbounded: typing.Final[type[CylinderUnbounded]]
    Ellipsoid: typing.Final[type[Ellipsoid]]
    Empty: typing.Final[type[Empty]]
    Parallelipiped: typing.Final[type[Parallelipiped]]
    Plane: typing.Final[type[Plane]]
    Sphere: typing.Final[type[Sphere]]
    Torus: typing.Final[type[Torus]]
    Wedge: typing.Final[type[Wedge]]
