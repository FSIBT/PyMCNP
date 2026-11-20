import typing

from ..... import abc
from ..Act import Act


class Sample(Act):
    """
    Represents sample act data options.

    Attributes:
        keyword: sample act data option ``r'SAMPLE'`` symbol.
        equals: sample act data option ``r'='`` symbol.
        value: sample act data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'SAMPLE'] = abc.Terminal[r'SAMPLE']('SAMPLE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:CORRELATE|NONFISS_COR)']
