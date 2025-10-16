import re

from . import _card
from .. import types
from .. import errors


class C(_card.Card):
    """
    Represents INP c cards.
    """

    _KEYWORD = 'c'

    _ATTRS = {
        'prefix': types.String,
        'suffix': types.Integer,
        'bounds': types.Tuple(types.Real),
        't': types.String,
        'c': types.String,
    }

    _REGEX = re.compile(rf'\A([*]?)c(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)

    def __init__(
        self, suffix: str | int | types.Integer, bounds: list[str] | list[float] | list[types.Real], prefix: str | types.String = None, t: str | types.String = None, c: str | types.String = None
    ):
        """
        Initializes `C`.

        Parameters:
            prefix: Star prefix.
            suffix: Data card option suffix.
            bounds: Upper cosine bounds for bin.
            t: Notation to provide totals.
            c: Notation to make bin values cumulative.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.prefix: types.String = prefix
        self.suffix: types.Integer = suffix
        self.bounds: types.Tuple(types.Real) = bounds
        self.t: types.String = t
        self.c: types.String = c

    @property
    def prefix(self) -> types.String:
        """
        Star prefix

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._prefix

    @prefix.setter
    def prefix(self, prefix: str | types.String) -> None:
        """
        Sets `prefix`.

        Parameters:
            prefix: Star prefix.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if prefix is not None:
            if isinstance(prefix, types.String):
                prefix = prefix
            elif isinstance(prefix, str):
                prefix = types.String.from_mcnp(prefix)

        if prefix is not None and prefix.value.lower() not in {'*', '+'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, prefix)

        self._prefix: types.String = prefix

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets `suffix`.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def bounds(self) -> types.Tuple(types.Real):
        """
        Upper cosine bounds for bin

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bounds

    @bounds.setter
    def bounds(self, bounds: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `bounds`.

        Parameters:
            bounds: Upper cosine bounds for bin.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bounds is not None:
            array = []
            for item in bounds:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            bounds = types.Tuple(types.Real)(array)

        if bounds is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bounds)

        self._bounds: types.Tuple(types.Real) = bounds

    @property
    def t(self) -> types.String:
        """
        Notation to provide totals

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._t

    @t.setter
    def t(self, t: str | types.String) -> None:
        """
        Sets `t`.

        Parameters:
            t: Notation to provide totals.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if t is not None:
            if isinstance(t, types.String):
                t = t
            elif isinstance(t, str):
                t = types.String.from_mcnp(t)

        self._t: types.String = t

    @property
    def c(self) -> types.String:
        """
        Notation to make bin values cumulative

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._c

    @c.setter
    def c(self, c: str | types.String) -> None:
        """
        Sets `c`.

        Parameters:
            c: Notation to make bin values cumulative.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if c is not None:
            if isinstance(c, types.String):
                c = c
            elif isinstance(c, str):
                c = types.String.from_mcnp(c)

        self._c: types.String = c
