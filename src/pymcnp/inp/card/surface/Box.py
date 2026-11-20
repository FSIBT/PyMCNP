import typing

import numpy

from .... import abc
from .... import _show
from ..Surface import Surface
from ... import literal


class Box(Surface):
    """
    Represents box surface cards.
    """

    if typing.TYPE_CHECKING:
        prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
        j: literal.Integer
        keyword: typing.Annotated[abc.Terminal, r'BOX']
        vx: literal.Real
        vy: literal.Real
        vz: literal.Real
        a1x: literal.Real
        a1y: literal.Real
        a1z: literal.Real
        a2x: literal.Real
        a2y: literal.Real
        a2z: literal.Real


class Box_0(Box):
    """
    Represents box surface cards, form #0.

    Attributes:
        prefix: box surface card ``prefix`` parameter.
        j: box surface card ``j`` parameter.
        keyword: box surface card ``r'BOX'`` symbol.
        vx: box surface card ``vx`` parameter.
        vy: box surface card ``vy`` parameter.
        vz: box surface card ``vz`` parameter.
        a1x: box surface card ``a1x`` parameter.
        a1y: box surface card ``a1y`` parameter.
        a1z: box surface card ``a1z`` parameter.
        a2x: box surface card ``a2x`` parameter.
        a2y: box surface card ``a2y`` parameter.
        a2z: box surface card ``a2z`` parameter.
        a3x: box surface card ``a3x`` parameter.
        a3y: box surface card ``a3y`` parameter.
        a3z: box surface card ``a3z`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    keyword: typing.Annotated[abc.Terminal, r'BOX'] = abc.Terminal[r'BOX']('BOX')
    vx: literal.Real
    vy: literal.Real
    vz: literal.Real
    a1x: literal.Real
    a1y: literal.Real
    a1z: literal.Real
    a2x: literal.Real
    a2y: literal.Real
    a2z: literal.Real
    a3x: literal.Real
    a3y: literal.Real
    a3z: literal.Real

    def __post_init__(self) -> None:
        """
        Validates box surface cards, form #0.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        a1 = numpy.array((float(self.a1x), float(self.a1y), float(self.a1z)))
        a2 = numpy.array((float(self.a2x), float(self.a2y), float(self.a2z)))
        a3 = numpy.array((float(self.a3x), float(self.a3y), float(self.a3z)))

        if not numpy.dot(a1, a2) == 0 or not numpy.dot(a2, a3) == 0 or not numpy.dot(a3, a1) == 0:
            raise abc.Error('Invalid value.', f'{a1}\n{a2}\n{a3}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes box surface cards, form #0.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of box surface cards, form #0.
        """

        v = numpy.array((float(self.vx), float(self.vy), float(self.vz)))
        a1 = numpy.array((float(self.a1x), float(self.a1y), float(self.a1z)))
        a2 = numpy.array((float(self.a2x), float(self.a2y), float(self.a2z)))
        a3 = numpy.array((float(self.a3x), float(self.a3y), float(self.a3z)))

        cross = numpy.cross(numpy.array((1, 0, 0)), a1)
        angle = numpy.degrees(numpy.arccos(a1[0] / numpy.linalg.norm(a1)))

        vis = shapes.Box(float(numpy.linalg.norm(a1)), float(numpy.linalg.norm(a2)), float(numpy.linalg.norm(a3)))
        vis = vis.rotate(cross, angle, numpy.zeros(3))
        vis = vis.translate(v + 0.5 * (a1 + a2 + a3))

        return vis


class Box_1(Box):
    """
    Represents box surface cards, form #1.

    Attributes:
        prefix: box surface card ``prefix`` parameter.
        j: box surface card ``j`` parameter.
        keyword: box surface card ``r'BOX'`` symbol.
        vx: box surface card ``vx`` parameter.
        vy: box surface card ``vy`` parameter.
        vz: box surface card ``vz`` parameter.
        a1x: box surface card ``a1x`` parameter.
        a1y: box surface card ``a1y`` parameter.
        a1z: box surface card ``a1z`` parameter.
        a2x: box surface card ``a2x`` parameter.
        a2y: box surface card ``a2y`` parameter.
        a2z: box surface card ``a2z`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    keyword: typing.Annotated[abc.Terminal, r'BOX'] = abc.Terminal[r'BOX']('BOX')
    vx: literal.Real
    vy: literal.Real
    vz: literal.Real
    a1x: literal.Real
    a1y: literal.Real
    a1z: literal.Real
    a2x: literal.Real
    a2y: literal.Real
    a2z: literal.Real

    def __post_init__(self) -> None:
        """
        Validates box surface cards, form #1.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        a1 = numpy.array((float(self.a1x), float(self.a1y), float(self.a1z)))
        a2 = numpy.array((float(self.a2x), float(self.a2y), float(self.a2z)))

        if not numpy.dot(a1, a2) == 0:
            raise abc.Error('Invalid value.', f'{a1}\n{a2}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes box surface cards, form #1.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of box surface cards, form #1.
        """

        v = numpy.array((float(self.vx), float(self.vy), float(self.vz)))
        a1 = numpy.array((float(self.a1x), float(self.a1y), float(self.a1z)))
        a2 = numpy.array((float(self.a2x), float(self.a2y), float(self.a2z)))
        a3 = numpy.cross(a1, a2)

        cross = numpy.cross(numpy.array((1, 0, 0)), a1)
        angle = numpy.degrees(numpy.arccos(a1[0] / numpy.linalg.norm(a1)))

        vis = shapes.Box(float(numpy.linalg.norm(a1)), float(numpy.linalg.norm(a2)), float(numpy.linalg.norm(a3)))
        vis = vis.rotate(cross, angle, numpy.zeros(3))
        vis = vis.translate(v + 0.5 * (a1 + a2 + a3))

        return vis
