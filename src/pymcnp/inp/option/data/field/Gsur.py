import typing


from ..... import abc
from .... import literal
from ..Field import Field


class Gsur(Field):
    """
    Represents gsur field data options.

    Attributes:
        keyword: gsur field data option ``r'GSUR'`` symbol.
        equals: gsur field data option ``r'='`` symbol.
        s: gsur field data option ``s`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'GSUR'] = abc.Terminal[r'GSUR']('GSUR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    s: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
