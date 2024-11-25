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
    BFIELD = 'bflcl'
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


class CellOption(_card.CardOption):
    """
    Represents INP cell card option keywords.

    ``CellOption`` implements ``_card.CardOption``.

    Attributes:
        keyword: Cell card option keyword.
        value: Cell card option value.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self) -> str:
        """
        Generates INP from ``CellOption`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``CellOption``.
        """

        # Processing Suffix
        suffix_str = str(self.suffix.to_mcnp()) if hasattr(self, 'suffix') else ''

        # Processing Designator
        designator_str = (
            f":{','.join(self.designator.particles)}"
            if hasattr(self, 'designator') and self.designator is not None
            else ''
        )

        value_str = ''
        if isinstance(self.value, tuple):
            value_str = ' '.join(
                [
                    str(param.value) if hasattr(param, 'value') else str(param)
                    for param in self.value
                ]
            )
        else:
            value_str = self.value.value if hasattr(self.value, 'value') else str(self.value)

        return f'{self.keyword.to_mcnp()}{suffix_str}{designator_str}={value_str}'
