import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Mgopt(DataOption_, keyword='mgopt'):
    """
    Represents INP mgopt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

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
        rf'mgopt( {types.String._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
    )

    def __init__(
        self,
        mcal: types.String,
        igm: types.Integer,
        iplt: types.Integer,
        iab: types.Integer,
        icw: types.Integer,
        fnw: types.Real,
        rim: types.Real,
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if mcal is None or mcal not in {'f', 'a'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, mcal)
        if igm is None or not (igm >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, igm)
        if iplt is None or not (iplt == 0 or iplt == 1 or iplt == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, iplt)
        if iab is None or not (iab == 0 or iab == 1 or iab == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, iab)
        if icw is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, icw)
        if fnw is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fnw)
        if rim is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, rim)

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
