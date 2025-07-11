import re

from . import _option
from ...utils import types
from ...utils import errors


class F_2(_option.DataOption):
    """
    Represents INP f variation #2 elements.

    Attributes:
        prefix: Star prefix.
        suffix: Data card option suffix.
        a: Letter.
        designator: Data card particle designator.
        rings: Detector points.
        nd: Total/average specified surfaces/cells option.
    """

    _KEYWORD = 'f'

    _ATTRS = {
        'prefix': types.String,
        'suffix': types.Integer,
        'a': types.String,
        'designator': types.Designator,
        'rings': types.Tuple[types.Ring],
        'nd': types.String,
    }

    _REGEX = re.compile(r'\A([*+])?f(\d*[5])([xyz])(?::(\S+))?((?: \S+ \S+ \S+)+?)( nd)?\Z')

    def __init__(
        self,
        suffix: str | int | types.Integer,
        a: str | types.String,
        rings: list[str] | list[types.Ring],
        prefix: str | types.String = None,
        designator: str | types.Designator = None,
        nd: str | types.String = None,
    ):
        """
        Initializes ``F_2``.

        Parameters:
            prefix: Star prefix.
            suffix: Data card option suffix.
            a: Letter.
            designator: Data card particle designator.
            rings: Detector points.
            nd: Total/average specified surfaces/cells option.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.prefix: types.String = prefix
        self.suffix: types.Integer = suffix
        self.a: types.String = a
        self.designator: types.Designator = designator
        self.rings: types.Tuple[types.Ring] = rings
        self.nd: types.String = nd

    @property
    def prefix(self) -> types.String:
        """
        Gets ``prefix``.

        Returns:
            ``prefix``.
        """

        return self._prefix

    @prefix.setter
    def prefix(self, prefix: str | types.String) -> None:
        """
        Sets ``prefix``.

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
            else:
                raise TypeError

        if prefix is not None and prefix not in {'*', '+'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, prefix)

        self._prefix: types.String = prefix

    @property
    def suffix(self) -> types.Integer:
        """
        Gets ``suffix``.

        Returns:
            ``suffix``.
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets ``suffix``.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)
            else:
                raise TypeError

        if suffix is None or not (suffix <= 99_999_999 and suffix % 10 == 5):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def a(self) -> types.String:
        """
        Gets ``a``.

        Returns:
            ``a``.
        """

        return self._a

    @a.setter
    def a(self, a: str | types.String) -> None:
        """
        Sets ``a``.

        Parameters:
            a: Letter.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if a is not None:
            if isinstance(a, types.String):
                a = a
            elif isinstance(a, str):
                a = types.String.from_mcnp(a)
            else:
                raise TypeError

        if a is None or a not in {'x', 'y', 'z'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a)

        self._a: types.String = a

    def to_mcnp(self):
        """
        Generates INP from ``F_2``.

        Returns:
            INP for ``F_2``.
        """

        return f'{self.prefix or ""}f{self.suffix}{self.a}{f":{self.designator}" if self.designator else ""} {self.rings} {self.nd or ""}'

    @property
    def designator(self) -> types.Designator:
        """
        Gets ``designator``.

        Returns:
            ``designator``.
        """

        return self._designator

    @designator.setter
    def designator(self, designator: str | types.Designator) -> None:
        """
        Sets ``designator``.

        Parameters:
            designator: Data card particle designator.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if designator is not None:
            if isinstance(designator, types.Designator):
                designator = designator
            elif isinstance(designator, str):
                designator = types.Designator.from_mcnp(designator)
            else:
                raise TypeError

        self._designator: types.Designator = designator

    @property
    def rings(self) -> types.Tuple[types.Ring]:
        """
        Gets ``rings``.

        Returns:
            ``rings``.
        """

        return self._rings

    @rings.setter
    def rings(self, rings: list[str] | list[types.Ring]) -> None:
        """
        Sets ``rings``.

        Parameters:
            rings: Detector points.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if rings is not None:
            array = []
            for item in rings:
                if isinstance(item, types.Ring):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.Ring.from_mcnp(item))
                else:
                    raise TypeError
            rings = types.Tuple(array)

        if rings is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, rings)

        self._rings: types.Tuple[types.Ring] = rings

    @property
    def nd(self) -> types.String:
        """
        Gets ``nd``.

        Returns:
            ``nd``.
        """

        return self._nd

    @nd.setter
    def nd(self, nd: str | types.String) -> None:
        """
        Sets ``nd``.

        Parameters:
            nd: Total/average specified surfaces/cells option.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if nd is not None:
            if isinstance(nd, types.String):
                nd = nd
            elif isinstance(nd, str):
                nd = types.String.from_mcnp(nd)
            else:
                raise TypeError

        if nd is not None and not (nd == 'nd'):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nd)

        self._nd: types.String = nd
