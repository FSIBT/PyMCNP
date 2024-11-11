from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class MultigroupAdjointTransport(Datum):
    """
    ``MultigroupAdjointTransport`` represents INP multigroup adjoint transport
    option data cards.

    ``MultigroupAdjointTransport`` inherits attributes from ``Datum``. It
    represents the INP multigroup adjoint transport option data card syntax
    element.

    Attributes:
        mcal: Problem kind setting.
        igm: Total number of energy groups for all particles.
        iplt: Indicator of how weight windows are to be used.
        isb: Contols adjoint biasing for adjoint problems.
        icw: Nmae of the refreence cell for generated weight windows.
        fnw: Normalization value for gerneated weight windows.
        rim: Compression limit for gerneted weight windows.
    """

    def __init__(
        self,
        mcal: str,
        igm: types.McnpInteger,
        iplt: types.McnpInteger,
        isb: types.McnpInteger,
        icw: types.McnpInteger,
        fnw: types.McnpInteger,
        rim: types.McnpInteger,
    ):
        """
        ``__init__`` initializes ``MultigroupAdjointTransport``.

        Parameters:
            mcal: Problem kind setting.
            igm: Total number of energy groups for all particles.
            iplt: Indicator of how weight windows are to be used.
            isb: Contols adjoint biasing for adjoint problems.
            icw: Nmae of the refreence cell for generated weight windows.
            fnw: Normalization value for gerneated weight windows.
            rim: Compression limit for gerneted weight windows.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if mcal is None or not (mcal == 'f' or mcal == 'a'):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if igm is None or not (igm != 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if iplt is None or iplt not in {0, 1, 2}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if isb is None or isb not in {0, 1, 2}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if icw is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if fnw is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if rim is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'mgopt')
        self.mnemonic = DatumMnemonic.MULTIGROUP_ADJOINT_TRANSPORT
        self.parameters = (mcal, igm, iplt, isb, icw, fnw, rim)

        self.mcal = mcal
        self.igm = igm
        self.iplt = iplt
        self.isb = isb
        self.icw = icw
        self.fnw = fnw
        self.rim = rim
