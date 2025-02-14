import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Imp(_option.DataOption_, keyword='imp'):
    """
    Represents INP data card imp options.

    Attributes:
        importances: Cell importance.
        designator: Data card particle designator.
    """

    _REGEX = re.compile(r'\Aimp:(\S+?)(( \S+)+)\Z')

    def __init__(self, importances: tuple[types.Real], designator: types.Designator):
        """
        Initializes ``DataOption_Imp``.

        Parameters:
            importances: Cell importance.
            designator: Data card particle designator.

        Returns:
            ``DataOption_Imp``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_DESIGNATOR.
        """

        if importances is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, importances)
        if designator is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_DESIGNATOR, designator)

        self.value: typing.Final[tuple[any]] = types._Tuple([importances])
        self.importances: typing.Final[tuple[types.Real]] = importances
        self.designator: typing.Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Imp`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Imp``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Imp._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        designator = types.Designator.from_mcnp(tokens[1])
        importances = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[2])]
        )

        return DataOption_Imp(importances, designator)
