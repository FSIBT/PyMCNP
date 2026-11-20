import typing


from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Kints(Mesh):
    """
    Represents kints mesh data options.

    Attributes:
        keyword: kints mesh data option ``r'KINTS'`` symbol.
        equals: kints mesh data option ``r'='`` symbol.
        n: kints mesh data option ``n`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'KINTS'] = abc.Terminal[r'KINTS']('KINTS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
