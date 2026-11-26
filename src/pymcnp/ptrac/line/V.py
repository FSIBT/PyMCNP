import re
import typing
import decimal
import dataclasses

from ... import abc
from ..Line import Line


class Space(abc.Terminal):
    _pattern = re.compile(r'(\n |)', re.IGNORECASE)


_TWELVE = abc.Terminal[r'.{12}']
_VALUES = abc.Array[_TWELVE, Space]


class _Nv(abc.Nonterminal):
    """
    Represents nv symbols.

    Attributes:
        n: nv symbols ``n`` parameter.
        v: nv symbols ``v`` parameter.
    """

    _space = (Space,)

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    n: typing.Annotated[abc.Terminal, r'.{12}']
    v: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'.{12}'], Space] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    @classmethod
    def _from_mcnp_at(cls, source: str, pos: int) -> tuple[typing.Self, int]:
        """
        Compiles source strings at positions into their corresponding nonterminal symbols.

        Parameters:
            source: Source string to compile.
            pos: Position in ``source`` to compile at.

        Returns:
            Nonterminal symbol corresponding to ``source`` at ``pos`` and the position where it ends.

        Raises:
            Error: Invalid source string.
        """

        n, pos = _TWELVE._from_mcnp_at(source, pos)
        space, pos = Space._from_mcnp_at(source, pos)

        v = []
        spaces = []
        _n = int(decimal.Decimal(n).to_integral_value(rounding=None))
        if _n != 0:
            for i in range(_n - 1):
                vi, pos = _TWELVE._from_mcnp_at(source, pos)
                v.append(vi)
                space, pos = Space._from_mcnp_at(source, pos)
                spaces.append(space)

            vi, pos = _TWELVE._from_mcnp_at(source, pos)
            v.append(vi)

        return cls(
            n=n,
            v=_VALUES(*v, spaces=spaces),
            spaces={'n': space},
        ), pos


class V(Line):
    """
    Represents v lines.

    Attributes:
        m: v line ``m`` parameter.
        nv: v v line ``nv`` parameter.
    """

    _space = (Space,)

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
