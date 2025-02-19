import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Dxc(_option.DataOption_, keyword='dxc'):
    """
    Represents INP data card dxc options.

    Attributes:
        probabilities: Probability of contribution to DXTRAN.
        suffix: Data card option suffix.
        designator: Data card particle designator.
    """

    _REGEX = re.compile(r'\Adxc(\d+?):(\S+?)(( \S+)+)\Z')

    def __init__(
        self, probabilities: tuple[types.Real], suffix: types.Integer, designator: types.Designator
    ):
        """
        Initializes ``DataOption_Dxc``.

        Parameters:
            probabilities: Probability of contribution to DXTRAN.
            suffix: Data card option suffix.
            designator: Data card particle designator.

        Returns:
            ``DataOption_Dxc``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if probabilities is None or not (
            filter(lambda entry: not (0 <= entry <= 1), probabilities)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, probabilities)
        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)

        self.value: typing.Final[tuple[any]] = types._Tuple([probabilities])
        self.probabilities: typing.Final[tuple[types.Real]] = probabilities
        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Dxc`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Dxc``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Dxc._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        designator = types.Designator.from_mcnp(tokens[2])
        probabilities = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[3])]
        )

        return DataOption_Dxc(probabilities, suffix, designator)
