import typing
import dataclasses

from ... import abc
from ..Line import Line


class Header(Line):
    """
    Represents header lines.

    Attributes:
        code: header line `code` parameter.
        version: header line `version` parameter.
        ld: header line `ld` parameter.
        probid: header line `probid` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    code: typing.Annotated[abc.Terminal, r'.{7}']
    version: typing.Annotated[abc.Terminal, r'version .{6}']
    ld: typing.Annotated[abc.Terminal, r'ld=.{10}']
    probid: typing.Annotated[abc.Terminal, r'probid =.{20}']
