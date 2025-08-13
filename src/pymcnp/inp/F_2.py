import re

from . import f_2
from . import _card
from .. import types
from .. import errors


class F_2(_card.Card):
    """
    Represents INP `f` elements variation #2.
    """

    _KEYWORD = 'f'

    _ATTRS = {
        'prefix': types.String,
        'suffix': types.Integer,
        'a': types.String,
        'designator': types.Designator,
        'rings': types.Tuple(f_2.Ring),
        'nd': types.String,
    }

    _REGEX = re.compile(r'\A([*+])?f(\d*[5])([xyz])(?::(\S+))?((?: \S+ \S+ \S+)+?)( nd)?\Z', re.IGNORECASE)

    def __init__(
        self,
        suffix: str | int | types.Integer,
        a: str | types.String,
        rings: list[str] | list[f_2.Ring],
        prefix: str | types.String = None,
        designator: str | types.Designator = None,
        nd: str | types.String = None,
    ):
        """
        Initializes `F_2`.

        Parameters:
            prefix: Star prefix.
            suffix: Data card option suffix.
            a: Letter.
            designator: Data card particle designator.
            rings: Detector points.
            nd: Total/average specified surfaces/cells option.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.prefix: types.String = prefix
        self.suffix: types.Integer = suffix
        self.a: types.String = a
        self.designator: types.Designator = designator
        self.rings: types.Tuple(f_2.Ring) = rings
        self.nd: types.String = nd

    def to_mcnp(self):
        """
        Generates INP from `F_2`.

        Returns:
            INP for `F_2`.
        """

        return f'{self.prefix if self.prefix is not None else ""}f{self.suffix}{self.a}{f":{self.designator}" if self.designator is not None else ""} {self.rings} {self.nd if self.nd is not None else ""}'

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

        if suffix is None or not (suffix <= 99_999_999 and suffix % 10 == 5):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def a(self) -> types.String:
        """
        Letter

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a

    @a.setter
    def a(self, a: str | types.String) -> None:
        """
        Sets `a`.

        Parameters:
            a: Letter.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a is not None:
            if isinstance(a, types.String):
                a = a
            elif isinstance(a, str):
                a = types.String.from_mcnp(a)

        if a is None or a.value.lower() not in {'x', 'y', 'z'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, a)

        self._a: types.String = a

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
    def rings(self) -> types.Tuple(f_2.Ring):
        """
        Detector points

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._rings

    @rings.setter
    def rings(self, rings: list[str] | list[f_2.Ring]) -> None:
        """
        Sets `rings`.

        Parameters:
            rings: Detector points.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if rings is not None:
            array = []
            for item in rings:
                if isinstance(item, f_2.Ring):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(f_2.Ring.from_mcnp(item))
            rings = types.Tuple(f_2.Ring)(array)

        if rings is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, rings)

        self._rings: types.Tuple(f_2.Ring) = rings

    @property
    def nd(self) -> types.String:
        """
        Total/average specified surfaces/cells option

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._nd

    @nd.setter
    def nd(self, nd: str | types.String) -> None:
        """
        Sets `nd`.

        Parameters:
            nd: Total/average specified surfaces/cells option.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if nd is not None:
            if isinstance(nd, types.String):
                nd = nd
            elif isinstance(nd, str):
                nd = types.String.from_mcnp(nd)

        if nd is not None and not (nd == 'nd'):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, nd)

        self._nd: types.String = nd
