import typing


from .... import abc
from ... import literal
from ..Data import Data


class Drxs(Data):
    """
    Represents drxs data cards.

    Attributes:
        keyword: drxs data card ``r'DRXS'`` symbol.
        z: drxs data card ``z`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DRXS'] = abc.Terminal[r'DRXS']('DRXS')
    z: typing.Annotated[abc.Array, literal.Zaid, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
