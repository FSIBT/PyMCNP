import typing
import decimal
import dataclasses

import numpy

from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Sz(Surface):
    """
    Represents sz surface cards.

    Attributes:
        prefix: sz surface card `prefix` parameter.
        j: sz surface card `j` parameter.
        n: sz surface card `n` parameter.
        keyword: sz surface card `SZ` symbol.
        z: sz surface card `z` parameter.
        r: sz surface card `R` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'SZ'] | str = abc.Terminal[r'SZ']('SZ')
    z: literal.Real | int | float | decimal.Decimal | str
    r: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates sz surface cards.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Sz`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Sz`
        """

        vis = shapes.Sphere(float(self.r))
        vis = vis.translate(numpy.array((0, 0, float(self.z))))

        return vis
