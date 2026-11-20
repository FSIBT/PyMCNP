import typing


from .... import abc
from ..Data import Data


class Za(Data):
    """
    Represents za data cards.

    Attributes:
        keyword: za data card ``r'ZA'`` symbol.
        x: za data card ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ZA'] = abc.Terminal[r'ZA']('ZA')
    x: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'\S+'], None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
