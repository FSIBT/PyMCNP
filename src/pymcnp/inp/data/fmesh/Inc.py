import re
import typing


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Inc(FmeshOption_, keyword='inc'):
    """
    Represents INP inc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'lower': types.Real,
        'upper': types.Real,
    }

    _REGEX = re.compile(r'inc( \S+)( \S+)?')

    def __init__(self, lower: types.Real, upper: types.Real = None):
        """
        Initializes ``Inc``.

        Parameters:
            lower: Collision for FMESH tally lower bound.
            upper: Collision for FMESH tally upper bound.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if lower is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, lower)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                lower,
                upper,
            ]
        )

        self.lower: typing.Final[types.Real] = lower
        self.upper: typing.Final[types.Real] = upper
