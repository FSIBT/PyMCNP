import re

from . import pikmt
from . import _card
from .. import types
from .. import errors


class Pikmt(_card.Card):
    """
    Represents INP `pikmt` cards.
    """

    _KEYWORD = 'pikmt'

    _ATTRS = {
        'biases': types.Tuple(pikmt.Photonbias),
    }

    _REGEX = re.compile(rf'\Apikmt((?: {pikmt.Photonbias._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, biases: list[str] | list[pikmt.Photonbias]):
        """
        Initializes `Pikmt`.

        Parameters:
            biases: Biases for proton production.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.biases: types.Tuple(pikmt.Photonbias) = biases

    @property
    def biases(self) -> types.Tuple(pikmt.Photonbias):
        """
        Biases for proton production

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._biases

    @biases.setter
    def biases(self, biases: list[str] | list[pikmt.Photonbias]) -> None:
        """
        Sets `biases`.

        Parameters:
            biases: Biases for proton production.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if biases is not None:
            array = []
            for item in biases:
                if isinstance(item, pikmt.Photonbias):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(pikmt.Photonbias.from_mcnp(item))
            biases = types.Tuple(pikmt.Photonbias)(array)

        if biases is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, biases)

        self._biases: types.Tuple(pikmt.Photonbias) = biases
