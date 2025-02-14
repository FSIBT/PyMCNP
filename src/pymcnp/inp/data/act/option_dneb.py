import re
import typing

from . import dneb
from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class ActOption_Dneb(_option.ActOption_, keyword='dneb'):
    """
    Represents INP data card data option dneb options.

    Attributes:
        biases: Delayed neutron energy biases.
    """

    _REGEX = re.compile(r'\Adneb((( \S+)( \S+))+)\Z')

    def __init__(self, biases: tuple[dneb.DnebEntry_Bias]):
        """
        Initializes ``ActOption_Dneb``.

        Parameters:
            biases: Delayed neutron energy biases.

        Returns:
            ``ActOption_Dneb``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if biases is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, biases)

        self.value: typing.Final[tuple[any]] = types._Tuple([biases])
        self.biases: typing.Final[tuple[dneb.DnebEntry_Bias]] = biases

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``ActOption_Dneb`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``ActOption_Dneb``.

        Raises:
            McnpError: SYNTAX_ACT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = ActOption_Dneb._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_ACT_OPTION, source)

        biases = types._Tuple(
            [
                dneb.DnebEntry_Bias.from_mcnp(token[0])
                for token in dneb.DnebEntry_Bias._REGEX.finditer(tokens[1])
            ]
        )

        return ActOption_Dneb(biases)
