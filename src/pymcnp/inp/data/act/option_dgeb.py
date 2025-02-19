import re
import typing

from . import dgeb
from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class ActOption_Dgeb(_option.ActOption_, keyword='dgeb'):
    """
    Represents INP data card data option dgeb options.

    Attributes:
        biases: Delayed neutron energy biases.
    """

    _REGEX = re.compile(r'\Adgeb((( \S+)( \S+))+)\Z')

    def __init__(self, biases: tuple[dgeb.DgebEntry_Bias]):
        """
        Initializes ``ActOption_Dgeb``.

        Parameters:
            biases: Delayed neutron energy biases.

        Returns:
            ``ActOption_Dgeb``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if biases is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, biases)

        self.value: typing.Final[tuple[any]] = types._Tuple([biases])
        self.biases: typing.Final[tuple[dgeb.DgebEntry_Bias]] = biases

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``ActOption_Dgeb`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``ActOption_Dgeb``.

        Raises:
            InpError: SYNTAX_ACT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = ActOption_Dgeb._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        biases = types._Tuple(
            [
                dgeb.DgebEntry_Bias.from_mcnp(token[0])
                for token in dgeb.DgebEntry_Bias._REGEX.finditer(tokens[1])
            ]
        )

        return ActOption_Dgeb(biases)
