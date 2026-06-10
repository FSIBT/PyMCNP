import re
import typing
import decimal
import dataclasses

from ... import abc
from ..Line import Line


class Space(abc.Terminal):
    _pattern = re.compile(r'(\n |)([\s\S]*)', re.IGNORECASE)


class _Nv(abc.Nonterminal):
    """
    Represents nv symbols.

    Attributes:
        n: nv symbols `n` parameter.
        v: nv symbols `v` parameter.
    """

    _space = (Space,)

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    n: typing.Annotated[abc.Terminal, r'.{12}']
    v: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'.{12}'], Space] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    @classmethod
    def from_mcnp(cls, source: str) -> tuple[typing.Self, str]:
        """
        Compiles source strings into their corresponding nonterminal symbols.

        Parameters:
            source: Source string to compile.

        Returns:
            Nonterminal symbol corresponding to `source`.

        Raises:
            Error: Invalid source string.
        """

        assert isinstance(source, str)

        spaces = {}

        n, source = abc.Terminal[r'.{12}'].from_mcnp(source)
        space, source = Space.from_mcnp(source)

        v = []
        spaces = []
        _n = int(decimal.Decimal(n).to_integral_value(rounding=None))
        if _n != 0:
            for i in range(_n - 1):
                vi, source = abc.Terminal[r'.{12}'].from_mcnp(source)
                v.append(vi)
                space, source = Space.from_mcnp(source)
                spaces.append(space)

            vi, source = abc.Terminal[r'.{12}'].from_mcnp(source)
            v.append(vi)

        return cls(n=n, v=abc.Array[abc.Terminal[r'.{12}'], Space](*v, spaces=spaces), **{'spaces': {'n': space}}), source


class V(Line):
    """
    Represents v lines.

    Attributes:
        m: v line `m` parameter.
        nv: v v line `nv` parameter.
    """

    _space = (Space,)

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    blank: typing.Annotated[abc.Terminal, r' ']
    m: typing.Annotated[abc.Terminal, r'  1\.4000E\+01']
    nv0: _Nv
    nv1: _Nv
    nv2: _Nv
    nv3: _Nv
    nv4: _Nv
    nv5: _Nv
    nv6: _Nv
    nv7: _Nv
    nv8: _Nv
    nv9: _Nv
    nv10: _Nv
    nv11: _Nv
    nv12: _Nv
    nv13: _Nv
    fill: typing.Annotated[abc.Terminal, r'(?:  0\.0000E\+00)*']
