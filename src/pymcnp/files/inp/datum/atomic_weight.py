from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors
from ...utils import _parser


class AtomicWeightValue:
    """
    ``AtomicWeightValue`` represents INP atomic weight data card entries.

    ``AtomicWeightValue`` implements INP material specifications as a
    Python inner class. Its attributes store different mateiral entries,
    and its methods provide entry points and endpoints for working with
    atomic weight entries. ``AtomicWeight`` depends on
    ``AtomicWeightValue`` as a data type.

    Attributes:
        zaid: Atomic weight value Zaid specifier.
        ratio: Atomic weight value weight ratio.
    """

    def __init__(self, zaid: types.Zaid, ratio: types.McnpReal):
        """
        ``__init__`` initializes ``AtomicWeightValue``.
        """

        if zaid is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ratio is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.zaid: types.Zaid = zaid
        self.ratio: types.McnpReal = ratio

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``AtomicWeightValue`` objects from INP.

        ``from_mcnp`` constructs instances of ``AtomicWeightValue`` from
        INP source strings, so it operates as a class constructor method
        and INP parser helper function.

        Parameters:
            source: INP for atomic weight values.

        Returns:
            ``AtomicWeightValue`` object.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSyntaxError: TOOFEW_DATUM_WEIGHT, TOOLONG_DATUM_WEIGHT.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split(' '),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_WEIGHT),
        )

        zaid = types.Zaid.from_mcnp(tokens.popl())
        ratio = types.McnpReal.from_mcnp(tokens.popl())

        if tokens:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_WEIGHT)

        return AtomicWeightValue(zaid, ratio)


class AtomicWeight(Datum):
    """
    ``AtomicWeight`` represents INP atomic weight data cards.

    ``AtomicWeight`` inherits attributes from ``Datum``. It represents
    the INP atomic weight data card syntax element.

    Attributes:
        weight_ratios: Tuple of weight ratios.
    """

    def __init__(self, weight_ratios: tuple[AtomicWeightValue]):
        """
        ``__init__`` initializes ``AtomicWeight``.

        Parameters:
            weight_ratios: Tuple of weight ratios.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in weight_ratios:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'awtab')
        self.mnemonic = DatumMnemonic.ATOMIC_WEIGHT
        self.parameters = weight_ratios

        self.weight_ratios = weight_ratios
