import typing
import decimal
import dataclasses

from ..... import abc
from ..Pert import Pert
from .... import literal


class Method(Pert):
    """
    Represents method pert data options.

    Attributes:
        keyword: method pert data option `METHOD` symbol.
        equals: method pert data option `=` symbol.
        j: method pert data option `j` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'METHOD'] | str = abc.Terminal[r'METHOD']('METHOD')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
