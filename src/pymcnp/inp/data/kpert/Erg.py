import re
import typing


from .option_ import KpertOption_
from ....utils import types
from ....utils import errors


class Erg(KpertOption_, keyword='erg'):
    """
    Represents INP erg elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'energies': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'erg(( {types.Real._REGEX.pattern})+)')

    def __init__(self, energies: types.Tuple[types.Real]):
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

        self.energies: typing.Final[types.Tuple[types.Real]] = energies
