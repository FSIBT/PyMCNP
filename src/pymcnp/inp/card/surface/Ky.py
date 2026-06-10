import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Ky(Surface):
    """
    Represents ky surface cards.

    Attributes:
        prefix: ky surface card `prefix` parameter.
        j: ky surface card `j` parameter.
        n: ky surface card `n` parameter.
        keyword: ky surface card `KY` symbol.
        y: ky surface card `y` parameter.
        t_squared: ky surface card `t_squared` parameter.
        plus_minus_1: ky surface card `plus_minus_1` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'KY'] | str = abc.Terminal[r'KY']('KY')
    y: literal.Real | int | float | decimal.Decimal | str
    t_squared: literal.Real | int | float | decimal.Decimal | str
    plus_minus_1: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates ky surface cards.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Ky`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Ky`.
        """

        vis = shapes.ConeUnbounded(float(self.t_squared) ** (1 / 2), float(self.plus_minus_1))
        vis = vis.rotate(numpy.array((1, 0, 0)), 90, (0, 0, 0))
        vis = vis.translate(numpy.array((0, float(self.y), 0)))

        return vis
