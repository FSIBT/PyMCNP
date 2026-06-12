import typing
import decimal
import dataclasses


from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Pz(Surface):
    """
    Represents pz surface cards.

    Attributes:
        prefix: pz surface card `prefix` parameter.
        j: pz surface card `j` parameter.
        n: pz surface card `n` parameter.
        keyword: pz surface card `PZ` symbol.
        d: pz surface card `D` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'PZ'] | str = abc.Terminal[r'PZ']('PZ')
    d: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates pz surface cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes pz surface cards.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of pz surface cards.
        """

        vis = shapes.Plane(0, 0, 1, float(self.d))

        return vis
