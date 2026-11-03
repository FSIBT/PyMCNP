import typing

from ..... import abc
from ..Act import Act


class Sample(Act):
    """
    Represents sample act data options.

    Attributes:
        keyword: sample act data option `SAMPLE` symbol.
        equals: sample act data option `=` symbol.
        value: sample act data option `value` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'SAMPLE'] | str = abc.Terminal[r'SAMPLE']('SAMPLE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:CORRELATE|NONFISS_COR)'] | str
