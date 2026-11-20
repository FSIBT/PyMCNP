import typing


from .... import abc
from ..Data import Data
from ... import option


class Field(Data):
    """
    Represents field data cards.

    Attributes:
        keyword: field data card ``r'FIELD'`` symbol.
        options: field data card ``options`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FIELD'] = abc.Terminal[r'FIELD']('FIELD')
    options: typing.Annotated[abc.Array, option.data.Field, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
