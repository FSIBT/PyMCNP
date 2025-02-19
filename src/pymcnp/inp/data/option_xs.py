import re
import typing

from . import xs
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Xs(_option.DataOption_, keyword='xs'):
    """
    Represents INP data card xs options.

    Attributes:
        weight_ratios: Tuple of atomic weight ratios.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Axs(\d+?)((( \S+)( \S+))+)\Z')

    def __init__(self, weight_ratios: tuple[xs.XsEntry_Substance], suffix: types.Integer):
        """
        Initializes ``DataOption_Xs``.

        Parameters:
            weight_ratios: Tuple of atomic weight ratios.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Xs``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if weight_ratios is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, weight_ratios)
        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([weight_ratios])
        self.weight_ratios: typing.Final[tuple[xs.XsEntry_Substance]] = weight_ratios
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Xs`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Xs``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Xs._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        weight_ratios = types._Tuple(
            [
                xs.XsEntry_Substance.from_mcnp(token[0])
                for token in xs.XsEntry_Substance._REGEX.finditer(tokens[2])
            ]
        )

        return DataOption_Xs(weight_ratios, suffix)
