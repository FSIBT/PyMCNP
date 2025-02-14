import re
import typing

from . import pikmt
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Pikmt(_option.DataOption_, keyword='pikmt'):
    """
    Represents INP data card pikmt options.

    Attributes:
        biases: Biases for proton production.
    """

    _REGEX = re.compile(r'\Apikmt((( \S+)( \S+)((( \S+)( \S+))+))+)\Z')

    def __init__(self, biases: tuple[pikmt.PikmtEntry_Bias]):
        """
        Initializes ``DataOption_Pikmt``.

        Parameters:
            biases: Biases for proton production.

        Returns:
            ``DataOption_Pikmt``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if biases is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, biases)

        self.value: typing.Final[tuple[any]] = types._Tuple([biases])
        self.biases: typing.Final[tuple[pikmt.PikmtEntry_Bias]] = biases

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Pikmt`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Pikmt``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Pikmt._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        biases = types._Tuple(
            [
                pikmt.PikmtEntry_Bias.from_mcnp(token[0])
                for token in pikmt.PikmtEntry_Bias._REGEX.finditer(tokens[1])
            ]
        )

        return DataOption_Pikmt(biases)
