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

    keyword: typing.Annotated[abc.Terminal, r'NPS'] = abc.Terminal[r'NPS']('NPS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    npp: literal.Integer
    npsmg: literal.Integer | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
