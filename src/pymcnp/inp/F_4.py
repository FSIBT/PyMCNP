import re

from . import _card
from .. import types
from .. import errors


class F_4(_card.Card):
    """
    Represents INP `f` elements variation #4.
    """

    _KEYWORD = 'f'

    _ATTRS = {
        'prefix': types.String,
        'suffix': types.Integer,
        'designator': types.Designator,
        'problems': types.Tuple(types.Lattice),
        't': types.String,
    }

    _REGEX = re.compile(rf'\A([*+])?f(\d*[123467])(?::(\S+))?((?: {types.Lattice._REGEX.pattern[3:-3]})+?)( t)?\Z', re.IGNORECASE)

    def __init__(
        self,
        suffix: str | int | types.Integer,
        problems: list[str] | list[types.Lattice],
        prefix: str | types.String = None,
        designator: str | types.Designator = None,
        t: str | types.String = None,
    ):
        """
        Initializes `F_4`.

        Parameters:
            prefix: Star prefix.
            suffix: Data card option suffix.
            designator: Data card particle designator.
            problems: Problem numbers of surface or cell.
            t: Notation to make bin values cumulative.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.prefix: types.String = prefix
        self.suffix: types.Integer = suffix
        self.designator: types.Designator = designator
        self.problems: types.Tuple(types.Lattice) = problems
        self.t: types.String = t

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

        if suffix is None or not (suffix <= 99_999_999 and suffix % 10 in {1, 2, 4, 6, 7}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def designator(self) -> types.Designator:
        """
        Data card particle designator

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._designator

    @designator.setter
    def designator(self, designator: str | types.Designator) -> None:
        """
        Sets `designator`.

        Parameters:
            designator: Data card particle designator.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if designator is not None:
            if isinstance(designator, types.Designator):
                designator = designator
            elif isinstance(designator, str):
                designator = types.Designator.from_mcnp(designator)

        self._designator: types.Designator = designator

    @property
    def problems(self) -> types.Tuple(types.Lattice):
        """
        Problem numbers of surface or cell

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._problems

    @problems.setter
    def problems(self, problems: list[str] | list[types.Lattice]) -> None:
        """
        Sets `problems`.

        Parameters:
            problems: Problem numbers of surface or cell.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if problems is not None:
            array = []
            for item in problems:
                if isinstance(item, types.Lattice):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.Lattice.from_mcnp(item))
            problems = types.Tuple(types.Lattice)(array)

        if problems is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, problems)

        self._problems: types.Tuple(types.Lattice) = problems

    @property
    def t(self) -> types.String:
        """
        Notation to make bin values cumulative

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
            t: Notation to make bin values cumulative.

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
