import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Eff(SdefOption_, keyword='eff'):
    """
    Represents INP eff elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'criterion': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Aeff( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, criterion: types.RealOrJump):
        """
        Initializes ``Eff``.

        Parameters:
            criterion: Rejection efficiency criterion for position sampling.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if criterion is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, criterion)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                criterion,
            ]
        )

        self.criterion: typing.Final[types.RealOrJump] = criterion
