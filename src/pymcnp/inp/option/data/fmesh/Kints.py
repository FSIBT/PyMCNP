import typing


from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Kints(Fmesh):
    """
    Represents kints fmesh data options.

    Attributes:
        keyword: kints fmesh data option ``r'KINTS'`` symbol.
        equals: kints fmesh data option ``r'='`` symbol.
        n: kints fmesh data option ``n`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'KINTS'] = abc.Terminal[r'KINTS']('KINTS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
