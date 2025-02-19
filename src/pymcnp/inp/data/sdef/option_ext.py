import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Ext(_option.SdefOption_, keyword='ext'):
    """
    Represents INP data card data option ext options.

    Attributes:
        distance_cosine: Distance for POS along AXS or Cosine of angle from AXS.
    """

    _REGEX = re.compile(r'\Aext( \S+)\Z')

    def __init__(self, distance_cosine: types.Real):
        """
        Initializes ``SdefOption_Ext``.

        Parameters:
            distance_cosine: Distance for POS along AXS or Cosine of angle from AXS.

        Returns:
            ``SdefOption_Ext``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if distance_cosine is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, distance_cosine)

        self.value: typing.Final[tuple[any]] = types._Tuple([distance_cosine])
        self.distance_cosine: typing.Final[types.Real] = distance_cosine

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Ext`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Ext``.

        Raises:
            InpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Ext._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        distance_cosine = types.Real.from_mcnp(tokens[1])

        return SdefOption_Ext(distance_cosine)
