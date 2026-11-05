import typing

from ..... import abc
from ..Stop import Stop
from .... import literal


class Nps(Stop):
    """
    Represents nps stop data options.

    Attributes:
        keyword: nps stop data option ``r'NPS'`` symbol.
        equals: nps stop data option ``r'='`` symbol.
        npp: nps stop data option ``npp`` parameter.
        npsmg: nps stop data option ``npsmg`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'NPS'] | str = abc.Terminal[r'NPS']('NPS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    npp: literal.Integer | int | str
    npsmg: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
