from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class MaterialNeutronScattering(Datum):
    """
    ``MaterialNeutronScattering`` represents INP thermal neutron scattering
    data cards.

    ``MaterialNeutronScattering`` inherits attributes from ``Datum``. It
    represents the INP thermal neturon scattering data card syntax element.

    Attributes:
        identifiers: Tuple of material identifiers.
        suffix: Data card suffix.
    """

    def __init__(self, identifiers: tuple[str], suffix: types.McnpInteger):
        """
        ``__init__`` initializes ``MaterialNeutronScattering``.

        Parameters:
            identifiers: Tuple of material identifiers.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in identifiers:
            if parameter is None or not parameter:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        _card.Card.__init__(self, f'mt{suffix}')
        self.mnemonic = DatumMnemonic.MATERIAL_NEUTRON_SCATTERING
        self.parameters = identifiers
        self.suffix = suffix
