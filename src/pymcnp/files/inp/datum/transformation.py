from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class Transformation(Datum):
    """
    ``Transformation`` represents INP transformion data cards.

    ``Transformation`` inherits attributes from ``Datum``. It represents the INP
    transformion data card syntax element.

    Attributes:
        displacement: Transformation displacement vector.
        rotation: Transformation rotation matrix.
        system: Transformation coordinate system setting.
        suffix: Data card suffix.
    """

    def __init__(
        self,
        displacement: tuple[float],
        rotation: tuple[tuple[float]],
        system: types.McnpInteger,
        suffix: types.McnpInteger,
        is_angle: bool,
    ):
        """
        ``__init__`` initializes ``Transformation``.

        Parameters:
            displacement: Transformation displacement vector.
            rotation: Transformation rotation matrix.
            system: Transformation coordinate system setting.
            suffix: Data card suffix.
            is_angle: Angle units modifier.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSematnicCodes.INVALID_DATUM_SUFFIX)

        for entry in displacement:
            if entry is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for row in rotation:
            for entry in row:
                if entry is None:
                    raise errors.MCNPSemanticError(
                        errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS
                    )

        if system is None or system not in {-1, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, f'tr{suffix}')
        self.mnemonic = DatumMnemonic.TRANSFORMATION
        self.parameters = (displacement, rotation, system)
        self.suffix = suffix

        self.displacement = displacement
        self.rotation = rotation
        self.system = system
        self.is_angle = is_angle
