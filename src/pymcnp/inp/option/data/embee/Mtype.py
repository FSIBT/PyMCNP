import typing

from ..... import abc
from ..Embee import Embee


class Mtype(Embee):
    """
    Represents mtype embee data options.

    Attributes:
        keyword: mtype embee data option ``r'MTYPE'`` symbol.
        equals: mtype embee data option ``r'='`` symbol.
        type: mtype embee data option ``type`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MTYPE'] | str = abc.Terminal[r'MTYPE']('MTYPE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    type: typing.Annotated[abc.Terminal, r'(?:FLUX|ISOTOPIC|POPULATION|REACTION|SOURCE|TRACKS)'] | str
