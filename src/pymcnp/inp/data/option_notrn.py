import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Notrn(_option.DataOption_, keyword='notrn'):
    """
    Represents INP data card notrn options.

    Attributes:

    """

    _REGEX = re.compile(r'\Anotrn\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``DataOption_Notrn``.

        Parameters:


        Returns:
            ``DataOption_Notrn``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([])

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Notrn`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Notrn``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Notrn._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        return DataOption_Notrn()
