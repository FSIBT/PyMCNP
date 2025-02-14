import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PtracOption_Nps(_option.PtracOption_, keyword='nps'):
    """
    Represents INP data card data option nps options.

    Attributes:
        particles: Sets the range of particle histories for which events will be output.
    """

    _REGEX = re.compile(r'\Anps(( \S+)+)\Z')

    def __init__(self, particles: tuple[types.Integer]):
        """
        Initializes ``PtracOption_Nps``.

        Parameters:
            particles: Sets the range of particle histories for which events will be output.

        Returns:
            ``PtracOption_Nps``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if particles is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, particles)

        self.value: typing.Final[tuple[any]] = types._Tuple([particles])
        self.particles: typing.Final[tuple[types.Integer]] = particles

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PtracOption_Nps`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PtracOption_Nps``.

        Raises:
            McnpError: SYNTAX_PTRAC_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PtracOption_Nps._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_PTRAC_OPTION, source)

        particles = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return PtracOption_Nps(particles)
