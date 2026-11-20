import typing

from .... import abc
from ... import literal
from ..Data import Data


class Wwp(Data):
    """
    Represents wwp data cards.

    Attributes:
        keyword: wwp data card ``r'WWP'`` symbol.
        colon: wwp data card ``colon`` parameter.
        particle: wwp data card ``particle`` parameter.
        wupn: wwp data card ``wupn`` parameter.
        wsurvn: wwp data card ``wsurvn`` parameter.
        mxspln: wwp data card ``mxspln`` parameter.
        mwhere: wwp data card ``mwhere`` parameter.
        switchn: wwp data card ``switchn`` parameter.
        mtime: wwp data card ``mtime`` parameter.
        wnorm: wwp data card ``wnorm`` parameter.
        etsplt: wwp data card ``etsplt`` parameter.
        wu: wwp data card ``wu`` parameter.
        nmfp: wwp data card ``nmfp`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'WWP'] = abc.Terminal[r'WWP']('WWP')
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    wupn: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
    wsurvn: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
    mxspln: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
    mwhere: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
    switchn: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
    mtime: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
    wnorm: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
    etsplt: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
    wu: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
    nmfp: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
