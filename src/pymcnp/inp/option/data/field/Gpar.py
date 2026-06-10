import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..Field import Field


class Gpar(Field):
    """
    Represents gpar field data options.

    Attributes:
        keyword: gpar field data option `GPAR` symbol.
        equals: gpar field data option `=` symbol.
        p: gpar field data option `p` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'GPAR'] | str = abc.Terminal[r'GPAR']('GPAR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    p: literal.Real | int | float | decimal.Decimal | str
