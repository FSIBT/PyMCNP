import typing

from ..... import abc
from ..Ptrac import Ptrac
from .... import literal


class Max(Ptrac):
    """
    Represents max ptrac data options.

    Attributes:
        keyword: max ptrac data option `MAX` symbol.
        equals: max ptrac data option `=` symbol.
        value: max ptrac data option `value` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MAX'] | str = abc.Terminal[r'MAX']('MAX')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
