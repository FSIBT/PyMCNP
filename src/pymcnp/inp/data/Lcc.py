import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Lcc(DataOption_, keyword='lcc'):
    """
    Represents INP lcc elements.

    Attributes:
        stincl: Rescaling factor of the cascade duration.
        v0incl: Potential depth.
        xfoisaincl: Maximum impact parameter for Pauli blocking.
        npaulincl: Pauli blocking parameter setting.
        nosurfincl: Difuse nuclear surface based on Wood-Saxon density setting.
        ecutincl: Bertini model energy below this energy.
        ebankincl: INCL bank particles below this energy.
        ebankabia: ABLA bank particles below this energy.
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


@dataclasses.dataclass
class LccBuilder:
    """
    Builds ``Lcc``.

    Attributes:
        stincl: Rescaling factor of the cascade duration.
        v0incl: Potential depth.
        xfoisaincl: Maximum impact parameter for Pauli blocking.
        npaulincl: Pauli blocking parameter setting.
        nosurfincl: Difuse nuclear surface based on Wood-Saxon density setting.
        ecutincl: Bertini model energy below this energy.
        ebankincl: INCL bank particles below this energy.
        ebankabia: ABLA bank particles below this energy.
    """

    stincl: str | float | types.RealOrJump
    v0incl: str | float | types.RealOrJump
    xfoisaincl: str | float | types.RealOrJump
    npaulincl: str | int | types.IntegerOrJump
    nosurfincl: str | int | types.IntegerOrJump
    ecutincl: str | float | types.RealOrJump
    ebankincl: str | float | types.RealOrJump
    ebankabia: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``LccBuilder`` into ``Lcc``.

        Returns:
            ``Lcc`` for ``LccBuilder``.
        """

        if isinstance(self.stincl, types.Real):
            stincl = self.stincl
        elif isinstance(self.stincl, float) or isinstance(self.stincl, int):
            stincl = types.RealOrJump(self.stincl)
        elif isinstance(self.stincl, str):
            stincl = types.RealOrJump.from_mcnp(self.stincl)

        if isinstance(self.v0incl, types.Real):
            v0incl = self.v0incl
        elif isinstance(self.v0incl, float) or isinstance(self.v0incl, int):
            v0incl = types.RealOrJump(self.v0incl)
        elif isinstance(self.v0incl, str):
            v0incl = types.RealOrJump.from_mcnp(self.v0incl)

        if isinstance(self.xfoisaincl, types.Real):
            xfoisaincl = self.xfoisaincl
        elif isinstance(self.xfoisaincl, float) or isinstance(self.xfoisaincl, int):
            xfoisaincl = types.RealOrJump(self.xfoisaincl)
        elif isinstance(self.xfoisaincl, str):
            xfoisaincl = types.RealOrJump.from_mcnp(self.xfoisaincl)

        if isinstance(self.npaulincl, types.Integer):
            npaulincl = self.npaulincl
        elif isinstance(self.npaulincl, int):
            npaulincl = types.IntegerOrJump(self.npaulincl)
        elif isinstance(self.npaulincl, str):
            npaulincl = types.IntegerOrJump.from_mcnp(self.npaulincl)

        if isinstance(self.nosurfincl, types.Integer):
            nosurfincl = self.nosurfincl
        elif isinstance(self.nosurfincl, int):
            nosurfincl = types.IntegerOrJump(self.nosurfincl)
        elif isinstance(self.nosurfincl, str):
            nosurfincl = types.IntegerOrJump.from_mcnp(self.nosurfincl)

        if isinstance(self.ecutincl, types.Real):
            ecutincl = self.ecutincl
        elif isinstance(self.ecutincl, float) or isinstance(self.ecutincl, int):
            ecutincl = types.RealOrJump(self.ecutincl)
        elif isinstance(self.ecutincl, str):
            ecutincl = types.RealOrJump.from_mcnp(self.ecutincl)

        if isinstance(self.ebankincl, types.Real):
            ebankincl = self.ebankincl
        elif isinstance(self.ebankincl, float) or isinstance(self.ebankincl, int):
            ebankincl = types.RealOrJump(self.ebankincl)
        elif isinstance(self.ebankincl, str):
            ebankincl = types.RealOrJump.from_mcnp(self.ebankincl)

        if isinstance(self.ebankabia, types.Real):
            ebankabia = self.ebankabia
        elif isinstance(self.ebankabia, float) or isinstance(self.ebankabia, int):
            ebankabia = types.RealOrJump(self.ebankabia)
        elif isinstance(self.ebankabia, str):
            ebankabia = types.RealOrJump.from_mcnp(self.ebankabia)

        return Lcc(
            stincl=stincl,
            v0incl=v0incl,
            xfoisaincl=xfoisaincl,
            npaulincl=npaulincl,
            nosurfincl=nosurfincl,
            ecutincl=ecutincl,
            ebankincl=ebankincl,
            ebankabia=ebankabia,
        )
