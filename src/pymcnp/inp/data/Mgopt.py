import re
import copy
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

    _KEYWORD = 'mgopt'

    _ATTRS = {
        'mcal': types.String,
        'igm': types.Integer,
        'iplt': types.Integer,
        'iab': types.Integer,
        'icw': types.Integer,
        'fnw': types.Real,
        'rim': types.Real,
    }

    _REGEX = re.compile(
        rf'\Amgopt( {types.String._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        mcal: types.String,
        igm: types.Integer,
        iplt: types.Integer = None,
        iab: types.Integer = None,
        icw: types.Integer = None,
        fnw: types.Real = None,
        rim: types.Real = None,
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
        if igm is None or not (igm.value >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, igm)
        if iplt is not None and not (iplt.value == 0 or iplt.value == 1 or iplt.value == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, iplt)
        if iab is not None and not (iab.value == 0 or iab.value == 1 or iab.value == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, iab)

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
        self.igm: typing.Final[types.Integer] = igm
        self.iplt: typing.Final[types.Integer] = iplt
        self.iab: typing.Final[types.Integer] = iab
        self.icw: typing.Final[types.Integer] = icw
        self.fnw: typing.Final[types.Real] = fnw
        self.rim: typing.Final[types.Real] = rim


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
    igm: str | int | types.Integer
    iplt: str | int | types.Integer = None
    iab: str | int | types.Integer = None
    icw: str | int | types.Integer = None
    fnw: str | float | types.Real = None
    rim: str | float | types.Real = None

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
            igm = types.Integer(self.igm)
        elif isinstance(self.igm, str):
            igm = types.Integer.from_mcnp(self.igm)

        iplt = self.iplt
        if isinstance(self.iplt, types.Integer):
            iplt = self.iplt
        elif isinstance(self.iplt, int):
            iplt = types.Integer(self.iplt)
        elif isinstance(self.iplt, str):
            iplt = types.Integer.from_mcnp(self.iplt)

        iab = self.iab
        if isinstance(self.iab, types.Integer):
            iab = self.iab
        elif isinstance(self.iab, int):
            iab = types.Integer(self.iab)
        elif isinstance(self.iab, str):
            iab = types.Integer.from_mcnp(self.iab)

        icw = self.icw
        if isinstance(self.icw, types.Integer):
            icw = self.icw
        elif isinstance(self.icw, int):
            icw = types.Integer(self.icw)
        elif isinstance(self.icw, str):
            icw = types.Integer.from_mcnp(self.icw)

        fnw = self.fnw
        if isinstance(self.fnw, types.Real):
            fnw = self.fnw
        elif isinstance(self.fnw, float) or isinstance(self.fnw, int):
            fnw = types.Real(self.fnw)
        elif isinstance(self.fnw, str):
            fnw = types.Real.from_mcnp(self.fnw)

        rim = self.rim
        if isinstance(self.rim, types.Real):
            rim = self.rim
        elif isinstance(self.rim, float) or isinstance(self.rim, int):
            rim = types.Real(self.rim)
        elif isinstance(self.rim, str):
            rim = types.Real.from_mcnp(self.rim)

        return Mgopt(
            mcal=mcal,
            igm=igm,
            iplt=iplt,
            iab=iab,
            icw=icw,
            fnw=fnw,
            rim=rim,
        )

    @staticmethod
    def unbuild(ast: Mgopt):
        """
        Unbuilds ``Mgopt`` into ``MgoptBuilder``

        Returns:
            ``MgoptBuilder`` for ``Mgopt``.
        """

        return Mgopt(
            mcal=copy.deepcopy(ast.mcal),
            igm=copy.deepcopy(ast.igm),
            iplt=copy.deepcopy(ast.iplt),
            iab=copy.deepcopy(ast.iab),
            icw=copy.deepcopy(ast.icw),
            fnw=copy.deepcopy(ast.fnw),
            rim=copy.deepcopy(ast.rim),
        )
