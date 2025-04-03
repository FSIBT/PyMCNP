import re
import typing


from .option_ import PertOption_
from ....utils import types
from ....utils import errors


class Rho(PertOption_, keyword='rho'):
    """
    Represents INP rho elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'density': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Arho( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, density: types.RealOrJump):
        """
        Initializes ``Rho``.

        Parameters:
            density: Perturbed density.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if density is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, density)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                density,
            ]
        )

        self.density: typing.Final[types.RealOrJump] = density
