import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Pwt(DataOption_, keyword='pwt'):
    """
    Represents INP pwt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'weights': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Apwt((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, weights: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Pwt``.

        Parameters:
            weights: Relative threshold weight of photons produced at neutron collisions in cell.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if weights is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, weights)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                weights,
            ]
        )

        self.weights: typing.Final[types.Tuple[types.RealOrJump]] = weights
