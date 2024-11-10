from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CrossSectionFileValue:
    """
    ``CrossSectionFileValue`` represents INP cross-section file data card
    entries.

    ``CrossSectionFileValue`` implements INP material specifications as a
    Python inner class. Its attributes store different mateiral entries,
    and its methods provide entry points and endpoints for working with
    cross-section file entries. ``CrossSectionFile`` depends on
    ``CrossSectionFileValue`` as a data type.

    Attributes:
        weight_ratios: Tuple of weight ratios.
    """

    def __init__(self, zaid: types.Zaid, ratio: types.McnpReal):
        """
        ``__init__`` initializes ``CrossSectionFile``.
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
        ``from_mcnp`` generates ``CrossSectionFileValue`` objects from INP.

        ``from_mcnp`` constructs instances of ``CrossSectionFileValue``
        from INP source strings, so it operates as a class constructor
        method and INP parser helper function.

        Parameters:
            source: INP for cross-section file values.

        Returns:
            ``CrossSectionFileValue`` object.

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

        return CrossSectionFileValue(zaid, ratio)


class CrossSectionFile(Datum):
    """
    ``CrossSectionFile`` represents INP cross-section file data cards.

    ``CrossSectionFile`` inherits attributes from ``Datum``. It represents the
    INP cross-section file data card syntax element.

    Attributes:
        weight_ratios: Tuple of weight ratios.
        suffix: Data card suffix.
    """

    def __init__(self, weight_ratios: tuple[CrossSectionFileValue], suffix: types.McnpInteger):
        """
        ``__init__`` initializes ``CrossSectionFile``.

        Parameters:
            weight_ratios: Tuple of weight ratios.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if weight_ratios is None or not weight_ratios:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for weight_ratio in weight_ratios:
            if weight_ratio is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, f'xs{suffix}')
        self.mnemonic = DatumMnemonic.CROSS_SECTION_FILE
        self.parameters = weight_ratios
        self.suffix = suffix

        self.weight_ratios = weight_ratios
