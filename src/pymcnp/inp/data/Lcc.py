import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Lcc(DataOption_, keyword='lcc'):
    """
    Represents INP lcc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'stincl': types.RealOrJump,
        'v0incl': types.RealOrJump,
        'xfoisaincl': types.RealOrJump,
        'npaulincl': types.IntegerOrJump,
        'nosurfincl': types.IntegerOrJump,
        'ecutincl': types.RealOrJump,
        'ebankincl': types.RealOrJump,
        'ebankabia': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Alcc( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        stincl: types.RealOrJump,
        v0incl: types.RealOrJump,
        xfoisaincl: types.RealOrJump,
        npaulincl: types.IntegerOrJump,
        nosurfincl: types.IntegerOrJump,
        ecutincl: types.RealOrJump,
        ebankincl: types.RealOrJump,
        ebankabia: types.RealOrJump,
    ):
        """
        Initializes ``Lcc``.

        Parameters:
            stincl: Rescaling factor of the cascade duration.
            v0incl: Potential depth.
            xfoisaincl: Maximum impact parameter for Pauli blocking.
            npaulincl: Pauli blocking parameter setting.
            nosurfincl: Difuse nuclear surface based on Wood-Saxon density setting.
            ecutincl: Bertini model energy below this energy.
            ebankincl: INCL bank particles below this energy.
            ebankabia: ABLA bank particles below this energy.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if stincl is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, stincl)
        if v0incl is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, v0incl)
        if xfoisaincl is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, xfoisaincl)
        if npaulincl is None or not (npaulincl == 0 or npaulincl == -1 or npaulincl == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, npaulincl)
        if nosurfincl is None or not (
            xfoisaincl == -2 or xfoisaincl == -1 or xfoisaincl == 0 or xfoisaincl == 1
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, nosurfincl)
        if ecutincl is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ecutincl)
        if ebankincl is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ebankincl)
        if ebankabia is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ebankabia)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                stincl,
                v0incl,
                xfoisaincl,
                npaulincl,
                nosurfincl,
                ecutincl,
                ebankincl,
                ebankabia,
            ]
        )

        self.stincl: typing.Final[types.RealOrJump] = stincl
        self.v0incl: typing.Final[types.RealOrJump] = v0incl
        self.xfoisaincl: typing.Final[types.RealOrJump] = xfoisaincl
        self.npaulincl: typing.Final[types.IntegerOrJump] = npaulincl
        self.nosurfincl: typing.Final[types.IntegerOrJump] = nosurfincl
        self.ecutincl: typing.Final[types.RealOrJump] = ecutincl
        self.ebankincl: typing.Final[types.RealOrJump] = ebankincl
        self.ebankabia: typing.Final[types.RealOrJump] = ebankabia
