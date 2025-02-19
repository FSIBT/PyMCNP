import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Eff(_option.SdefOption_, keyword='eff'):
    """
    Represents INP data card data option eff options.

    Attributes:
        criterion: Rejection efficiency criterion for position sampling.
    """

    _REGEX = re.compile(r'\Aeff( \S+)\Z')

    def __init__(self, criterion: types.Real):
        """
        Initializes ``SdefOption_Eff``.

        Parameters:
            criterion: Rejection efficiency criterion for position sampling.

        Returns:
            ``SdefOption_Eff``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if criterion is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, criterion)

        self.value: typing.Final[tuple[any]] = types._Tuple([criterion])
        self.criterion: typing.Final[types.Real] = criterion

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Eff`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Eff``.

        Raises:
            InpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Eff._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        criterion = types.Real.from_mcnp(tokens[1])

        return SdefOption_Eff(criterion)
