import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Ara(_option.SdefOption_, keyword='ara'):
    """
    Represents INP data card data option ara options.

    Attributes:
        area: Area of surface.
    """

    _REGEX = re.compile(r'\Aara( \S+)\Z')

    def __init__(self, area: types.Real):
        """
        Initializes ``SdefOption_Ara``.

        Parameters:
            area: Area of surface.

        Returns:
            ``SdefOption_Ara``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if area is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, area)

        self.value: typing.Final[tuple[any]] = types._Tuple([area])
        self.area: typing.Final[types.Real] = area

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Ara`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Ara``.

        Raises:
            InpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Ara._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        area = types.Real.from_mcnp(tokens[1])

        return SdefOption_Ara(area)
