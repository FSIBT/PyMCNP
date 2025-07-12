import re

from . import _option
from ....utils import types
from ....utils import errors


class Filter(_option.PtracOption):
    """
    Represents INP filter elements.
    """

    _KEYWORD = 'filter'

    _ATTRS = {
        'variables': types.Tuple[types.PtracFilter],
    }

    _REGEX = re.compile(rf'\Afilter((?: {types.PtracFilter._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, variables: list[str] | list[types.PtracFilter]):
        """
        Initializes ``Filter``.

        Parameters:
            variables: MCNP6 variables for filtering.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.variables: types.Tuple[types.PtracFilter] = variables

    @property
    def variables(self) -> types.Tuple[types.PtracFilter]:
        """
        MCNP6 variables for filtering

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._variables

    @variables.setter
    def variables(self, variables: list[str] | list[types.PtracFilter]) -> None:
        """
        Sets ``variables``.

        Parameters:
            variables: MCNP6 variables for filtering.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if variables is not None:
            array = []
            for item in variables:
                if isinstance(item, types.PtracFilter):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.PtracFilter.from_mcnp(item))

            variables = types.Tuple(array)

        if variables is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, variables)

        self._variables: types.Tuple[types.PtracFilter] = variables
