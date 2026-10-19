import re
import typing
import decimal
import dataclasses

from ... import abc
from ..Line import Line


class Space(abc.Terminal):
    _pattern = re.compile(r'(\n |)([\s\S]*)', re.IGNORECASE)


@typing.dataclass_transform(kw_only_default=True)
class _Nv(abc.Nonterminal):
    """
    Represents nv symbols.

    Attributes:
        n: nv symbols `n` parameter.
        v: nv symbols `v` parameter.
    """

    _space = (Space,)

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    n: typing.Annotated[abc.Terminal, r'.{12}'] = dataclasses.field(kw_only=True)
    v: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'.{12}'], Space] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    @classmethod
    def _from(cls, source: str, pos: int) -> tuple[typing.Self, int]:
        term = abc.Terminal[r'.{12}']

        n, pos = term._from(source, pos)
        space, pos = Space._from(source, pos)

        v = []
        spaces = []
        _n = int(decimal.Decimal(n).to_integral_value(rounding=None))
        if _n != 0:
            for i in range(_n - 1):
                vi, pos = term._from(source, pos)
                v.append(vi)
                space, pos = Space._from(source, pos)
                spaces.append(space)

            vi, pos = term._from(source, pos)
            v.append(vi)

        return cls(n=n, v=abc.Array[abc.Terminal[r'.{12}'], Space](*v, spaces=spaces), **{'spaces': {'n': space}}), pos


class V(Line):
    """
    Represents v lines.

    Attributes:
        m: v line `m` parameter.
        nv: v v line `nv` parameter.
    """

    _space = (Space,)

    blank: typing.Annotated[abc.Terminal, r' '] = dataclasses.field(kw_only=True)
    m: typing.Annotated[abc.Terminal, r'  1\.4000E\+01'] = dataclasses.field(kw_only=True)
    nv0: _Nv = dataclasses.field(kw_only=True)
    nv1: _Nv = dataclasses.field(kw_only=True)
    nv2: _Nv = dataclasses.field(kw_only=True)
    nv3: _Nv = dataclasses.field(kw_only=True)
    nv4: _Nv = dataclasses.field(kw_only=True)
    nv5: _Nv = dataclasses.field(kw_only=True)
    nv6: _Nv = dataclasses.field(kw_only=True)
    nv7: _Nv = dataclasses.field(kw_only=True)
    nv8: _Nv = dataclasses.field(kw_only=True)
    nv9: _Nv = dataclasses.field(kw_only=True)
    nv10: _Nv = dataclasses.field(kw_only=True)
    nv11: _Nv = dataclasses.field(kw_only=True)
    nv12: _Nv = dataclasses.field(kw_only=True)
    nv13: _Nv = dataclasses.field(kw_only=True)
    fill: typing.Annotated[abc.Terminal, r'(?:  0\.0000E\+00)*'] = dataclasses.field(kw_only=True)

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)
