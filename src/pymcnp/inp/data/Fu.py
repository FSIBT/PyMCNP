import re

from . import _option
from ... import types
from ... import errors


class Fu(_option.DataOption):
    """
    Represents INP fu elements.
    """

    _KEYWORD = 'fu'

    _ATTRS = {
        'suffix': types.Integer,
        'bounds': types.Tuple(types.Real),
        'nt': types.String,
        'c': types.String,
    }

    _REGEX = re.compile(rf'\Afu(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)(?: (nt))?(?: (c))?\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, bounds: list[str] | list[float] | list[types.Real], nt: str | types.String = None, c: str | types.String = None):
        """
        Initializes ``Fu``.

        Parameters:
            suffix: Data card option suffix.
            bounds: Input parameters for user bins.
            nt: Notation to inhibit automatic totaling.
            c: Notation to make bin values cumulative.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.bounds: types.Tuple(types.Real) = bounds
        self.nt: types.String = nt
        self.c: types.String = c

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
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

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def bounds(self) -> types.Tuple(types.Real):
        """
        Input parameters for user bins

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._bounds

    @bounds.setter
    def bounds(self, bounds: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets ``bounds``.

        Parameters:
            bounds: Input parameters for user bins.

        Raises:
            InpError: SEMANTICS_OPTION.
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
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bounds)

        self._bounds: types.Tuple(types.Real) = bounds

    @property
    def nt(self) -> types.String:
        """
        Notation to inhibit automatic totaling

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
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

        if nt is not None and nt.value.lower() not in {'nt'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nt)

        self._nt: types.String = nt

    @property
    def c(self) -> types.String:
        """
        Notation to make bin values cumulative

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
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

        if c is not None and c.value.lower() not in {'c'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, c)

        self._c: types.String = c
