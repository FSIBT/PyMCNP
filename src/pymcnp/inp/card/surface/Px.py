import typing
import decimal
import dataclasses


from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Px(Surface):
    """
    Represents px surface cards.

    Attributes:
        prefix: px surface card `prefix` parameter.
        j: px surface card `j` parameter.
        n: px surface card `n` parameter.
        keyword: px surface card `PX` symbol.
        d: px surface card `D` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'PX'] | str = abc.Terminal[r'PX']('PX')
    d: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates px surface cards.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Px`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Px`
        """

        vis = shapes.Plane(1, 0, 0, float(self.d))

        return vis
