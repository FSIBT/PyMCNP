import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Phys_4(DataOption_, keyword='phys'):
    """
    Represents INP phys_4 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'designator': types.Designator,
        'emax': types.RealOrJump,
        'istrg': types.IntegerOrJump,
        'xmunum': types.IntegerOrJump,
        'xmugam': types.RealOrJump,
        'i_mcs_model': types.IntegerOrJump,
        'i_int_model': types.IntegerOrJump,
        'i_els_model': types.IntegerOrJump,
        'efac': types.RealOrJump,
        'ckvnum': types.RealOrJump,
        'drp': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Aphys:(\S+)( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        designator: types.Designator,
        emax: types.RealOrJump,
        istrg: types.IntegerOrJump,
        xmunum: types.IntegerOrJump,
        xmugam: types.RealOrJump,
        i_mcs_model: types.IntegerOrJump,
        i_int_model: types.IntegerOrJump,
        i_els_model: types.IntegerOrJump,
        efac: types.RealOrJump,
        ckvnum: types.RealOrJump,
        drp: types.RealOrJump,
    ):
        """
        Initializes ``Phys_4``.

        Parameters:
            designator: Data card particle designator.
            emax: Upper energy limit.
            istrg: Charged-particle straggling controls.
            xmunum: Selection of muonic x-ray controls.
            xmugam: Probability for emitting k-shell photon.
            i_mcs_model: Choice of Coulomb scattering model controls.
            i_int_model: Treatment of nuclear interactions controls.
            i_els_model: Treatment of nuclear elastic scattering controls.
            efac: Stopping power energy spacing.
            ckvnum: Crenkov photon emission scalar.
            drp: Lower energy delta-ray cutoff.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if emax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, emax)
        if istrg is None or istrg not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, istrg)
        if xmunum is None or xmunum not in {-1, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, xmunum)
        if xmugam is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, xmugam)
        if i_mcs_model is None or i_mcs_model not in {-1, 0, 1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, i_mcs_model)
        if i_int_model is None or i_int_model not in {-1, 0, 1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, i_int_model)
        if i_els_model is None or i_els_model not in {-1, 0}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, i_els_model)
        if efac is None or not (0.8 <= efac <= 0.99):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, efac)
        if ckvnum is None or not (0 <= ckvnum < 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ckvnum)
        if drp is None or not (drp >= 0 or drp == -1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, drp)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                emax,
                istrg,
                xmunum,
                xmugam,
                i_mcs_model,
                i_int_model,
                i_els_model,
                efac,
                ckvnum,
                drp,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.emax: typing.Final[types.RealOrJump] = emax
        self.istrg: typing.Final[types.IntegerOrJump] = istrg
        self.xmunum: typing.Final[types.IntegerOrJump] = xmunum
        self.xmugam: typing.Final[types.RealOrJump] = xmugam
        self.i_mcs_model: typing.Final[types.IntegerOrJump] = i_mcs_model
        self.i_int_model: typing.Final[types.IntegerOrJump] = i_int_model
        self.i_els_model: typing.Final[types.IntegerOrJump] = i_els_model
        self.efac: typing.Final[types.RealOrJump] = efac
        self.ckvnum: typing.Final[types.RealOrJump] = ckvnum
        self.drp: typing.Final[types.RealOrJump] = drp
