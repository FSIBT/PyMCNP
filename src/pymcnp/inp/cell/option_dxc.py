import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Dxc(_option.CellOption_, keyword='dxc'):
    """
    Represents INP cell card dxc options.

    Attributes:
        probability: Cell probability of DXTRAN contribution.
        suffix: Cell option suffix.
        designator: Cell particle designator.
    """

    _REGEX = re.compile(r'\Adxc(\d+?):(\S+?)( \S+)\Z')

    def __init__(
        self, probability: types.Real, suffix: types.Integer, designator: types.Designator
    ):
        """
        Initializes ``CellOption_Dxc``.

        Parameters:
            probability: Cell probability of DXTRAN contribution.
            suffix: Cell option suffix.
            designator: Cell particle designator.

        Returns:
            ``CellOption_Dxc``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if probability is None or not (0 <= probability <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, probability)
        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)

        self.value: typing.Final[tuple[any]] = types._Tuple([probability])
        self.probability: typing.Final[types.Real] = probability
        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Dxc`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Dxc``.

        Raises:
            InpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Dxc._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        designator = types.Designator.from_mcnp(tokens[2])
        probability = types.Real.from_mcnp(tokens[3])

        return CellOption_Dxc(probability, suffix, designator)
