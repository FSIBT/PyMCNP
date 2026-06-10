import typing
import decimal
import dataclasses

from ..... import abc
from ..Stop import Stop
from .... import literal


class F(Stop):
    """
    Represents f stop data options.

    Attributes:
        keyword: f stop data option `F` symbol.
        suffix: f stop data option `k` parameter.
        equals: f stop data option `=` symbol.
        e: f stop data option `e` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'F'] | str = abc.Terminal[r'F']('F')
    suffix: literal.Integer | int | str
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    e: literal.Real | int | float | decimal.Decimal | str
