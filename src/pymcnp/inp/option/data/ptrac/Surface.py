import typing


from ..... import abc
from ..Ptrac import Ptrac
from .... import literal


class Surface(Ptrac):
    """
    Represents surface ptrac data options.

    Attributes:
        keyword: surface ptrac data option ``r'SURFACE'`` symbol.
        equals: surface ptrac data option ``r'='`` symbol.
        s: surface ptrac data option ``s`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'SURFACE'] = abc.Terminal[r'SURFACE']('SURFACE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    s: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
