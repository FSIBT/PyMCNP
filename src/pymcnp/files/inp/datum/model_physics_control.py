from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import errors


class ModelPhysicsControl(Datum):
    """
    ``ModelPhysicsControl`` represents INP model physics control data cards.

    ``ModelPhysicsControl`` inherits attributes from ``Datum``. It represents
    the INP model physics control data card syntax element.

    Attributes:
        setting: On/Off.
    """

    def __init__(self, setting: str):
        """
        ``__init__`` initializes ``ModelPhysicsControl``.

        Parameters:
            setting: On/Off.
        """

        if setting is None or setting not in {'yes', 'no'}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'mphys')
        self.mnemonic = DatumMnemonic.MODEL_PHYSICS_CONTROL
        self.parameters = (setting,)

        self.setting = setting
