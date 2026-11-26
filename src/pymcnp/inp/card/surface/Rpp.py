import typing


from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Rpp(Surface):
    """
    Represents rpp surface cards.

    Attributes:
        prefix: rpp surface card ``prefix`` parameter.
        j: rpp surface card ``j`` parameter.
        keyword: rpp surface card ``r'RPP'`` symbol.
        xmin: rpp surface card ``xmin`` parameter.
        xmax: rpp surface card ``xmax`` parameter.
        ymin: rpp surface card ``ymin`` parameter.
        ymax: rpp surface card ``ymax`` parameter.
        zmin: rpp surface card ``zmin`` parameter.
        zmax: rpp surface card ``zmax`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    keyword: typing.Annotated[abc.Terminal, r'RPP'] = abc.Terminal[r'RPP']('RPP')
    xmin: literal.Real
    xmax: literal.Real
    ymin: literal.Real
    ymax: literal.Real
    zmin: literal.Real
    zmax: literal.Real

    def __post_init__(self) -> None:
        """
        Validates rpp surface cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes rpp surface cards.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualizations of rpp surface cards.
        """

        vis = shapes.Parallelepiped(
            float(self.xmin),
            float(self.xmax),
            float(self.ymin),
            float(self.ymax),
            float(self.zmin),
            float(self.zmax),
        )

        return vis
