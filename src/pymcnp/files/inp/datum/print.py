from typing import Final

from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import errors
from ...utils import types


class Print(Datum):
    """
    ``Print`` represents INP output print tables data cards.

    ``Print`` inherits attributes from ``Datum``. It represents the INP output
    print tables data card syntax element.

    Attributes:
        tables: Tuple of table numbers.
    """

    def __init__(self, tables: tuple[types.McnpInteger]):
        """
        ``__init__`` initializes ``Print``.

        Parameters:
            tables: Tuple of table numbers.
        """

        if tables is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for number in tables:
            if number is None or number not in {
                -1,
                10,
                20,
                30,
                32,
                35,
                38,
                40,
                41,
                44,
                50,
                55,
                60,
                62,
                70,
                72,
                80,
                85,
                86,
                87,
                90,
                95,
                98,
                100,
                102,
                110,
                115,
                117,
                118,
                120,
                126,
                128,
                130,
                140,
                150,
                160,
                161,
                162,
                163,
                170,
                175,
                178,
                180,
                190,
                198,
                200,
                210,
                220,
                -10,
                -20,
                -30,
                -32,
                -35,
                -38,
                -40,
                -41,
                -44,
                -50,
                -55,
                -60,
                -62,
                -70,
                -72,
                -80,
                -85,
                -86,
                -87,
                -90,
                -95,
                -98,
                -100,
                -102,
                -110,
                -115,
                -117,
                -118,
                -120,
                -126,
                -128,
                -130,
                -140,
                -150,
                -160,
                -161,
                -162,
                -163,
                -170,
                -175,
                -178,
                -180,
                -190,
                -198,
                -200,
                -210,
                -220,
            }:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'print')
        self.mnemonic: Final[DatumMnemonic] = DatumMnemonic.OUTPUT_PRINT_TABLES
        self.parameters: Final[tuple] = tables

        self.tables: Final[tuple] = tables
