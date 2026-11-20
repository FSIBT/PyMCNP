import typing


from .... import abc
from ..Data import Data
from ... import option


class Sdef(Data):
    """
    Represents sdef data cards.

    Attributes:
        keyword: sdef data card ``r'SDEF'`` symbol.
        options: sdef data card ``options`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'SDEF'] = abc.Terminal[r'SDEF']('SDEF')
    options: typing.Annotated[abc.Array, option.data.Sdef, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
