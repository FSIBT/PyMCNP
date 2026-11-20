import typing


from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Px(Surface):
    """
    Represents px surface cards.

    Attributes:
        prefix: px surface card ``prefix`` parameter.
        j: px surface card ``j`` parameter.
        n: px surface card ``n`` parameter.
        keyword: px surface card ``r'PX'`` symbol.
        d: px surface card ``D`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'PX'] = abc.Terminal[r'PX']('PX')
    d: literal.Real

    def __post_init__(self) -> None:
        """
        Validates px surface cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes px surface cards.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of px surface cards.
        """

        vis = shapes.Plane(1, 0, 0, float(self.d))

        return vis
