import re

from . import _option
from ... import types
from ... import errors


class Xlims(_option.MplotOption):
    """
    Represents INP `xlims` elements.
    """

    _KEYWORD = 'xlims'

    _ATTRS = {
        'lower': types.Real,
        'upper': types.Real,
        'nsteps': types.Real,
    }

    _REGEX = re.compile(rf'\Axlims( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)

    def __init__(self, lower: str | int | float | types.Real, upper: str | int | float | types.Real, nsteps: str | int | float | types.Real = None):
        """
        Initializes `Xlims`.

        Parameters:
            lower: x-axis lower limit.
            upper: x-axis upper limit.
            nsteps: x-axis interval.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.lower: types.Real = lower
        self.upper: types.Real = upper
        self.nsteps: types.Real = nsteps

    @property
    def lower(self) -> types.Real:
        """
        X-axis lower limit

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._lower

    @lower.setter
    def lower(self, lower: str | int | float | types.Real) -> None:
        """
        Sets `lower`.

        Parameters:
            lower: x-axis lower limit.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if lower is not None:
            if isinstance(lower, types.Real):
                lower = lower
            elif isinstance(lower, int) or isinstance(lower, float):
                lower = types.Real(lower)
            elif isinstance(lower, str):
                lower = types.Real.from_mcnp(lower)

        if lower is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, lower)

        self._lower: types.Real = lower

    @property
    def upper(self) -> types.Real:
        """
        X-axis upper limit

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._upper

    @upper.setter
    def upper(self, upper: str | int | float | types.Real) -> None:
        """
        Sets `upper`.

        Parameters:
            upper: x-axis upper limit.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if upper is not None:
            if isinstance(upper, types.Real):
                upper = upper
            elif isinstance(upper, int) or isinstance(upper, float):
                upper = types.Real(upper)
            elif isinstance(upper, str):
                upper = types.Real.from_mcnp(upper)

        if upper is None or not (self.lower < upper):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, upper)

        self._upper: types.Real = upper

    @property
    def nsteps(self) -> types.Real:
        """
        X-axis interval

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._nsteps

    @nsteps.setter
    def nsteps(self, nsteps: str | int | float | types.Real) -> None:
        """
        Sets `nsteps`.

        Parameters:
            nsteps: x-axis interval.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if nsteps is not None:
            if isinstance(nsteps, types.Real):
                nsteps = nsteps
            elif isinstance(nsteps, int) or isinstance(nsteps, float):
                nsteps = types.Real(nsteps)
            elif isinstance(nsteps, str):
                nsteps = types.Real.from_mcnp(nsteps)

        if nsteps is not None and not (nsteps >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nsteps)

        self._nsteps: types.Real = nsteps
