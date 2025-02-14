import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Sd(_option.DataOption_, keyword='sd'):
    """
    Represents INP data card sd options.

    Attributes:
        information: Area, volume, or mass by segmented, surface/cell.
    """

    _REGEX = re.compile(r'\Asd(( \S+)+)\Z')

    def __init__(self, information: tuple[types.Real]):
        """
        Initializes ``DataOption_Sd``.

        Parameters:
            information: Area, volume, or mass by segmented, surface/cell.

        Returns:
            ``DataOption_Sd``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if information is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, information)

        self.value: typing.Final[tuple[any]] = types._Tuple([information])
        self.information: typing.Final[tuple[types.Real]] = information

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Sd`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Sd``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Sd._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        information = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return DataOption_Sd(information)
