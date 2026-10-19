import typing
import decimal
import dataclasses


from .... import abc
from .... import _show
from ... import literal
from ..Surface import Surface


class Rpp(Surface):
    """
    Represents rpp surface cards.

    Attributes:
        prefix: rpp surface card `prefix` parameter.
        j: rpp surface card `j` parameter.
        keyword: rpp surface card `RPP` symbol.
        xmin: rpp surface card `xmin` parameter.
        xmax: rpp surface card `xmax` parameter.
        ymin: rpp surface card `ymin` parameter.
        ymax: rpp surface card `ymax` parameter.
        zmin: rpp surface card `zmin` parameter.
        zmax: rpp surface card `zmax` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str = dataclasses.field(kw_only=True)
    keyword: typing.Annotated[abc.Terminal, r'RPP'] | str = abc.Terminal[r'RPP']('RPP')
    xmin: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    xmax: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    ymin: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    ymax: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    zmin: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    zmax: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)

    def __post_init__(self) -> None:
        """
        Validates rpp surface cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.j, literal.Integer)

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

        vis = shapes.Parallelipiped(
            float(self.xmin),
            float(self.xmax),
            float(self.ymin),
            float(self.ymax),
            float(self.zmin),
            float(self.zmax),
        )

        return vis
