import typing
import dataclasses

from ..... import abc
from ..Kpert import Kpert


class Linear(Kpert):
    """
    Represents linear kpert data options.

    Attributes:
        keyword: linear kpert data option `LINEAR` symbol.
        equals: linear kpert data option `=` symbol.
        value: linear kpert data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'LINEAR'] | str = abc.Terminal[r'LINEAR']('LINEAR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:NO|YES)'] | str
