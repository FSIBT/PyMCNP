import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KsenOption_Cos(_option.KsenOption_, keyword='cos'):
    """
    Represents INP data card data option cos options.

    Attributes:
        cosines: Range of direction-change cosines.
    """

    _REGEX = re.compile(r'\Acos(( \S+)+)\Z')

    def __init__(self, cosines: tuple[types.Real]):
        """
        Initializes ``KsenOption_Cos``.

        Parameters:
            cosines: Range of direction-change cosines.

        Returns:
            ``KsenOption_Cos``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if cosines is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cosines)

        self.value: typing.Final[tuple[any]] = types._Tuple([cosines])
        self.cosines: typing.Final[tuple[types.Real]] = cosines

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KsenOption_Cos`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KsenOption_Cos``.

        Raises:
            InpError: SYNTAX_KSEN_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KsenOption_Cos._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        cosines = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return KsenOption_Cos(cosines)
