import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Sp0(_option.DataOption_, keyword='sp'):
    """
    Represents INP data card sp_0 options.

    Attributes:
        option: Probability kind setting.
        probabilities: Particle source probabilities.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Asp(\d+?)( \S+)(( \S+)+)\Z')

    def __init__(
        self, option: types.String, probabilities: tuple[types.Real], suffix: types.Integer
    ):
        """
        Initializes ``DataOption_Sp0``.

        Parameters:
            option: Probability kind setting.
            probabilities: Particle source probabilities.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Sp0``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if option is None or option not in {'d', 'c', 'v', 'w'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, option)
        if probabilities is None or not (
            filter(lambda entry: not (0 <= entry <= 1), probabilities)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, probabilities)
        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([option, probabilities])
        self.option: typing.Final[types.String] = option
        self.probabilities: typing.Final[tuple[types.Real]] = probabilities
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Sp0`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Sp0``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Sp0._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        option = types.String.from_mcnp(tokens[2])
        probabilities = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[3])]
        )

        return DataOption_Sp0(option, probabilities, suffix)
