import typing
import dataclasses

from ..... import abc
from ..Fmesh import Fmesh


class Tally(Fmesh):
    """
    Represents tally fmesh data options.

    Attributes:
        keyword: tally fmesh data option `TALLY` symbol.
        equals: tally fmesh data option `=` symbol.
        value: tally fmesh data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TALLY'] | str = abc.Terminal[r'TALLY']('TALLY')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:HIST|FAST_HIST|BATCH|RMA_BATCH)'] | str
