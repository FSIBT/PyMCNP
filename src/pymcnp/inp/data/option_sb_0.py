import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Sb0(_option.DataOption_, keyword='sb'):
    """
    Represents INP data card sb_0 options.

    Attributes:
        option: Bias kind setting.
        biases: Particle source biases.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Asb(\d+?)( \S+)(( \S+)+)\Z')

    def __init__(self, option: types.String, biases: tuple[types.Real], suffix: types.Integer):
        """
        Initializes ``DataOption_Sb0``.

        Parameters:
            option: Bias kind setting.
            biases: Particle source biases.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Sb0``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_SUFFIX.
        """

        if option is None or option not in {'d', 'c', 'v', 'w'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, option)
        if biases is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, biases)
        if suffix is None or not (1 <= suffix <= 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_SUFFIX, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([option, biases])
        self.option: typing.Final[types.String] = option
        self.biases: typing.Final[tuple[types.Real]] = biases
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Sb0`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Sb0``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Sb0._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        option = types.String.from_mcnp(tokens[2])
        biases = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[3])]
        )

        return DataOption_Sb0(option, biases, suffix)
