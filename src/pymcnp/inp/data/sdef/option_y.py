import re
import typing


from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Y(_option.SdefOption_, keyword='y'):
    """
    Represents INP data card data option y options.

    Attributes:
        y_coordinate: Y-cordinate of position.
    """

    _REGEX = re.compile(r'\Ay( \S+)\Z')

    def __init__(self, y_coordinate: types.Real):
        """
        Initializes ``SdefOption_Y``.

        Parameters:
            y_coordinate: Y-cordinate of position.

        Returns:
            ``SdefOption_Y``.

        Raises:
            InpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if y_coordinate is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_DATA_OPTION_VALUE, y_coordinate)

        self.value: typing.Final[tuple[any]] = types._Tuple([y_coordinate])
        self.y_coordinate: typing.Final[types.Real] = y_coordinate

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Y`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Y``.

        Raises:
            InpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Y._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_SDEF_OPTION, source)

        y_coordinate = types.Real.from_mcnp(tokens[1])

        return SdefOption_Y(y_coordinate)
