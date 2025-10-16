import re

from . import _option
from ... import types
from ... import errors


class Inc(_option.FmeshOption):
    """
    Represents INP `inc` elements.
    """

    _KEYWORD = 'inc'

    _ATTRS = {
        'lower': types.Real,
        'upper': types.Real,
    }

    _REGEX = re.compile(rf'\Ainc( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)

    def __init__(self, lower: str | int | float | types.Real, upper: str | int | float | types.Real = None):
        """
        Initializes `Inc`.

        Parameters:
            lower: Collision for FMESH tally lower bound.
            upper: Collision for FMESH tally upper bound.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.lower: types.Real = lower
        self.upper: types.Real = upper

    @property
    def lower(self) -> types.Real:
        """
        Collision for FMESH tally lower bound

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
            lower: Collision for FMESH tally lower bound.

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
        Collision for FMESH tally upper bound

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
            upper: Collision for FMESH tally upper bound.

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

        self._upper: types.Real = upper
