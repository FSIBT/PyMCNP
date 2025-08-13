import re

from . import _card
from .. import types
from .. import errors


class Fs(_card.Card):
    """
    Represents INP `fs` cards.
    """

    _KEYWORD = 'fs'

    _ATTRS = {
        'suffix': types.Integer,
        'numbers': types.Tuple(types.Integer),
        't': types.String,
        'c': types.String,
    }

    _REGEX = re.compile(rf'\Afs(\d+)((?: {types.Integer._REGEX.pattern[2:-2]})+?)( t)?( c)?\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, numbers: list[str] | list[int] | list[types.Integer], t: str | types.String = None, c: str | types.String = None):
        """
        Initializes `Fs`.

        Parameters:
            suffix: Data card option suffix.
            numbers: Signed problem number of a segmenting surface..
            t: Notation to provide totals.
            c: Notation to make bin values cumulative.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.numbers: types.Tuple(types.Integer) = numbers
        self.t: types.String = t
        self.c: types.String = c

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

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def numbers(self) -> types.Tuple(types.Integer):
        """
        Signed problem number of a segmenting surface.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._numbers

    @numbers.setter
    def numbers(self, numbers: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets `numbers`.

        Parameters:
            numbers: Signed problem number of a segmenting surface..

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if numbers is not None:
            array = []
            for item in numbers:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))
            numbers = types.Tuple(types.Integer)(array)

        if numbers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, numbers)

        self._numbers: types.Tuple(types.Integer) = numbers

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

        if t is not None and t.value.lower() not in {'t'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, t)

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

        if c is not None and c.value.lower() not in {'c'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, c)

        self._c: types.String = c
