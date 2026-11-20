import typing


from .... import abc
from ..Data import Data
from ... import option


class Act(Data):
    """
    Represents act data cards.

    Attributes:
        keyword: act data card ``r'ACT'`` symbol.
        options: act data card ``options`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ACT'] = abc.Terminal[r'ACT']('ACT')
    options: typing.Annotated[abc.Array, option.data.Act, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
