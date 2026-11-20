import typing


from .... import abc
from ..Data import Data
from ... import group


class Awtab(Data):
    """
    Represents awtab data cards.

    Attributes:
        keyword: awtab data card ``r'AWTAB'`` symbol.
        z_a: awtab data card ``z_a`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'AWTAB'] = abc.Terminal[r'AWTAB']('AWTAB')
    z_a: typing.Annotated[abc.Array, group.Constituent, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
