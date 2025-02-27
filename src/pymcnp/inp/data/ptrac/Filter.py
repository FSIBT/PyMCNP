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
        'variables': types.Tuple[types.PtracFilterEntry],
    }

    _REGEX = re.compile(rf'filter(( {types.PtracFilterEntry._REGEX.pattern})+)')

    def __init__(self, variables: types.Tuple[types.PtracFilterEntry]):
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

        self.variables: typing.Final[types.Tuple[types.PtracFilterEntry]] = variables
