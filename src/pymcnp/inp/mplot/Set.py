import re

from . import _option
from ... import types
from ... import errors


class Set(_option.MplotOption):
    """
    Represents INP `set` elements.
    """

    _KEYWORD = 'set'

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
        rf'\Aset( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        f: str | int | types.Integer,
        d: str | int | types.Integer,
        u: str | int | types.Integer,
        s: str | int | types.Integer,
        m: str | int | types.Integer,
        c: str | int | types.Integer,
        e: str | int | types.Integer,
        t: str | int | types.Integer,
    ):
        """
        Initializes `Set`.

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

        self.f: types.Integer = f
        self.d: types.Integer = d
        self.u: types.Integer = u
        self.s: types.Integer = s
        self.m: types.Integer = m
        self.c: types.Integer = c
        self.e: types.Integer = e
        self.t: types.Integer = t

    @property
    def f(self) -> types.Integer:
        """
        F bin number

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._f

    @f.setter
    def f(self, f: str | int | types.Integer) -> None:
        """
        Sets `f`.

        Parameters:
            f: F bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if f is not None:
            if isinstance(f, types.Integer):
                f = f
            elif isinstance(f, int):
                f = types.Integer(f)
            elif isinstance(f, str):
                f = types.Integer.from_mcnp(f)

        if f is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, f)

        self._f: types.Integer = f

    @property
    def d(self) -> types.Integer:
        """
        D bin number

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._d

    @d.setter
    def d(self, d: str | int | types.Integer) -> None:
        """
        Sets `d`.

        Parameters:
            d: D bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if d is not None:
            if isinstance(d, types.Integer):
                d = d
            elif isinstance(d, int):
                d = types.Integer(d)
            elif isinstance(d, str):
                d = types.Integer.from_mcnp(d)

        if d is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, d)

        self._d: types.Integer = d

    @property
    def u(self) -> types.Integer:
        """
        U bin number

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._u

    @u.setter
    def u(self, u: str | int | types.Integer) -> None:
        """
        Sets `u`.

        Parameters:
            u: U bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if u is not None:
            if isinstance(u, types.Integer):
                u = u
            elif isinstance(u, int):
                u = types.Integer(u)
            elif isinstance(u, str):
                u = types.Integer.from_mcnp(u)

        if u is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, u)

        self._u: types.Integer = u

    @property
    def s(self) -> types.Integer:
        """
        S bin number

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._s

    @s.setter
    def s(self, s: str | int | types.Integer) -> None:
        """
        Sets `s`.

        Parameters:
            s: S bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if s is not None:
            if isinstance(s, types.Integer):
                s = s
            elif isinstance(s, int):
                s = types.Integer(s)
            elif isinstance(s, str):
                s = types.Integer.from_mcnp(s)

        if s is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, s)

        self._s: types.Integer = s

    @property
    def m(self) -> types.Integer:
        """
        M bin number

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._m

    @m.setter
    def m(self, m: str | int | types.Integer) -> None:
        """
        Sets `m`.

        Parameters:
            m: M bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if m is not None:
            if isinstance(m, types.Integer):
                m = m
            elif isinstance(m, int):
                m = types.Integer(m)
            elif isinstance(m, str):
                m = types.Integer.from_mcnp(m)

        if m is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, m)

        self._m: types.Integer = m

    @property
    def c(self) -> types.Integer:
        """
        C bin number

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._c

    @c.setter
    def c(self, c: str | int | types.Integer) -> None:
        """
        Sets `c`.

        Parameters:
            c: C bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if c is not None:
            if isinstance(c, types.Integer):
                c = c
            elif isinstance(c, int):
                c = types.Integer(c)
            elif isinstance(c, str):
                c = types.Integer.from_mcnp(c)

        if c is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, c)

        self._c: types.Integer = c

    @property
    def e(self) -> types.Integer:
        """
        E bin number

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._e

    @e.setter
    def e(self, e: str | int | types.Integer) -> None:
        """
        Sets `e`.

        Parameters:
            e: E bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if e is not None:
            if isinstance(e, types.Integer):
                e = e
            elif isinstance(e, int):
                e = types.Integer(e)
            elif isinstance(e, str):
                e = types.Integer.from_mcnp(e)

        if e is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, e)

        self._e: types.Integer = e

    @property
    def t(self) -> types.Integer:
        """
        T bin number

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._t

    @t.setter
    def t(self, t: str | int | types.Integer) -> None:
        """
        Sets `t`.

        Parameters:
            t: T bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if t is not None:
            if isinstance(t, types.Integer):
                t = t
            elif isinstance(t, int):
                t = types.Integer(t)
            elif isinstance(t, str):
                t = types.Integer.from_mcnp(t)

        if t is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, t)

        self._t: types.Integer = t
