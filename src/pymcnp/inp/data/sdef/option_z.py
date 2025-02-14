import re
import typing


from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Z(_option.SdefOption_, keyword='z'):
    """
    Represents INP data card data option z options.

    Attributes:
        z_coordinate: Z-cordinate of position.
    """

    _REGEX = re.compile(r'\Az( \S+)\Z')

    def __init__(self, z_coordinate: types.Real):
        """
        Initializes ``SdefOption_Z``.

        Parameters:
            z_coordinate: Z-cordinate of position.

        Returns:
            ``SdefOption_Z``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if z_coordinate is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, z_coordinate)

        self.value: typing.Final[tuple[any]] = types._Tuple([z_coordinate])
        self.z_coordinate: typing.Final[types.Real] = z_coordinate

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Z`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Z``.

        Raises:
            McnpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Z._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SDEF_OPTION, source)

        z_coordinate = types.Real.from_mcnp(tokens[1])

        return SdefOption_Z(z_coordinate)
