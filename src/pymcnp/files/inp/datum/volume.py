from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import errors
from ...utils import _parser


class Volume(Datum):
    """
    ``Volume`` represents INP volume data cards.

    ``Volume`` inherits attributes from ``Datum``. It represents the INP volume
    data card syntax element.

    Attributes:
        has_no: No volume calculation option.
        volumes: Tuple of cell volumes.
    """

    def __init__(self, volumes: tuple[float], has_no: bool = False):
        """
        ``__init__`` initializes ``Volume``.

        Parameters:
            has_no: No volume calculation option.
            volumes: Tuple of cell volumes.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for entry in volumes:
            if entry is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if has_no is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'vol')
        self.mnemonic = DatumMnemonic.VOLUME
        self.parameters = (has_no, *volumes)

        self.has_no = has_no
        self.volumes = volumes

    def to_mcnp(self) -> str:
        """Overrides the baseclass function."""

        if self.has_no:
            return _parser.Postprocessor.add_continuation_lines(
                f"vol no {' '.join(str(volume) for volume in self.volumes)}"
            )
        else:
            return _parser.Postprocessor.add_continuation_lines(
                f"vol {' '.join(str(volume) for volume in self.volumes)}"
            )
