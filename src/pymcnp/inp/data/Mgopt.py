import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Mgopt(DataOption):
    """
    Represents INP mgopt elements.

    Attributes:
        mcal: Problem type setting.
        igm: Total number of energy groups for all kinds of particle.
        iplt: Weight windows usage indicator.
        iab: Adjoint biasing for adjoint problems contorls.
        icw: Name of the reference cell for generated weight windows.
        fnw: Normalization value for generated weight windows.
        rim: Generated weight windows compression limit.
    """

    _ATTRS = {
        'mcal': types.String,
        'igm': types.IntegerOrJump,
        'iplt': types.IntegerOrJump,
        'iab': types.IntegerOrJump,
        'icw': types.IntegerOrJump,
        'fnw': types.RealOrJump,
        'rim': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Amgopt( {types.String._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        mcal: types.String,
        igm: types.IntegerOrJump,
        iplt: types.IntegerOrJump,
        iab: types.IntegerOrJump,
        icw: types.IntegerOrJump,
        fnw: types.RealOrJump,
        rim: types.RealOrJump,
    ):
        """
        Initializes ``Mgopt``.

        Parameters:
            mcal: Problem type setting.
            igm: Total number of energy groups for all kinds of particle.
            iplt: Weight windows usage indicator.
            iab: Adjoint biasing for adjoint problems contorls.
            icw: Name of the reference cell for generated weight windows.
            fnw: Normalization value for generated weight windows.
            rim: Generated weight windows compression limit.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if mcal is None or mcal not in {'f', 'a'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, mcal)
        if igm is None or not (igm >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, igm)
        if iplt is None or not (iplt == 0 or iplt == 1 or iplt == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, iplt)
        if iab is None or not (iab == 0 or iab == 1 or iab == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, iab)
        if icw is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, icw)
        if fnw is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fnw)
        if rim is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, rim)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                mcal,
                igm,
                iplt,
                iab,
                icw,
                fnw,
                rim,
            ]
        )

        self.mcal: typing.Final[types.String] = mcal
        self.igm: typing.Final[types.IntegerOrJump] = igm
        self.iplt: typing.Final[types.IntegerOrJump] = iplt
        self.iab: typing.Final[types.IntegerOrJump] = iab
        self.icw: typing.Final[types.IntegerOrJump] = icw
        self.fnw: typing.Final[types.RealOrJump] = fnw
        self.rim: typing.Final[types.RealOrJump] = rim


@dataclasses.dataclass
class MgoptBuilder:
    """
    Builds ``Mgopt``.

    Attributes:
        mcal: Problem type setting.
        igm: Total number of energy groups for all kinds of particle.
        iplt: Weight windows usage indicator.
        iab: Adjoint biasing for adjoint problems contorls.
        icw: Name of the reference cell for generated weight windows.
        fnw: Normalization value for generated weight windows.
        rim: Generated weight windows compression limit.
    """

    mcal: str | types.String
    igm: str | int | types.IntegerOrJump
    iplt: str | int | types.IntegerOrJump
    iab: str | int | types.IntegerOrJump
    icw: str | int | types.IntegerOrJump
    fnw: str | float | types.RealOrJump
    rim: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``MgoptBuilder`` into ``Mgopt``.

        Returns:
            ``Mgopt`` for ``MgoptBuilder``.
        """

        mcal = self.mcal
        if isinstance(self.mcal, types.String):
            mcal = self.mcal
        elif isinstance(self.mcal, str):
            mcal = types.String.from_mcnp(self.mcal)

        igm = self.igm
        if isinstance(self.igm, types.Integer):
            igm = self.igm
        elif isinstance(self.igm, int):
            igm = types.IntegerOrJump(self.igm)
        elif isinstance(self.igm, str):
            igm = types.IntegerOrJump.from_mcnp(self.igm)

        iplt = self.iplt
        if isinstance(self.iplt, types.Integer):
            iplt = self.iplt
        elif isinstance(self.iplt, int):
            iplt = types.IntegerOrJump(self.iplt)
        elif isinstance(self.iplt, str):
            iplt = types.IntegerOrJump.from_mcnp(self.iplt)

        iab = self.iab
        if isinstance(self.iab, types.Integer):
            iab = self.iab
        elif isinstance(self.iab, int):
            iab = types.IntegerOrJump(self.iab)
        elif isinstance(self.iab, str):
            iab = types.IntegerOrJump.from_mcnp(self.iab)

        icw = self.icw
        if isinstance(self.icw, types.Integer):
            icw = self.icw
        elif isinstance(self.icw, int):
            icw = types.IntegerOrJump(self.icw)
        elif isinstance(self.icw, str):
            icw = types.IntegerOrJump.from_mcnp(self.icw)

        fnw = self.fnw
        if isinstance(self.fnw, types.Real):
            fnw = self.fnw
        elif isinstance(self.fnw, float) or isinstance(self.fnw, int):
            fnw = types.RealOrJump(self.fnw)
        elif isinstance(self.fnw, str):
            fnw = types.RealOrJump.from_mcnp(self.fnw)

        rim = self.rim
        if isinstance(self.rim, types.Real):
            rim = self.rim
        elif isinstance(self.rim, float) or isinstance(self.rim, int):
            rim = types.RealOrJump(self.rim)
        elif isinstance(self.rim, str):
            rim = types.RealOrJump.from_mcnp(self.rim)

        return Mgopt(
            mcal=mcal,
            igm=igm,
            iplt=iplt,
            iab=iab,
            icw=icw,
            fnw=fnw,
            rim=rim,
        )
