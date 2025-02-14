import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Vec(_option.SdefOption_, keyword='vec'):
    """
    Represents INP data card data option vec options.

    Attributes:
        x: Reference vector for DIR x-component.
        y: Reference vector for DIR y-component.
        z: Reference vector for DIR z-component.
    """

    _REGEX = re.compile(r'\Avec( \S+)( \S+)( \S+)\Z')

    def __init__(self, x: types.Real, y: types.Real, z: types.Real):
        """
        Initializes ``SdefOption_Vec``.

        Parameters:
            x: Reference vector for DIR x-component.
            y: Reference vector for DIR y-component.
            z: Reference vector for DIR z-component.

        Returns:
            ``SdefOption_Vec``.

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
        Generates ``SdefOption_Vec`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Vec``.

        Raises:
            McnpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Vec._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SDEF_OPTION, source)

        x = types.Real.from_mcnp(tokens[1])
        y = types.Real.from_mcnp(tokens[2])
        z = types.Real.from_mcnp(tokens[3])

        return SdefOption_Vec(x, y, z)
