import re
import typing


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Emesh(FmeshOption_, keyword='emesh'):
    """
    Represents INP emesh elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'energy': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Aemesh( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, energy: types.RealOrJump):
        """
        Initializes ``Emesh``.

        Parameters:
            energy: Values of mesh points in energy.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if energy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                energy,
            ]
        )

        self.energy: typing.Final[types.RealOrJump] = energy
