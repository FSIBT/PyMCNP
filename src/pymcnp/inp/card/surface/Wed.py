import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Wed(Surface):
    """
    Represents wed surface cards.

    Attributes:
        prefix: wed surface card `prefix` parameter.
        j: wed surface card `j` parameter.
        keyword: wed surface card `WED` symbol.
        vx: wed surface card `vx` parameter.
        vy: wed surface card `vy` parameter.
        vz: wed surface card `vz` parameter.
        v1x: wed surface card `v1x` parameter.
        v1y: wed surface card `v1y` parameter.
        v1z: wed surface card `v1z` parameter.
        v2x: wed surface card `v2x` parameter.
        v2y: wed surface card `v2y` parameter.
        v2z: wed surface card `v2z` parameter.
        v3x: wed surface card `v3x` parameter.
        v3y: wed surface card `v3y` parameter.
        v3z: wed surface card `v3z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    keyword: typing.Annotated[abc.Terminal, r'WED'] | str = abc.Terminal[r'WED']('WED')
    vx: literal.Real | int | float | decimal.Decimal | str
    vy: literal.Real | int | float | decimal.Decimal | str
    vz: literal.Real | int | float | decimal.Decimal | str
    v1x: literal.Real | int | float | decimal.Decimal | str
    v1y: literal.Real | int | float | decimal.Decimal | str
    v1z: literal.Real | int | float | decimal.Decimal | str
    v2x: literal.Real | int | float | decimal.Decimal | str
    v2y: literal.Real | int | float | decimal.Decimal | str
    v2z: literal.Real | int | float | decimal.Decimal | str
    v3x: literal.Real | int | float | decimal.Decimal | str
    v3y: literal.Real | int | float | decimal.Decimal | str
    v3z: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates web surface cards.
        """

        assert isinstance(self.j, literal.Integer)

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Wed`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Wed`
        """

        v = numpy.array((float(self.vx), float(self.vy), float(self.vz)))
        v1 = numpy.array((float(self.v1x), float(self.v1y), float(self.v1z)))
        v2 = numpy.array((float(self.v2x), float(self.v2y), float(self.v2z)))
        v3 = numpy.array((float(self.v3x), float(self.v3y), float(self.v3z)))

        cross = numpy.cross(numpy.array((1, 0, 0)), v1)
        angle = numpy.degrees(numpy.arccos(v1[0] / numpy.linalg.norm(v1)))

        vis = shapes.Wedge(numpy.linalg.norm(v1), numpy.linalg.norm(v2), numpy.linalg.norm(v3))
        vis = vis.rotate(cross, angle, (0, 0, 0))
        vis = vis.translate(v)

        return vis
