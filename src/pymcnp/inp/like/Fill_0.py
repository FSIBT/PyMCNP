import re

from . import _option
from ... import types
from ... import errors


class Fill_0(_option.LikeOption):
    """
    Represents INP `fill` elements variation #0.
    """

    _KEYWORD = 'fill'

    _ATTRS = {
        'prefix': types.String,
        'i': types.Index,
        'j': types.Index,
        'k': types.Index,
        'universes': types.Tuple(types.Integer),
        'm': types.Integer,
    }

    _REGEX = re.compile(rf'\A([*])?fill (\S+:\S+) (\S+:\S+) (\S+:\S+)((?: {types.Integer._REGEX.pattern[2:-2]})+?)(?: [(]({types.Integer._REGEX.pattern[2:-2]})[)])?\Z', re.IGNORECASE)

    def __init__(
        self,
        i: str | types.Index,
        j: str | types.Index,
        k: str | types.Index,
        universes: list[str] | list[int] | list[types.Integer],
        prefix: str | types.String = None,
        m: str | int | types.Integer = None,
    ):
        """
        Initializes `Fill_0`.

        Parameters:
            prefix: Star prefix.
            i: Lattice parameter #1.
            j: Lattice parameter #2.
            k: Lattice parameter #3.
            universes: Fill universe numbers.
            m: Displacement vector origin.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.prefix: types.String = prefix
        self.i: types.Index = i
        self.j: types.Index = j
        self.k: types.Index = k
        self.universes: types.Tuple(types.Integer) = universes
        self.m: types.Integer = m

    @property
    def prefix(self) -> types.String:
        """
        Gets `prefix`.

        Returns:
            `prefix`.
        """

        return self._prefix

    @prefix.setter
    def prefix(self, prefix: str | types.String) -> None:
        """
        Sets `prefix`.

        Parameters:
            prefix: Star prefix.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if prefix is not None:
            if isinstance(prefix, types.String):
                prefix = prefix
            elif isinstance(prefix, str):
                prefix = types.String.from_mcnp(prefix)

        if prefix is not None and prefix.value.lower() not in {'*'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, prefix)

        self._prefix: types.String = prefix

    @property
    def i(self) -> types.Index:
        """
        Gets `i`.

        Returns:
            `i`.
        """

        return self._i

    @i.setter
    def i(self, i: str | types.Index) -> None:
        """
        Sets `i`.

        Parameters:
            i: Lattice parameter #1.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if i is not None:
            if isinstance(i, types.Index):
                i = i
            elif isinstance(i, str):
                i = types.Index.from_mcnp(i)

        if i is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i)

        self._i: types.Index = i

    @property
    def j(self) -> types.Index:
        """
        Gets `j`.

        Returns:
            `j`.
        """

        return self._j

    @j.setter
    def j(self, j: str | types.Index) -> None:
        """
        Sets `j`.

        Parameters:
            j: Lattice parameter #2.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if j is not None:
            if isinstance(j, types.Index):
                j = j
            elif isinstance(j, str):
                j = types.Index.from_mcnp(j)

        if j is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, j)

        self._j: types.Index = j

    @property
    def k(self) -> types.Index:
        """
        Gets `k`.

        Returns:
            `k`.
        """

        return self._k

    @k.setter
    def k(self, k: str | types.Index) -> None:
        """
        Sets `k`.

        Parameters:
            k: Lattice parameter #3.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if k is not None:
            if isinstance(k, types.Index):
                k = k
            elif isinstance(k, str):
                k = types.Index.from_mcnp(k)

        if k is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, k)

        self._k: types.Index = k

    @property
    def universes(self) -> types.Tuple(types.Integer):
        """
        Gets `universes`.

        Returns:
            `universes`.
        """

        return self._universes

    @universes.setter
    def universes(self, universes: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets `universes`.

        Parameters:
            universes: Fill universe numbers.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if universes is not None:
            array = []
            for item in universes:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))

            universes = types.Tuple(types.Integer)(array)

        if universes is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, universes)

        self._universes: types.Tuple(types.Integer) = universes

    @property
    def m(self) -> types.Integer:
        """
        Gets `m`.

        Returns:
            `m`.
        """

        return self._m

    @m.setter
    def m(self, m: str | int | types.Integer) -> None:
        """
        Sets `m`.

        Parameters:
            m: Displacement vector origin.

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

        self._m: types.Integer = m
