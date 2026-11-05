import typing

import collections

from .... import abc
from ..Data import Data
from ... import option


class Mesh(Data):
    """
    Represents mesh data cards.

    Attributes:
        keyword: mesh data card ``r'MESH'`` symbol.
        options: mesh data card ``options`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MESH'] | str = abc.Terminal[r'MESH']('MESH')
    options: typing.Annotated[abc.Array, option.data.Mesh, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Mesh | str] | str = abc.Terminal[r'']('')
