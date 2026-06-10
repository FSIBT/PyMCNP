import typing
import dataclasses

from ..... import abc
from ..Tropt import Tropt


class Nescat(Tropt):
    """
    Represents nescat tropt data options.

    Attributes:
        keyword: nescat tropt data option `NESCAT` symbol.
        equals: nescat tropt data option `=` symbol.
        value: nescat tropt data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NESCAT'] | str = abc.Terminal[r'NESCAT']('NESCAT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:OFF|ON)'] | str
