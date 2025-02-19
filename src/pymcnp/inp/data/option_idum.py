import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Idum(_option.DataOption_, keyword='idum'):
    """
    Represents INP data card idum options.

    Attributes:
        intergers: Integer array.
    """

    _REGEX = re.compile(r'\Aidum(( \S+)+)\Z')

    def __init__(self, intergers: tuple[types.Integer]):
        """
        Initializes ``DataOption_Idum``.

        Parameters:
            intergers: Integer array.

        Returns:
            ``DataOption_Idum``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if intergers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, intergers)

        self.value: typing.Final[tuple[any]] = types._Tuple([intergers])
        self.intergers: typing.Final[tuple[types.Integer]] = intergers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Idum`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Idum``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Idum._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        intergers = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return DataOption_Idum(intergers)
