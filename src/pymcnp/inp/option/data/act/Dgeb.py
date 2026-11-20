import typing


from ..... import abc
from ..Act import Act
from .... import group


class Dgeb(Act):
    """
    Represents dgeb act data options.

    Attributes:
        keyword: dgeb act data option ``r'DGEB'`` symbol.
        equals: dgeb act data option ``r'='`` symbol.
        value: dgeb act data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DGEB'] = abc.Terminal[r'DGEB']('DGEB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Array, group.Bias, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
