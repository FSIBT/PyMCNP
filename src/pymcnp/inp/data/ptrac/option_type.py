import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PtracOption_Type(_option.PtracOption_, keyword='type'):
    """
    Represents INP data card data option type options.

    Attributes:
        particles: Filters events based on one or more particle types.
    """

    _REGEX = re.compile(r'\Atype(( \S+)+)\Z')

    def __init__(self, particles: tuple[types.Designator]):
        """
        Initializes ``PtracOption_Type``.

        Parameters:
            particles: Filters events based on one or more particle types.

        Returns:
            ``PtracOption_Type``.

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
        Generates ``PtracOption_Type`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PtracOption_Type``.

        Raises:
            McnpError: SYNTAX_PTRAC_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PtracOption_Type._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_PTRAC_OPTION, source)

        particles = types._Tuple(
            [types.Designator.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return PtracOption_Type(particles)
