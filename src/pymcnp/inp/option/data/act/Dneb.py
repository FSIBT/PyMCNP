import typing


from ..... import abc
from ..Act import Act
from .... import group


class Dneb(Act):
    """
    Represents dneb act data options.

    Attributes:
        keyword: dneb act data option ``r'DNEB'`` symbol.
        equals: dneb act data option ``r'='`` symbol.
        value: dneb act data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DNEB'] = abc.Terminal[r'DNEB']('DNEB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Array, group.Bias, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
