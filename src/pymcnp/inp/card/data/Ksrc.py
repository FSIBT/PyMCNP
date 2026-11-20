import typing


from .... import abc
from ..Data import Data
from ... import group


class Ksrc(Data):
    """
    Represents ksrc data cards.

    Attributes:
        keyword: ksrc data card ``r'KSRC'`` symbol.
        xyz: ksrc data card ``xyz`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'KSRC'] = abc.Terminal[r'KSRC']('KSRC')
    xyz: typing.Annotated[abc.Array, group.Location, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
