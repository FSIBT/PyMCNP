import math
import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ..Surface import Surface
from ... import literal


class Rhp(Surface):
    """
    Represents rhp surface cards.
    """

    pass


class Rhp_0(Rhp):
    """
    Represents rhp surface cards, form #0.

    Attributes:
        prefix: rhp surface card `prefix` parameter.
        j: rhp surface card `j` parameter.
        keyword: rhp surface card `RHP` symbol.
        vx: rhp surface card `vx` parameter.
        vy: rhp surface card `vy` parameter.
        vz: rhp surface card `vz` parameter.
        h1: rhp surface card `h1` parameter.
        h2: rhp surface card `h2` parameter.
        h3: rhp surface card `h3` parameter.
        r1: rhp surface card `r1` parameter.
        r2: rhp surface card `r2` parameter.
        r3: rhp surface card `r3` parameter.
        s1: rhp surface card `s1` parameter.
        s2: rhp surface card `s2` parameter.
        s3: rhp surface card `s3` parameter.
        t1: rhp surface card `t1` parameter.
        t2: rhp surface card `t2` parameter.
        t3: rhp surface card `t3` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    keyword: typing.Annotated[abc.Terminal, r'(?:RHP|HEX)'] | str = abc.Terminal[r'(?:RHP|HEX)']('RHP')
    vx: literal.Real | int | float | decimal.Decimal | str
    vy: literal.Real | int | float | decimal.Decimal | str
    vz: literal.Real | int | float | decimal.Decimal | str
    h1: literal.Real | int | float | decimal.Decimal | str
    h2: literal.Real | int | float | decimal.Decimal | str
    h3: literal.Real | int | float | decimal.Decimal | str
    r1: literal.Real | int | float | decimal.Decimal | str
    r2: literal.Real | int | float | decimal.Decimal | str
    r3: literal.Real | int | float | decimal.Decimal | str
    s1: literal.Real | int | float | decimal.Decimal | str
    s2: literal.Real | int | float | decimal.Decimal | str
    s3: literal.Real | int | float | decimal.Decimal | str
    t1: literal.Real | int | float | decimal.Decimal | str
    t2: literal.Real | int | float | decimal.Decimal | str
    t3: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates rhp surface cards, form #0.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.j, literal.Integer)

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes rhp surface cards, form #0.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of rhp surface cards, form #0.
        """

        v = numpy.array((float(self.vx), float(self.vy), float(self.vz)))
        h = numpy.array((float(self.h1), float(self.h2), float(self.h3)))
        r = numpy.array((float(self.r1), float(self.r2), float(self.r3)))
        s = numpy.array((float(self.s1), float(self.s2), float(self.s3)))
        t = numpy.array((float(self.t1), float(self.t2), float(self.t3)))

        cross = numpy.cross(v, numpy.array((0, 0, 1)))
        angle = numpy.degrees(numpy.arccos(v[2] / numpy.linalg.norm(v)))
        apothem_r = float(numpy.linalg.norm(r) * 2 / math.sqrt(3))
        apothem_s = float(numpy.linalg.norm(s) * 2 / math.sqrt(3))
        apothem_t = float(numpy.linalg.norm(t) * 2 / math.sqrt(3))

        vis = shapes.CylinderHexagonal(float(numpy.linalg.norm(h)), apothem_r, apothem_s, apothem_t)
        vis = vis.rotate(cross, angle, numpy.zeros(3))
        vis = vis.translate(v)

        return vis


class Rhp_1(Rhp):
    """
    Represents rhp surface cards, form #1.

    Attributes:
        j: rhp surface card `j` parameter.
        keyword: rhp surface card `RHP` symbol.
        vx: rhp surface card `vx` parameter.
        vy: rhp surface card `vy` parameter.
        vz: rhp surface card `vz` parameter.
        h1: rhp surface card `h1` parameter.
        h2: rhp surface card `h2` parameter.
        h3: rhp surface card `h3` parameter.
        r1: rhp surface card `r1` parameter.
        r2: rhp surface card `r2` parameter.
        r3: rhp surface card `r3` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    j: literal.Integer | int | str
    keyword: typing.Annotated[abc.Terminal, r'(?:RHP|HEX)'] | str = abc.Terminal[r'(?:RHP|HEX)']('RHP')
    vx: literal.Real | int | float | decimal.Decimal | str
    vy: literal.Real | int | float | decimal.Decimal | str
    vz: literal.Real | int | float | decimal.Decimal | str
    h1: literal.Real | int | float | decimal.Decimal | str
    h2: literal.Real | int | float | decimal.Decimal | str
    h3: literal.Real | int | float | decimal.Decimal | str
    r1: literal.Real | int | float | decimal.Decimal | str
    r2: literal.Real | int | float | decimal.Decimal | str
    r3: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates rhp surface cards, form #1.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.j, literal.Integer)

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')
