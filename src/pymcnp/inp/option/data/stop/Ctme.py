import typing
import decimal
import dataclasses

from ..... import abc
from ..Stop import Stop
from .... import literal


class Ctme(Stop):
    """
    Represents ctme stop data options.

    Attributes:
        keyword: ctme stop data option `CTME` symbol.
        equals: ctme stop data option `=` symbol.
        tme: ctme stop data option `tme` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'CTME'] | str = abc.Terminal[r'CTME']('CTME')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    tme: literal.Real | int | float | decimal.Decimal | str
