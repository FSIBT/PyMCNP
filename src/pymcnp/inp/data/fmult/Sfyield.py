import re
import typing


from .option_ import FmultOption_
from ....utils import types
from ....utils import errors


class Sfyield(FmultOption_, keyword='sfyield'):
    """
    Represents INP sfyield elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'fission_yield': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Asfyield( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, fission_yield: types.RealOrJump):
        """
        Initializes ``Sfyield``.

        Parameters:
            fission_yield: Spontaneous fission yield.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fission_yield is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fission_yield)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fission_yield,
            ]
        )

        self.fission_yield: typing.Final[types.RealOrJump] = fission_yield
