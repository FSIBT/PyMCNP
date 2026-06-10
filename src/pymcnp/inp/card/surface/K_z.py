import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class K_z(Surface):
    """
    Represents k_z surface cards.

    Attributes:
        prefix: k_z surface card `prefix` parameter.
        j: k_z surface card `j` parameter.
        n: k_z surface card `n` parameter.
        keyword: k_z surface card `K/Z` symbol.
        x: k_z surface card `x` parameter.
        y: k_z surface card `y` parameter.
        z: k_z surface card `z` parameter.
        t_squared: k_z surface card `t_squared` parameter.
        plus_minus_1: k_z surface card `plus_minus_1` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'K/Z'] | str = abc.Terminal[r'K/Z']('K/Z')
    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str
    t_squared: literal.Real | int | float | decimal.Decimal | str
    plus_minus_1: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates k/z surface cards.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `K_z`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `K_z`.
        """

        vis = shapes.ConeUnbounded(float(self.t_squared) ** (1 / 2), float(self.plus_minus_1))
        vis = vis.translate(numpy.array((float(self.x), float(self.y), float(self.z))))

        return vis
