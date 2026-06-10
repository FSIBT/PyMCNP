import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Trc(Surface):
    """
    Represents trc surface cards.

    Attributes:
        prefix: trc surface card `prefix` parameter.
        j: trc surface card `j` parameter.
        keyword: trc surface card `TRC` symbol.
        vx: trc surface card `vx` parameter.
        vy: trc surface card `vy` parameter.
        vz: trc surface card `vz` parameter.
        h1: trc surface card `h1` parameter.
        h2: trc surface card `h2` parameter.
        h3: trc surface card `h3` parameter.
        r1: trc surface card `r1` parameter.
        r2: trc surface card `r2` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    keyword: typing.Annotated[abc.Terminal, r'TRC'] | str = abc.Terminal[r'TRC']('TRC')
    vx: literal.Real | int | float | decimal.Decimal | str
    vy: literal.Real | int | float | decimal.Decimal | str
    vz: literal.Real | int | float | decimal.Decimal | str
    h1: literal.Real | int | float | decimal.Decimal | str
    h2: literal.Real | int | float | decimal.Decimal | str
    h3: literal.Real | int | float | decimal.Decimal | str
    r1: literal.Real | int | float | decimal.Decimal | str
    r2: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates trc surface cards.
        """

        assert isinstance(self.j, literal.Integer)

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Trc`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Trc`
        """

        h = numpy.array((float(self.h1), float(self.h2), float(self.h3)))

        cross = numpy.cross(h, numpy.array((0, 0, 1)))
        angle = numpy.degrees(numpy.arccos(h[2] / numpy.linalg.norm(h)))

        vis = shapes.ConeTruncated(numpy.linalg.norm(h), float(self.r1), float(self.r2))
        vis = vis.rotate(cross, angle, (0, 0, 0))
        vis = vis.translate(numpy.array((float(self.vx), float(self.vy), float(self.vz))))

        return vis
