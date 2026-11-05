import typing

from ..... import abc
from ..Read import Read


class Encode(Read):
    """
    Represents encode read data options.

    Attributes:
        keyword: encode read data option ``r'ENCODE'`` symbol.
        equals: encode read data option ``r'='`` symbol.
        password: encode read data option ``password`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ENCODE'] | str = abc.Terminal[r'ENCODE']('ENCODE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    password: typing.Annotated[abc.Terminal, r'\S+'] | str
