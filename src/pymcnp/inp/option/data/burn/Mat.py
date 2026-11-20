import typing


from ..... import abc
from .... import literal
from ..Burn import Burn


class Mat(Burn):
    """
    Represents mat burn data options.

    Attributes:
        keyword: mat burn data option ``r'MAT'`` symbol.
        equals: mat burn data option ``r'='`` symbol.
        m: mat burn data option ``m`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MAT'] = abc.Terminal[r'MAT']('MAT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    m: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
