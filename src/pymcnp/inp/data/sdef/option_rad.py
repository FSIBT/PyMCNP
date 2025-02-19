import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Rad(_option.SdefOption_, keyword='rad'):
    """
    Represents INP data card data option rad options.

    Attributes:
        radial_distance: Radial distance fo the position from POS or AXS.
    """

    _REGEX = re.compile(r'\Arad( \S+)\Z')

    def __init__(self, radial_distance: types.Real):
        """
        Initializes ``SdefOption_Rad``.

        Parameters:
            radial_distance: Radial distance fo the position from POS or AXS.

        Returns:
            ``SdefOption_Rad``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if radial_distance is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, radial_distance)

        self.value: typing.Final[tuple[any]] = types._Tuple([radial_distance])
        self.radial_distance: typing.Final[types.Real] = radial_distance

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Rad`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Rad``.

        Raises:
            InpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Rad._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        radial_distance = types.Real.from_mcnp(tokens[1])

        return SdefOption_Rad(radial_distance)
