import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Axs(_option.SdefOption_, keyword='axs'):
    """
    Represents INP data card data option axs options.

    Attributes:
        x: Reference vector for EXT and RAD x-component.
        y: Reference vector for EXT and RAD y-component.
        z: Reference vector for EXT and RAD z-component.
    """

    _REGEX = re.compile(r'\Aaxs( \S+)( \S+)( \S+)\Z')

    def __init__(self, x: types.Real, y: types.Real, z: types.Real):
        """
        Initializes ``SdefOption_Axs``.

        Parameters:
            x: Reference vector for EXT and RAD x-component.
            y: Reference vector for EXT and RAD y-component.
            z: Reference vector for EXT and RAD z-component.

        Returns:
            ``SdefOption_Axs``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if x is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, x)
        if y is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, y)
        if z is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, z)

        self.value: typing.Final[tuple[any]] = types._Tuple([x, y, z])
        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Axs`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Axs``.

        Raises:
            McnpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Axs._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SDEF_OPTION, source)

        x = types.Real.from_mcnp(tokens[1])
        y = types.Real.from_mcnp(tokens[2])
        z = types.Real.from_mcnp(tokens[3])

        return SdefOption_Axs(x, y, z)
