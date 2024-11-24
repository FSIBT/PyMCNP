"""
Contains classes representing INP surface cards.
"""

from . import _card
from ..utils import types  # noqa
from ..utils import errors
from ..utils import _parser


class SurfaceMnemonic(_card.CardMnemonic):
    """
    Represents INP surface card mnemonics.

    ``SurfaceMnemonic`` implements ``_card.CardMnemonic``.
    """

    P = 'p'
    PX = 'px'
    PY = 'py'
    PZ = 'pz'
    SO = 'so'
    S = 's'
    SX = 'sx'
    SY = 'sy'
    SZ = 'sz'
    C_X = 'c/x'
    C_Y = 'c/y'
    C_Z = 'c/z'
    CX = 'cx'
    CY = 'cy'
    CZ = 'cz'
    K_X = 'k/x'
    K_Y = 'k/y'
    K_Z = 'k/z'
    KX = 'kx'
    KY = 'ky'
    KZ = 'kz'
    SQ = 'sq'
    GQ = 'gq'
    TX = 'tx'
    TY = 'ty'
    TZ = 'tz'
    X = 'x'
    Y = 'y'
    Z = 'z'
    BOX = 'box'
    RPP = 'rpp'
    SPH = 'sph'
    RCC = 'rcc'
    RHP = 'rhp'
    REC = 'rec'
    TRC = 'trc'
    ELL = 'ell'
    WED = 'wed'
    ARB = 'arb'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceMnemonic`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``SurfaceMnemonic``.

        Returns:
            ``SurfaceMnemonic`` object.

        Raises:
            McnpError: INVALID_SURFACE_MNEMONIC.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return SurfaceMnemonic(source)
        except ValueError:
            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_MNEMONIC)


class Surface(_card.Card):
    """
    Represents INP data cards.

    ``Surface`` extends the ``_card.Card`` abstract class.

    Attributes:
        ident: Card identifier.
        line_number: Card line number.
        comment: Card inline comment.
        number: Surface card number.
        mnemonic: Surface card type identifier.
        transform: Surface card transformation number.
        periodic: Surface card periodic number.
        parameters: Surface parameter list.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Surface``.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Surface``.
        """

        number_str = self.number.to_mcnp()
        transform_str = self.transform.to_mcnp() if self.transform is not None else ' '
        parameter_str = ' '.join(
            str(parameter.value) if hasattr(parameter, 'to_mcnp') else str(parameter)
            for parameter in self.parameters
        )

        source = f'{number_str} {transform_str} {self.mnemonic.to_mcnp()} {parameter_str}'

        return _parser.Postprocessor.add_continuation_lines(source)
