import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Pd(_option.CellOption_, keyword='pd'):
    """
    Represents INP cell card pd options.

    Attributes:
        probability: Cell probability of DXTRAN contribution.
        suffix: Cell option suffix.
    """

    _REGEX = re.compile(r'\Apd(\d+?)( \S+)\Z')

    def __init__(self, probability: types.Real, suffix: types.Integer):
        """
        Initializes ``CellOption_Pd``.

        Parameters:
            probability: Cell probability of DXTRAN contribution.
            suffix: Cell option suffix.

        Returns:
            ``CellOption_Pd``.

        Raises:
            McnpError: SEMANTICS_CELL_OPTION_VALUE.
            McnpError: SEMANTICS_CELL_OPTION_SUFFIX.
        """

        if probability is None or not (0 <= probability <= 1):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, probability)
        if suffix is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_SUFFIX, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([probability])
        self.probability: typing.Final[types.Real] = probability
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Pd`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Pd``.

        Raises:
            McnpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Pd._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_CELL_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        probability = types.Real.from_mcnp(tokens[2])

        return CellOption_Pd(probability, suffix)
