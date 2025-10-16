import re

from . import _entry
from ... import types
from ... import errors


class Variables(_entry.DsEntry_2):
    """
    Represents INP `variables` elements.
    """

    _KEYWORD = ''

    _ATTRS = {
        'independent': types.Distribution,
        'dependent': types.Real,
    }

    _REGEX = re.compile(rf'\A({types.Distribution._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, independent: str | types.Distribution, dependent: str | int | float | types.Real):
        """
        Initializes `Variables`.

        Parameters:
            independent: Independent source dependent variable.
            dependent: Dependent source dependent variable.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.independent: types.Distribution = independent
        self.dependent: types.Real = dependent

    @property
    def independent(self) -> types.Real:
        """
        Independent source dependent variable

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._independent

    @independent.setter
    def independent(self, independent: str | types.Distribution) -> None:
        """
        Sets `independent`.

        Parameters:
            independent: Independent source dependent variable.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if independent is not None:
            if isinstance(independent, types.Distribution):
                independent = independent
            elif isinstance(independent, str):
                independent = types.Distribution.from_mcnp(independent)

        if independent is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, independent)

        self._independent: types.Distribution = independent

    @property
    def dependent(self) -> types.Real:
        """
        Dependent source dependent variable

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._dependent

    @dependent.setter
    def dependent(self, dependent: str | int | float | types.Real) -> None:
        """
        Sets `dependent`.

        Parameters:
            dependent: Dependent source dependent variable.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if dependent is not None:
            if isinstance(dependent, types.Real):
                dependent = dependent
            elif isinstance(dependent, int) or isinstance(dependent, float):
                dependent = types.Real(dependent)
            elif isinstance(dependent, str):
                dependent = types.Real.from_mcnp(dependent)

        if dependent is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, dependent)

        self._dependent: types.Real = dependent
