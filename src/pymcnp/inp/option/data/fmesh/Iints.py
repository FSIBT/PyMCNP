import typing


from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Iints(Fmesh):
    """
    Represents iints fmesh data options.

    Attributes:
        keyword: iints fmesh data option ``r'IINTS'`` symbol.
        equals: iints fmesh data option ``r'='`` symbol.
        n: iints fmesh data option ``n`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'IINTS'] = abc.Terminal[r'IINTS']('IINTS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
