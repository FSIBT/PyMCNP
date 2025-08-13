import re

from . import filter
from . import _option
from ... import types
from ... import errors


class Filter(_option.PtracOption):
    """
    Represents INP `filter` elements.
    """

    _KEYWORD = 'filter'

    _ATTRS = {
        'variables': types.Tuple(filter.Entry),
    }

    _REGEX = re.compile(rf'\Afilter((?: {filter.Entry._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, variables: list[str] | list[filter.Entry]):
        """
        Initializes `Filter`.

        Parameters:
            variables: MCNP6 variables for filtering.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.variables: types.Tuple(filter.Entry) = variables

    @property
    def variables(self) -> types.Tuple(filter.Entry):
        """
        MCNP6 variables for filtering

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._variables

    @variables.setter
    def variables(self, variables: list[str] | list[filter.Entry]) -> None:
        """
        Sets `variables`.

        Parameters:
            variables: MCNP6 variables for filtering.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if variables is not None:
            array = []
            for item in variables:
                if isinstance(item, filter.Entry):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(filter.Entry.from_mcnp(item))
            variables = types.Tuple(filter.Entry)(array)

        if variables is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, variables)

        self._variables: types.Tuple(filter.Entry) = variables
