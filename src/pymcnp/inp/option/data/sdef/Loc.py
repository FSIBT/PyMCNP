import typing
import decimal
import dataclasses

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Loc(Sdef):
    """
    Represents loc sdef data options.

    Attributes:
        keyword: loc sdef data option `LOC` symbol.
        equals: loc sdef data option `equals` parameter.
        lat: loc sdef data option `lat` parameter.
        lng: loc sdef data option `lng` parameter.
        alt: loc sdef data option `alt` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'LOC'] | str = abc.Terminal[r'LOC']('LOC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    lat: literal.Real | int | float | decimal.Decimal | str
    lng: literal.Real | int | float | decimal.Decimal | str
    alt: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates loc sdef data options.
        """

        assert isinstance(self.lat, literal.Real)
        assert isinstance(self.lng, literal.Real)

        if not (-90 <= self.lat <= 90):
            raise abc.Error('Invalid value.', f'{self.lat=}')

        if not (-180 <= self.lng <= 180):
            raise abc.Error('Invalid value.', f'{self.lng=}')
