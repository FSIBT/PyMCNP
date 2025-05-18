import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Set(MplotOption):
    """
    Represents INP set elements.

    Attributes:
        f: F bin number.
        d: D bin number.
        u: U bin number.
        s: S bin number.
        m: M bin number.
        c: C bin number.
        e: E bin number.
        t: T bin number.
    """

    _ATTRS = {
        'f': types.Integer,
        'd': types.Integer,
        'u': types.Integer,
        's': types.Integer,
        'm': types.Integer,
        'c': types.Integer,
        'e': types.Integer,
        't': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Aset( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        f: types.Integer,
        d: types.Integer,
        u: types.Integer,
        s: types.Integer,
        m: types.Integer,
        c: types.Integer,
        e: types.Integer,
        t: types.Integer,
    ):
        """
        Initializes ``Set``.

        Parameters:
            f: F bin number.
            d: D bin number.
            u: U bin number.
            s: S bin number.
            m: M bin number.
            c: C bin number.
            e: E bin number.
            t: T bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if f is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, f)
        if d is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, d)
        if u is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, u)
        if s is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, s)
        if m is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, m)
        if c is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, c)
        if e is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, e)
        if t is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, t)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                f,
                d,
                u,
                s,
                m,
                c,
                e,
                t,
            ]
        )

        self.f: typing.Final[types.Integer] = f
        self.d: typing.Final[types.Integer] = d
        self.u: typing.Final[types.Integer] = u
        self.s: typing.Final[types.Integer] = s
        self.m: typing.Final[types.Integer] = m
        self.c: typing.Final[types.Integer] = c
        self.e: typing.Final[types.Integer] = e
        self.t: typing.Final[types.Integer] = t


@dataclasses.dataclass
class SetBuilder:
    """
    Builds ``Set``.

    Attributes:
        f: F bin number.
        d: D bin number.
        u: U bin number.
        s: S bin number.
        m: M bin number.
        c: C bin number.
        e: E bin number.
        t: T bin number.
    """

    f: str | int | types.Integer
    d: str | int | types.Integer
    u: str | int | types.Integer
    s: str | int | types.Integer
    m: str | int | types.Integer
    c: str | int | types.Integer
    e: str | int | types.Integer
    t: str | int | types.Integer

    def build(self):
        """
        Builds ``SetBuilder`` into ``Set``.

        Returns:
            ``Set`` for ``SetBuilder``.
        """

        f = self.f
        if isinstance(self.f, types.Integer):
            f = self.f
        elif isinstance(self.f, int):
            f = types.Integer(self.f)
        elif isinstance(self.f, str):
            f = types.Integer.from_mcnp(self.f)

        d = self.d
        if isinstance(self.d, types.Integer):
            d = self.d
        elif isinstance(self.d, int):
            d = types.Integer(self.d)
        elif isinstance(self.d, str):
            d = types.Integer.from_mcnp(self.d)

        u = self.u
        if isinstance(self.u, types.Integer):
            u = self.u
        elif isinstance(self.u, int):
            u = types.Integer(self.u)
        elif isinstance(self.u, str):
            u = types.Integer.from_mcnp(self.u)

        s = self.s
        if isinstance(self.s, types.Integer):
            s = self.s
        elif isinstance(self.s, int):
            s = types.Integer(self.s)
        elif isinstance(self.s, str):
            s = types.Integer.from_mcnp(self.s)

        m = self.m
        if isinstance(self.m, types.Integer):
            m = self.m
        elif isinstance(self.m, int):
            m = types.Integer(self.m)
        elif isinstance(self.m, str):
            m = types.Integer.from_mcnp(self.m)

        c = self.c
        if isinstance(self.c, types.Integer):
            c = self.c
        elif isinstance(self.c, int):
            c = types.Integer(self.c)
        elif isinstance(self.c, str):
            c = types.Integer.from_mcnp(self.c)

        e = self.e
        if isinstance(self.e, types.Integer):
            e = self.e
        elif isinstance(self.e, int):
            e = types.Integer(self.e)
        elif isinstance(self.e, str):
            e = types.Integer.from_mcnp(self.e)

        t = self.t
        if isinstance(self.t, types.Integer):
            t = self.t
        elif isinstance(self.t, int):
            t = types.Integer(self.t)
        elif isinstance(self.t, str):
            t = types.Integer.from_mcnp(self.t)

        return Set(
            f=f,
            d=d,
            u=u,
            s=s,
            m=m,
            c=c,
            e=e,
            t=t,
        )
