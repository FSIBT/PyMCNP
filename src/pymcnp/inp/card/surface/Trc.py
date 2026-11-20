import typing

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Trc(Surface):
    """
    Represents trc surface cards.

    Attributes:
        prefix: trc surface card ``prefix`` parameter.
        j: trc surface card ``j`` parameter.
        keyword: trc surface card ``r'TRC'`` symbol.
        vx: trc surface card ``vx`` parameter.
        vy: trc surface card ``vy`` parameter.
        vz: trc surface card ``vz`` parameter.
        h1: trc surface card ``h1`` parameter.
        h2: trc surface card ``h2`` parameter.
        h3: trc surface card ``h3`` parameter.
        r1: trc surface card ``r1`` parameter.
        r2: trc surface card ``r2`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    keyword: typing.Annotated[abc.Terminal, r'TRC'] = abc.Terminal[r'TRC']('TRC')
    vx: literal.Real
    vy: literal.Real
    vz: literal.Real
    h1: literal.Real
    h2: literal.Real
    h3: literal.Real
    r1: literal.Real
    r2: literal.Real

    def __post_init__(self) -> None:
        """
        Validates trc surface cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes trc surface cards.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of trc surface cards.
        """

        h = numpy.array((float(self.h1), float(self.h2), float(self.h3)))

        cross = numpy.cross(h, numpy.array((0, 0, 1)))
        angle = numpy.degrees(numpy.arccos(h[2] / numpy.linalg.norm(h)))

        vis = shapes.ConeTruncated(float(numpy.linalg.norm(h)), float(self.r1), float(self.r2))
        vis = vis.rotate(cross, angle, numpy.zeros(3))
        vis = vis.translate(numpy.array((float(self.vx), float(self.vy), float(self.vz))))

        return vis
