import re

from . import _entry
from .... import types
from .... import errors


class Entry(_entry.FilterEntry):
    """
    Represents INP `entry` elements.
    """

    _KEYWORD = ''

    _ATTRS = {
        'lower': types.Real,
        'variable': types.String,
        'upper': types.Real,
    }

    _REGEX = re.compile(r'\A([^\s,]+),([^\s,]+)(?:,([^\s,]+))?\Z', re.IGNORECASE)

    def __init__(self, lower: str | int | float | types.Real, upper: str | int | float | types.Real, variable: str | types.String = None):
        """
        Initializes `Entry`.

        Parameters:
            lower: Lower bound for filtering.
            variable: Variable name for PBL derived structure.
            upper: Upper bound for filtering.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.lower: types.Real = lower
        self.variable: types.String = variable
        self.upper: types.Real = upper

    def to_mcnp(self):
        """
        Generates INP from `Entry`.

        Returns:
            INP for `Entry`.
        """

        return f'{self.lower},{self.variable}{f",{self.upper}" if self.upper is not None else ""}'

    @property
    def lower(self) -> types.Real:
        """
        Lower bound for filtering

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
            lower: Lower bound for filtering.

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
    def variable(self) -> types.String:
        """
        Variable name for PBL derived structure

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._variable

    @variable.setter
    def variable(self, variable: str | types.String) -> None:
        """
        Sets `variable`.

        Parameters:
            variable: Variable name for PBL derived structure.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if variable is not None:
            if isinstance(variable, types.String):
                variable = variable
            elif isinstance(variable, str):
                variable = types.String.from_mcnp(variable)

        self._variable: types.String = variable

    @property
    def upper(self) -> types.Real:
        """
        Upper bound for filtering

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
            upper: Upper bound for filtering.

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

        if upper is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, upper)

        self._upper: types.Real = upper
