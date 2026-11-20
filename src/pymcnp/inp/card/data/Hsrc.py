import typing

from .... import abc
from ... import literal
from ..Data import Data


class Hsrc(Data):
    """
    Represents hsrc data cards.

    Attributes:
        keyword: hsrc data card ``r'HSRC'`` symbol.
        nx: hsrc data card ``nx`` parameter.
        xmin: hsrc data card ``xmin`` parameter.
        xmax: hsrc data card ``xmax`` parameter.
        ny: hsrc data card ``ny`` parameter.
        ymin: hsrc data card ``ymin`` parameter.
        ymax: hsrc data card ``ymax`` parameter.
        nz: hsrc data card ``nz`` parameter.
        zmin: hsrc data card ``zmin`` parameter.
        zmax: hsrc data card ``zmax`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'HSRC'] = abc.Terminal[r'HSRC']('HSRC')
    nx: literal.Integer
    xmin: literal.Real
    xmax: literal.Real
    ny: literal.Integer
    ymin: literal.Real
    ymax: literal.Real
    nz: literal.Integer
    zmin: literal.Real
    zmax: literal.Real

    def __post_init__(self) -> None:
        """
        Validates hsrc data cards.

        Raises:
            Error: Invalid value.
        """

        if not self.nx > 0:
            raise abc.Error('Invalid value.', f'{self.nx=}')

        if not self.ny > 0:
            raise abc.Error('Invalid value.', f'{self.ny=}')

        if not self.nz > 0:
            raise abc.Error('Invalid value.', f'{self.nz=}')
