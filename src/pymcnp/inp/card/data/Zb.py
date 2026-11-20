import typing


from .... import abc
from ..Data import Data


class Zb(Data):
    """
    Represents zb data cards.

    Attributes:
        keyword: zb data card ``r'ZB'`` symbol.
        x: zb data card ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ZB'] = abc.Terminal[r'ZB']('ZB')
    x: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'\S+'], None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
