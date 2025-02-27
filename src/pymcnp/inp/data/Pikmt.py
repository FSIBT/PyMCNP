import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Pikmt(DataOption_, keyword='pikmt'):
    """
    Represents INP pikmt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'biases': types.Tuple[types.PhotonBiasEntry],
    }

    _REGEX = re.compile(rf'pikmt(( {types.PhotonBiasEntry._REGEX.pattern})+)')

    def __init__(self, biases: types.Tuple[types.PhotonBiasEntry]):
        """
        Initializes ``Pikmt``.

        Parameters:
            biases: Biases for proton production.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if biases is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, biases)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                biases,
            ]
        )

        self.biases: typing.Final[types.Tuple[types.PhotonBiasEntry]] = biases
