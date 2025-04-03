import re
import typing


from .option_ import KsenOption_
from ....utils import types
from ....utils import errors


class Erg(KsenOption_, keyword='erg'):
    """
    Represents INP erg elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'energies': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aerg((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, energies: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Erg``.

        Parameters:
            energies: List of energies.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if energies is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energies)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                energies,
            ]
        )

        self.energies: typing.Final[types.Tuple[types.RealOrJump]] = energies
