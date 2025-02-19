import re
import typing


from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_X(_option.SdefOption_, keyword='x'):
    """
    Represents INP data card data option x options.

    Attributes:
        x_coordinate: X-cordinate of position.
    """

    _REGEX = re.compile(r'\Ax( \S+)\Z')

    def __init__(self, x_coordinate: types.Real):
        """
        Initializes ``SdefOption_X``.

        Parameters:
            x_coordinate: X-cordinate of position.

        Returns:
            ``SdefOption_X``.

        Raises:
            InpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if x_coordinate is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_DATA_OPTION_VALUE, x_coordinate)

        self.value: typing.Final[tuple[any]] = types._Tuple([x_coordinate])
        self.x_coordinate: typing.Final[types.Real] = x_coordinate

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_X`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_X``.

        Raises:
            InpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_X._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_SDEF_OPTION, source)

        x_coordinate = types.Real.from_mcnp(tokens[1])

        return SdefOption_X(x_coordinate)
