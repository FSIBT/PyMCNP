import typing

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Loc(Sdef):
    """
    Represents loc sdef data options.

    Attributes:
        keyword: loc sdef data option ``r'LOC'`` symbol.
        equals: loc sdef data option ``equals`` parameter.
        lat: loc sdef data option ``lat`` parameter.
        lng: loc sdef data option ``lng`` parameter.
        alt: loc sdef data option ``alt`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'LOC'] = abc.Terminal[r'LOC']('LOC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    lat: literal.Real
    lng: literal.Real
    alt: literal.Real

    def __post_init__(self) -> None:
        """
        Validates loc sdef data options.

        Raises:
            Error: Invalid value.
        """

        if not (-90 <= self.lat <= 90):
            raise abc.Error('Invalid value.', f'{self.lat=}')

        if not (-180 <= self.lng <= 180):
            raise abc.Error('Invalid value.', f'{self.lng=}')
