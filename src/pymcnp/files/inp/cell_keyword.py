"""
Contains classes representing INP cell card option keywords.
"""

from . import _card
from ..utils import errors
from ..utils import _parser


class CellKeyword(_card.CardKeyword):
    """
    Represents INP cell card option keywords.

    ``CellKeyword`` implements ``_card.CardKeyword``.
    """

    IMP = 'imp'
    VOL = 'vol'
    PWT = 'pwt'
    EXT = 'ext'
    FCL = 'fcl'
    WWN = 'wwn'
    DXC = 'dxc'
    NONU = 'nonu'
    PD = 'pd'
    TMP = 'tmp'
    U = 'u'
    TRCL = 'trcl'
    # COORDINATE_TRANSFORMATION_ANGLE = '*trcl'
    LAT = 'lat'
    FILL = 'fill'
    # FILL_ANGLE = '*fill'
    ELPT = 'elpt'
    COSY = 'cosy'
    BFLCL = 'bflcl'
    UNC = 'unc'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``CellKeyword``

        Returns:
            ``CellKeyword`` object.

        Raises:
            MCNPError: UNRECOGNIZED_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return CellKeyword(source)
        except ValueError:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, source)
