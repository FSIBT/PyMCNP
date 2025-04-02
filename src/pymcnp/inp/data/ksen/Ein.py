import re
import typing


from .option_ import KsenOption_
from ....utils import types
from ....utils import errors


class Ein(KsenOption_, keyword='ein'):
    """
    Represents INP ein elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'energies': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aein((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, energies: types.Tuple[types.Real]):
        """
        Initializes ``Ein``.

        Parameters:
            energies: List of ranges for incident energies.

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
