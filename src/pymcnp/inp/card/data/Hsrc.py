import typing
import decimal
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Hsrc(Data):
    """
    Represents hsrc data cards.

    Attributes:
        keyword: hsrc data card `HSRC` symbol.
        nx: hsrc data card `nx` parameter.
        xmin: hsrc data card `xmin` parameter.
        xmax: hsrc data card `xmax` parameter.
        ny: hsrc data card `ny` parameter.
        ymin: hsrc data card `ymin` parameter.
        ymax: hsrc data card `ymax` parameter.
        nz: hsrc data card `nz` parameter.
        zmin: hsrc data card `zmin` parameter.
        zmax: hsrc data card `zmax` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'HSRC'] | str = abc.Terminal[r'HSRC']('HSRC')
    nx: literal.Integer | int | str
    xmin: literal.Real | int | float | decimal.Decimal | str
    xmax: literal.Real | int | float | decimal.Decimal | str
    ny: literal.Integer | int | str
    ymin: literal.Real | int | float | decimal.Decimal | str
    ymax: literal.Real | int | float | decimal.Decimal | str
    nz: literal.Integer | int | str
    zmin: literal.Real | int | float | decimal.Decimal | str
    zmax: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates hsrc data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.nx, literal.Integer)
        assert isinstance(self.ny, literal.Integer)
        assert isinstance(self.nz, literal.Integer)

        if not self.nx > 0:
            raise abc.Error('Invalid value.', f'{self.nx=}')

        if not self.ny > 0:
            raise abc.Error('Invalid value.', f'{self.ny=}')

        if not self.nz > 0:
            raise abc.Error('Invalid value.', f'{self.nz=}')
