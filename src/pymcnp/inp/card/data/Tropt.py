import typing


from .... import abc
from ..Data import Data
from ... import option


class Tropt(Data):
    """
    Represents tropt data cards.

    Attributes:
        keyword: tropt data card ``r'TROPT'`` symbol.
        options: tropt data card ``options`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'TROPT'] = abc.Terminal[r'TROPT']('TROPT')
    options: typing.Annotated[abc.Array, option.data.Tropt, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
