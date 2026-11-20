import typing


from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Eints(Fmesh):
    """
    Represents eints fmesh data options.

    Attributes:
        keyword: eints fmesh data option ``r'EINTS'`` symbol.
        equals: eints fmesh data option ``r'='`` symbol.
        n: eints fmesh data option ``n`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EINTS'] = abc.Terminal[r'EINTS']('EINTS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
