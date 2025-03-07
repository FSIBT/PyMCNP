import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Erg(SdefOption_, keyword='erg'):
    """
    Represents INP erg elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'energy': types.Real,
    }

    _REGEX = re.compile(rf'erg( {types.Real._REGEX.pattern})')

    def __init__(self, energy: types.Real):
        """
        Initializes ``Erg``.

        Parameters:
            energy: Kinetic energy.

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

        self.energy: typing.Final[types.Real] = energy
