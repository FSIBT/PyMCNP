from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class DeterministicMaterials(Datum):
    """
    ``DeterministicMaterials`` represents INP deterministic materials data
    cards.

    ``DeterministicMaterials`` inherits attributes from ``Datum``. It
    represents the INP deterministic materials data card syntax element.

    Attributes:
        materials: Tuple of Zaids.
        suffix: Data card suffix.
    """

    def __init__(self, materials: tuple[types.Zaid], suffix: types.McnpInteger):
        """
        ``__init__`` initializes ``DeterministicMaterials``.

        Parameters:
            materials: Tuple of ZAID aliases.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in materials:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        _card.Card.__init__(self, f'dm{suffix}')
        self.mnemonic = DatumMnemonic.DETERMINISTIC_MATERIALS
        self.parameters = materials
        self.suffix = suffix

        self.materials = materials
