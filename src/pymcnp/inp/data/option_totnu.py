import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Totnu(_option.DataOption_, keyword='totnu'):
    """
    Represents INP data card totnu options.

    Attributes:
        no: Delay fission sampling on/off.
    """

    _REGEX = re.compile(r'\Atotnu( \S+)?\Z')

    def __init__(self, no: types.String = None):
        """
        Initializes ``DataOption_Totnu``.

        Parameters:
            no: Delay fission sampling on/off.

        Returns:
            ``DataOption_Totnu``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if no is not None and not (no == 'no'):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, no)

        self.value: typing.Final[tuple[any]] = types._Tuple([no])
        self.no: typing.Final[types.String] = no

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Totnu`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Totnu``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Totnu._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        no = types.String.from_mcnp(tokens[1]) if tokens[1] else None

        return DataOption_Totnu(no)
