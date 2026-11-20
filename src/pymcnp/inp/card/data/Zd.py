import typing


from .... import abc
from ..Data import Data


class Zd(Data):
    """
    Represents zd data cards.

    Attributes:
        keyword: zd data card ``r'ZD'`` symbol.
        x: zd data card ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ZD'] = abc.Terminal[r'ZD']('ZD')
    x: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'\S+'], None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
