import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Thtme(_option.DataOption_, keyword='thtme'):
    """
    Represents INP data card thtme options.

    Attributes:
        times: Tuple of times when thermal temperatures are specified.
    """

    _REGEX = re.compile(r'\Athtme(( \S+)+)\Z')

    def __init__(self, times: tuple[types.Real]):
        """
        Initializes ``DataOption_Thtme``.

        Parameters:
            times: Tuple of times when thermal temperatures are specified.

        Returns:
            ``DataOption_Thtme``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if times is None or not (filter(lambda entry: not (entry <= 99), times)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, times)

        self.value: typing.Final[tuple[any]] = types._Tuple([times])
        self.times: typing.Final[tuple[types.Real]] = times

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Thtme`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Thtme``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Thtme._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        times = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return DataOption_Thtme(times)
