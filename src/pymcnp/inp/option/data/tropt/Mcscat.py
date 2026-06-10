import typing
import dataclasses

from ..... import abc
from ..Tropt import Tropt


class Mcscat(Tropt):
    """
    Represents mcscat tropt data options.

    Attributes:
        keyword: mcscat tropt data option `MCSCAT` symbol.
        equals: mcscat tropt data option `=` symbol.
        value: mcscat tropt data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MCSCAT'] | str = abc.Terminal[r'MCSCAT']('MCSCAT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:OFF|FNALL|GAUSSIAN|FNAL2)'] | str
