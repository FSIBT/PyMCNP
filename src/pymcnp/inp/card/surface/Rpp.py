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

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    keyword: typing.Annotated[abc.Terminal, r'RPP'] | str = abc.Terminal[r'RPP']('RPP')
    xmin: literal.Real | int | float | decimal.Decimal | str
    xmax: literal.Real | int | float | decimal.Decimal | str
    ymin: literal.Real | int | float | decimal.Decimal | str
    ymax: literal.Real | int | float | decimal.Decimal | str
    zmin: literal.Real | int | float | decimal.Decimal | str
    zmax: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates rpp surface cards.
        """

        assert isinstance(self.j, literal.Integer)

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Rpp`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Rpp`
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
