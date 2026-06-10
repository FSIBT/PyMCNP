import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Rcc(Surface):
    """
    Represents rcc surface cards.

    Attributes:
        prefix: rcc surface card `prefix` parameter.
        j: rcc surface card `j` parameter.
        keyword: rcc surface card `RCC` symbol.
        vx: rcc surface card `vx` parameter.
        vy: rcc surface card `vy` parameter.
        vz: rcc surface card `vz` parameter.
        h1: rcc surface card `h1` parameter.
        h2: rcc surface card `h2` parameter.
        h3: rcc surface card `h3` parameter.
        r: rcc surface card `r` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    keyword: typing.Annotated[abc.Terminal, r'RCC'] | str = abc.Terminal[r'RCC']('RCC')
    vx: literal.Real | int | float | decimal.Decimal | str
    vy: literal.Real | int | float | decimal.Decimal | str
    vz: literal.Real | int | float | decimal.Decimal | str
    h1: literal.Real | int | float | decimal.Decimal | str
    h2: literal.Real | int | float | decimal.Decimal | str
    h3: literal.Real | int | float | decimal.Decimal | str
    r: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates rcc surface cards.
        """

        assert isinstance(self.j, literal.Integer)

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Rcc`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Rcc`
        """

        v = numpy.array((float(self.vx), float(self.vy), float(self.vz)))
        h = numpy.array((float(self.h1), float(self.h2), float(self.h3)))

        height = numpy.linalg.norm(h)
        vis = shapes.CylinderCircular(height, float(self.r))

        if height > 0:
            h = h / height
            cross = numpy.cross(numpy.array((0, 0, 1)), h)
            angle = numpy.degrees(numpy.arccos(numpy.clip(h[2], -1, 1)))

            if numpy.linalg.norm(cross) > 1e-10:
                vis = vis.rotate(cross, angle, (0, 0, 0))

        vis = vis.translate(v)

        return vis
