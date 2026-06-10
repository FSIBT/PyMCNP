import typing
import dataclasses

from ... import abc
from ..Line import Line


class I(Line):
    """
    Represents i lines.

    Attributes:
        nps: i line `nps` parameter.
        event_type: i line `event_type` parameter.
        number: i line `number` parameter.
        tfc: i line `tfc` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    blank: typing.Annotated[abc.Terminal, r' ']
    nps: typing.Annotated[abc.Terminal, r'.{10}']
    event_type: typing.Annotated[abc.Terminal, r'.{10}']
    number: typing.Annotated[abc.Terminal, r'.{10}'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    tfc: typing.Annotated[abc.Terminal, r'.{13}'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
