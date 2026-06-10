import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Ty(Surface):
    """
    Represents ty surface cards.

    Attributes:
        prefix: ty surface card `prefix` parameter.
        j: ty surface card `j` parameter.
        n: ty surface card `n` parameter.
        keyword: ty surface card `TY` symbol.
        x: ty surface card `x` parameter.
        y: ty surface card `y` parameter.
        z: ty surface card `z` parameter.
        a: ty surface card `A` parameter.
        b: ty surface card `B` parameter.
        c: ty surface card `C` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'TY'] | str = abc.Terminal[r'TY']('TY')
    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str
    a: literal.Real | int | float | decimal.Decimal | str
    b: literal.Real | int | float | decimal.Decimal | str
    c: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates ty surface cards.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Ty`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Ty`
        """

        vis = shapes.Torus(float(self.b), float(self.c), float(self.a))
        vis = vis.rotate(numpy.array((1, 0, 0)), 90, (0, 0, 0))
        vis = vis.translate(numpy.array((float(self.x), float(self.y), float(self.z))))

        return vis
