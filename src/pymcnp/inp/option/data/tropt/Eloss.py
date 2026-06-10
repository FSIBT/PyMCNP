import typing
import dataclasses

from ..... import abc
from ..Tropt import Tropt


class Eloss(Tropt):
    """
    Represents eloss tropt data options.

    Attributes:
        keyword: eloss tropt data option `ELOSS` symbol.
        equals: eloss tropt data option `=` symbol.
        value: eloss tropt data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ELOSS'] | str = abc.Terminal[r'ELOSS']('ELOSS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:OFF|STRAG1|CSDA)'] | str
