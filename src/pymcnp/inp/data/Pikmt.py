import re

from . import _option
from ...utils import types
from ...utils import errors


class Pikmt(_option.DataOption):
    """
    Represents INP pikmt elements.
    """

    _KEYWORD = 'pikmt'

    _ATTRS = {
        'biases': types.Tuple[types.PhotonBias],
    }

    _REGEX = re.compile(rf'\Apikmt((?: {types.PhotonBias._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, biases: list[str] | list[types.PhotonBias]):
        """
        Initializes ``Pikmt``.

        Parameters:
            biases: Biases for proton production.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.biases: types.Tuple[types.PhotonBias] = biases

    @property
    def biases(self) -> types.Tuple[types.PhotonBias]:
        """
        Biases for proton production

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._biases

    @biases.setter
    def biases(self, biases: list[str] | list[types.PhotonBias]) -> None:
        """
        Sets ``biases``.

        Parameters:
            biases: Biases for proton production.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if biases is not None:
            array = []
            for item in biases:
                if isinstance(item, types.PhotonBias):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.PhotonBias.from_mcnp(item))
            biases = types.Tuple(array)

        if biases is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, biases)

        self._biases: types.Tuple[types.PhotonBias] = biases
