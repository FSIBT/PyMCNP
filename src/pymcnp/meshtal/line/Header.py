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

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    code: typing.Annotated[abc.Terminal, r'.{7}'] = dataclasses.field(kw_only=True)
    version: typing.Annotated[abc.Terminal, r'version .{6}'] = dataclasses.field(kw_only=True)
    ld: typing.Annotated[abc.Terminal, r'ld=.{10}'] = dataclasses.field(kw_only=True)
    probid: typing.Annotated[abc.Terminal, r'probid =.{20}'] = dataclasses.field(kw_only=True)
