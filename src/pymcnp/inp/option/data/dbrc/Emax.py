import typing
import decimal
import dataclasses

from ..... import abc
from ..Dbrc import Dbrc
from .... import literal


class Emax(Dbrc):
    """
    Represents emax dbrc data options.

    Attributes:
        keyword: emax dbrc data option `EMAX` symbol.
        equals: emax dbrc data option `=` symbol.
        eee: emax dbrc data option `eee` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'EMAX'] | str = abc.Terminal[r'EMAX']('EMAX')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    eee: literal.Real | int | float | decimal.Decimal | str
