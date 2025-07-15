import re

from . import pikmt
from . import _option
from ...utils import types
from ...utils import errors


class Pikmt(_option.DataOption):
    """
    Represents INP pikmt elements.
    """

    _KEYWORD = 'pikmt'

    _ATTRS = {
        'biases': types.Tuple[pikmt.Photonbias],
    }

    _REGEX = re.compile(rf'\Apikmt((?: {pikmt.Photonbias._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, biases: list[str] | list[pikmt.Photonbias]):
        """
        Initializes ``Pikmt``.

        Parameters:
            biases: Biases for proton production.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.biases: types.Tuple[pikmt.Photonbias] = biases

    @property
    def biases(self) -> types.Tuple[pikmt.Photonbias]:
        """
        Biases for proton production

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._biases

    @biases.setter
    def biases(self, biases: list[str] | list[pikmt.Photonbias]) -> None:
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
                if isinstance(item, pikmt.Photonbias):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(pikmt.Photonbias.from_mcnp(item))
            biases = types.Tuple(array)

        if biases is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, biases)

        self._biases: types.Tuple[pikmt.Photonbias] = biases
