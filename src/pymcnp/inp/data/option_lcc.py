import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Lcc(_option.DataOption_, keyword='lcc'):
    """
    Represents INP data card lcc options.

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

    _REGEX = re.compile(r'\Alcc( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(
        self,
        stincl: types.Real,
        v0incl: types.Real,
        xfoisaincl: types.Real,
        npaulincl: types.Integer,
        nosurfincl: types.Integer,
        ecutincl: types.Real,
        ebankincl: types.Real,
        ebankabia: types.Real,
    ):
        """
        Initializes ``DataOption_Lcc``.

        Parameters:
            stincl: Rescaling factor of the cascade duration.
            v0incl: Potential depth.
            xfoisaincl: Maximum impact parameter for Pauli blocking.
            npaulincl: Pauli blocking parameter setting.
            nosurfincl: Difuse nuclear surface based on Wood-Saxon density setting.
            ecutincl: Bertini model energy below this energy.
            ebankincl: INCL bank particles below this energy.
            ebankabia: ABLA bank particles below this energy.

        Returns:
            ``DataOption_Lcc``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if stincl is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, stincl)
        if v0incl is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, v0incl)
        if xfoisaincl is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, xfoisaincl)
        if npaulincl is None or not (npaulincl == 0 or npaulincl == -1 or npaulincl == 1):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, npaulincl)
        if nosurfincl is None or not (
            xfoisaincl == -2 or xfoisaincl == -1 or xfoisaincl == 0 or xfoisaincl == 1
        ):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, nosurfincl)
        if ecutincl is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, ecutincl)
        if ebankincl is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, ebankincl)
        if ebankabia is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, ebankabia)

        self.value: typing.Final[tuple[any]] = types._Tuple(
            [stincl, v0incl, xfoisaincl, npaulincl, nosurfincl, ecutincl, ebankincl, ebankabia]
        )
        self.stincl: typing.Final[types.Real] = stincl
        self.v0incl: typing.Final[types.Real] = v0incl
        self.xfoisaincl: typing.Final[types.Real] = xfoisaincl
        self.npaulincl: typing.Final[types.Integer] = npaulincl
        self.nosurfincl: typing.Final[types.Integer] = nosurfincl
        self.ecutincl: typing.Final[types.Real] = ecutincl
        self.ebankincl: typing.Final[types.Real] = ebankincl
        self.ebankabia: typing.Final[types.Real] = ebankabia

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Lcc`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Lcc``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Lcc._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        stincl = types.Real.from_mcnp(tokens[1])
        v0incl = types.Real.from_mcnp(tokens[2])
        xfoisaincl = types.Real.from_mcnp(tokens[3])
        npaulincl = types.Integer.from_mcnp(tokens[4])
        nosurfincl = types.Integer.from_mcnp(tokens[5])
        ecutincl = types.Real.from_mcnp(tokens[6])
        ebankincl = types.Real.from_mcnp(tokens[7])
        ebankabia = types.Real.from_mcnp(tokens[8])

        return DataOption_Lcc(
            stincl, v0incl, xfoisaincl, npaulincl, nosurfincl, ecutincl, ebankincl, ebankabia
        )
