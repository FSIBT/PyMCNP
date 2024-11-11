from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class MaterialNuclideSubstitution(Datum):
    """
    ``MaterialNuclideSubstitution`` represents INP material nuclide
    substitution data cards.

    ``MaterialNuclideSubstitution`` inherits attributes from ``Datum``. It
    represents the INP material nuclide substitution data card syntax element.

    Attributes:
        zaids: Tuple of ZAID alias.
        suffix: Data card suffix.
        designator: Data card designator.
    """

    def __init__(
        self,
        zaids: tuple[types.Zaid],
        suffix: types.McnpInteger,
        designator: tuple[types.Designator],
    ):
        """
        ``__init__`` initializes ``MaterialNuclideSubstitution``.

        Parameters:
            zaids: Tuple of ZAID alias.
            suffix: Data card suffix.
            designator: Data card designator.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in zaids:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        for particle in designator:
            if particle is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR)

        _card.Card.__init__(self, f'mx{suffix}:{designator.to_mcnp()}')
        self.mnemonic = DatumMnemonic.MATERIAL_NUCLIDE_SUBSTITUTION
        self.parameters = zaids
        self.suffix = suffix
        self.designator = designator

        self.zaids = zaids
