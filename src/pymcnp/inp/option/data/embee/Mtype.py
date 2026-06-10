import typing
import dataclasses

from ..... import abc
from ..Embee import Embee


class Mtype(Embee):
    """
    Represents mtype embee data options.

    Attributes:
        keyword: mtype embee data option `MTYPE` symbol.
        equals: mtype embee data option `=` symbol.
        type: mtype embee data option `type` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MTYPE'] | str = abc.Terminal[r'MTYPE']('MTYPE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    type: typing.Annotated[abc.Terminal, r'(?:FLUX|ISOTOPIC|POPULATION|REACTION|SOURCE|TRACKS)'] | str
