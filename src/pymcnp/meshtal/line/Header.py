import typing

from ... import abc
from ..Line import Line


class Header(Line):
    """
    Represents header lines.

    Attributes:
        code: header line ``code`` parameter.
        version_preamble: header line ``r'version '`` symbol.
        version: header line ``version`` parameter.
        ld_preamble: header line ``r'ld='`` symbol.
        ld: header line ``ld`` parameter.
        probid_preamble: header line ``r'probid  ='`` symbol.
        probid: header line ``probid`` parameter.
    """

    code: typing.Annotated[abc.Terminal, r'.{7}']
    version_preamble: typing.Annotated[abc.Terminal, r'version ']
    version: typing.Annotated[abc.Terminal, r'.{6}']
    ld_preamble: typing.Annotated[abc.Terminal, r'ld=']
    ld: typing.Annotated[abc.Terminal, r'.{10}']
    probid_preamble: typing.Annotated[abc.Terminal, r'probid  =']
    probid: typing.Annotated[abc.Terminal, r'.{20}']
