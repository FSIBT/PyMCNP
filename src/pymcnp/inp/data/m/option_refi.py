import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MOption_Refi(_option.MOption_, keyword='refi'):
    """
    Represents INP data card data option refi options.

    Attributes:
        refractive_index: Refractive index constant.
    """

    _REGEX = re.compile(r'\Arefi( \S+)\Z')

    def __init__(self, refractive_index: types.Real):
        """
        Initializes ``MOption_Refi``.

        Parameters:
            refractive_index: Refractive index constant.

        Returns:
            ``MOption_Refi``.

        Raises:
            InpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if refractive_index is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_DATA_OPTION_VALUE, refractive_index)

        self.value: typing.Final[tuple[any]] = types._Tuple([refractive_index])
        self.refractive_index: typing.Final[types.Real] = refractive_index

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MOption_Refi`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MOption_Refi``.

        Raises:
            InpError: SYNTAX_M_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MOption_Refi._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_M_OPTION, source)

        refractive_index = types.Real.from_mcnp(tokens[1])

        return MOption_Refi(refractive_index)
