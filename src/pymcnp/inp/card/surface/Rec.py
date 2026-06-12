import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ..Surface import Surface
from ... import literal


class Rec(Surface):
    """
    Represents rec surface cards.
    """

    pass


class Rec_0(Rec):
    """
    Represents rec surface cards, form #0.

    Attributes:
        prefix: rec surface card `prefix` parameter.
        j: rec surface card `j` parameter.
        keyword: rec surface card `REC` symbol.
        vx: rec surface card `vx` parameter.
        vy: rec surface card `vy` parameter.
        vz: rec surface card `vz` parameter.
        h1: rec surface card `h1` parameter.
        h2: rec surface card `h2` parameter.
        h3: rec surface card `h3` parameter.
        v1x: rec surface card `v1x` parameter.
        v1y: rec surface card `v1y` parameter.
        v1z: rec surface card `v1z` parameter.
        v2x: rec surface card `v2x` parameter.
        v2y: rec surface card `v2y` parameter.
        v2z: rec surface card `v2z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    keyword: typing.Annotated[abc.Terminal, r'REC'] | str = abc.Terminal[r'REC']('REC')
    vx: literal.Real | int | float | decimal.Decimal | str
    vy: literal.Real | int | float | decimal.Decimal | str
    vz: literal.Real | int | float | decimal.Decimal | str
    h1: literal.Real | int | float | decimal.Decimal | str
    h2: literal.Real | int | float | decimal.Decimal | str
    h3: literal.Real | int | float | decimal.Decimal | str
    v1x: literal.Real | int | float | decimal.Decimal | str
    v1y: literal.Real | int | float | decimal.Decimal | str
    v1z: literal.Real | int | float | decimal.Decimal | str
    v2x: literal.Real | int | float | decimal.Decimal | str
    v2y: literal.Real | int | float | decimal.Decimal | str
    v2z: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates rec surface cards, form #0.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.j, literal.Integer)

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        h = numpy.array((float(self.h1), float(self.h2), float(self.h3)))
        v1 = numpy.array((float(self.v1x), float(self.v1y), float(self.v1z)))

        if not numpy.dot(h, v1) == 0:
            raise abc.Error('Invalid value.', f'{h=}\n{v1=}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes rcc surface cards, form #0.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of rcc surface cards, form #0.
        """

        v = numpy.array((float(self.vx), float(self.vy), float(self.vz)))
        h = numpy.array((float(self.h1), float(self.h2), float(self.h3)))
        v1 = numpy.array((float(self.v1x), float(self.v1y), float(self.v1z)))
        v2 = numpy.array((float(self.v2x), float(self.v2y), float(self.v2z)))

        cross = numpy.cross(v, numpy.array((0, 0, 1)))
        angle = numpy.degrees(numpy.arccos(v[2] / numpy.linalg.norm(v)))

        vis = shapes.CylinderElliptical(float(numpy.linalg.norm(h)), float(numpy.linalg.norm(v1)), float(numpy.linalg.norm(v2)))
        vis = vis.rotate(cross, angle, numpy.zeros(3))
        vis = vis.translate(v)

        return vis


class Rec_1(Rec):
    """
    Represents rec surface cards, form #1.

    Attributes:
        j: rec surface card `j` parameter.
        keyword: rec surface card `REC` symbol.
        vx: rec surface card `vx` parameter.
        vy: rec surface card `vy` parameter.
        vz: rec surface card `vz` parameter.
        h1: rec surface card `h1` parameter.
        h2: rec surface card `h2` parameter.
        h3: rec surface card `h3` parameter.
        v1x: rec surface card `v1x` parameter.
        v1y: rec surface card `v1y` parameter.
        v1z: rec surface card `v1z` parameter.
        v2x: rec surface card `v2x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    j: literal.Integer | int | str
    keyword: typing.Annotated[abc.Terminal, r'REC'] | str = abc.Terminal[r'REC']('REC')
    vx: literal.Real | int | float | decimal.Decimal | str
    vy: literal.Real | int | float | decimal.Decimal | str
    vz: literal.Real | int | float | decimal.Decimal | str
    h1: literal.Real | int | float | decimal.Decimal | str
    h2: literal.Real | int | float | decimal.Decimal | str
    h3: literal.Real | int | float | decimal.Decimal | str
    v1x: literal.Real | int | float | decimal.Decimal | str
    v1y: literal.Real | int | float | decimal.Decimal | str
    v1z: literal.Real | int | float | decimal.Decimal | str
    v2x: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates rec surface cards, form #1.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.j, literal.Integer)

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        h = numpy.array((float(self.h1), float(self.h2), float(self.h3)))
        v1 = numpy.array((float(self.v1x), float(self.v1y), float(self.v1z)))

        if not numpy.dot(h, v1) == 0:
            raise abc.Error('Invalid value.', f'{h=}\n{v1=}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes rec surface cards, form #1.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of rec surface cards, form #1.
        """

        v = numpy.array((float(self.vx), float(self.vy), float(self.vz)))
        h = numpy.array((float(self.h1), float(self.h2), float(self.h3)))
        v1 = numpy.array((float(self.v1x), float(self.v1y), float(self.v1z)))
        v2 = numpy.cross(h, v1)
        v2 = (v2 / numpy.linalg.norm(v2)) * float(self.v2x)

        cross = numpy.cross(v, numpy.array((0, 0, 1)))
        angle = numpy.degrees(numpy.arccos(v[2] / numpy.linalg.norm(v)))

        vis = shapes.CylinderElliptical(float(numpy.linalg.norm(h)), float(numpy.linalg.norm(v1)), float(numpy.linalg.norm(v2)))
        vis = vis.rotate(cross, angle, numpy.zeros(3))
        vis = vis.translate(v)

        return vis
