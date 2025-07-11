import re

from . import _option
from ...utils import types
from ...utils import errors


class E(_option.DataOption):
    """
    Represents INP e elements.

    Attributes:
        suffix: Data card option suffix.
        bounds: Upper energy bounds for bin.
        nt: Notation to inhibit automatic totaling.
        c: Notation to make bin values cumulative.
    """

    _KEYWORD = 'e'

    _ATTRS = {
        'suffix': types.Integer,
        'bounds': types.Tuple[types.Real],
        'nt': types.String,
        'c': types.String,
    }

    _REGEX = re.compile(rf'\Ae(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, suffix: str | int | types.Integer, bounds: list[str] | list[float] | list[types.Real], nt: str | types.String = None, c: str | types.String = None):
        """
        Initializes ``E``.

        Parameters:
            suffix: Data card option suffix.
            bounds: Upper energy bounds for bin.
            nt: Notation to inhibit automatic totaling.
            c: Notation to make bin values cumulative.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.bounds: types.Tuple[types.Real] = bounds
        self.nt: types.String = nt
        self.c: types.String = c

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

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def bounds(self) -> types.Tuple[types.Real]:
        """
        Gets ``bounds``.

        Returns:
            ``bounds``.
        """

        return self._bounds

    @bounds.setter
    def bounds(self, bounds: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets ``bounds``.

        Parameters:
            bounds: Upper energy bounds for bin.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if bounds is not None:
            array = []
            for item in bounds:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Real(item))
                elif isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
                else:
                    raise TypeError
            bounds = types.Tuple(array)

        if bounds is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bounds)

        self._bounds: types.Tuple[types.Real] = bounds

    @property
    def nt(self) -> types.String:
        """
        Gets ``nt``.

        Returns:
            ``nt``.
        """

        return self._nt

    @nt.setter
    def nt(self, nt: str | types.String) -> None:
        """
        Sets ``nt``.

        Parameters:
            nt: Notation to inhibit automatic totaling.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if nt is not None:
            if isinstance(nt, types.String):
                nt = nt
            elif isinstance(nt, str):
                nt = types.String.from_mcnp(nt)
            else:
                raise TypeError

        self._nt: types.String = nt

    @property
    def c(self) -> types.String:
        """
        Gets ``c``.

        Returns:
            ``c``.
        """

        return self._c

    @c.setter
    def c(self, c: str | types.String) -> None:
        """
        Sets ``c``.

        Parameters:
            c: Notation to make bin values cumulative.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if c is not None:
            if isinstance(c, types.String):
                c = c
            elif isinstance(c, str):
                c = types.String.from_mcnp(c)
            else:
                raise TypeError

        self._c: types.String = c
