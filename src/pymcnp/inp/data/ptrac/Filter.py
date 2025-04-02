import re
import typing


from .option_ import PtracOption_
from ....utils import types
from ....utils import errors


class Filter(PtracOption_, keyword='filter'):
    """
    Represents INP filter elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'variables': types.Tuple[types.PtracFilter],
    }

    _REGEX = re.compile(rf'\Afilter((?: {types.PtracFilter._REGEX.pattern})+?)\Z')

    def __init__(self, variables: types.Tuple[types.PtracFilter]):
        """
        Initializes ``Filter``.

        Parameters:
            variables: MCNP6 variables for filtering.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if variables is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, variables)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                variables,
            ]
        )

        self.variables: typing.Final[types.Tuple[types.PtracFilter]] = variables
