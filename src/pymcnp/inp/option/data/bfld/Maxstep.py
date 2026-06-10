import typing
import decimal
import dataclasses

from ..... import abc
from ..Bfld import Bfld
from .... import literal


class Maxstep(Bfld):
    """
    Represents maxstep bfld data options.

    Attributes:
        keyword: maxstep bfld data option `MAXSTEP` symbol.
        equals: maxstep bfld data option `=` symbol.
        ss: maxstep bfld data option `ss` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MAXSTEP'] | str = abc.Terminal[r'MAXSTEP']('MAXSTEP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    ss: literal.Real | int | float | decimal.Decimal | str
