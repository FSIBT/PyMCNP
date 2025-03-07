import re
import typing


from .option_ import FmultOption_
from ....utils import types
from ....utils import errors


class Sfnu(FmultOption_, keyword='sfnu'):
    """
    Represents INP sfnu elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'distribution': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'sfnu(( {types.Real._REGEX.pattern})+)')

    def __init__(self, distribution: types.Tuple[types.Real]):
        """
        Initializes ``Sfnu``.

        Parameters:
            distribution: V bar for or of cumulative distribution the sampling spontaneous fission.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if distribution is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, distribution)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                distribution,
            ]
        )

        self.distribution: typing.Final[types.Tuple[types.Real]] = distribution
