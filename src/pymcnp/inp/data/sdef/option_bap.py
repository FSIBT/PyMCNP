import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Bap(_option.SdefOption_, keyword='bap'):
    """
    Represents INP data card data option bap options.

    Attributes:
        ba1: Beam aperture half-width in the x transverse direction.
        ba2: Beam aperture half-width in the y transverse direction.
        u: Unused, arrbirary value.
    """

    _REGEX = re.compile(r'\Abap( \S+)( \S+)( \S+)\Z')

    def __init__(self, ba1: types.Real, ba2: types.Real, u: types.Real):
        """
        Initializes ``SdefOption_Bap``.

        Parameters:
            ba1: Beam aperture half-width in the x transverse direction.
            ba2: Beam aperture half-width in the y transverse direction.
            u: Unused, arrbirary value.

        Returns:
            ``SdefOption_Bap``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if ba1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, ba1)
        if ba2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, ba2)
        if u is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, u)

        self.value: typing.Final[tuple[any]] = types._Tuple([ba1, ba2, u])
        self.ba1: typing.Final[types.Real] = ba1
        self.ba2: typing.Final[types.Real] = ba2
        self.u: typing.Final[types.Real] = u

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Bap`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Bap``.

        Raises:
            McnpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Bap._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SDEF_OPTION, source)

        ba1 = types.Real.from_mcnp(tokens[1])
        ba2 = types.Real.from_mcnp(tokens[2])
        u = types.Real.from_mcnp(tokens[3])

        return SdefOption_Bap(ba1, ba2, u)
