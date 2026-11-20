import typing


from .... import abc
from ..Data import Data
from ... import option


class Read(Data):
    """
    Represents read data cards.

    Attributes:
        keyword: read data card ``r'READ'`` symbol.
        options: read data card ``options`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'READ'] = abc.Terminal[r'READ']('READ')
    options: typing.Annotated[abc.Array, option.data.Read, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
