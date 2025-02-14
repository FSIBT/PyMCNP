import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SsrOption_Pty(_option.SsrOption_, keyword='pty'):
    """
    Represents INP data card data option pty options.

    Attributes:
        particles: Tuple of designators.
    """

    _REGEX = re.compile(r'\Apty(( \S+)+)\Z')

    def __init__(self, particles: tuple[types.Designator]):
        """
        Initializes ``SsrOption_Pty``.

        Parameters:
            particles: Tuple of designators.

        Returns:
            ``SsrOption_Pty``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if particles is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, particles)

        self.value: typing.Final[tuple[any]] = types._Tuple([particles])
        self.particles: typing.Final[tuple[types.Designator]] = particles

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SsrOption_Pty`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SsrOption_Pty``.

        Raises:
            McnpError: SYNTAX_SSR_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SsrOption_Pty._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SSR_OPTION, source)

        particles = types._Tuple(
            [types.Designator.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return SsrOption_Pty(particles)
