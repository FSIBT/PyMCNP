import typing


from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Iints(Mesh):
    """
    Represents iints mesh data options.

    Attributes:
        keyword: iints mesh data option ``r'IINTS'`` symbol.
        equals: iints mesh data option ``r'='`` symbol.
        n: iints mesh data option ``n`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'IINTS'] = abc.Terminal[r'IINTS']('IINTS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
