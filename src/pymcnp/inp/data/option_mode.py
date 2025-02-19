import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Mode(_option.DataOption_, keyword='mode'):
    """
    Represents INP data card mode options.

    Attributes:
        particles: Tuple of particle designators.
    """

    _REGEX = re.compile(r'\Amode(( \S+)+)\Z')

    def __init__(self, particles: tuple[types.Designator]):
        """
        Initializes ``DataOption_Mode``.

        Parameters:
            particles: Tuple of particle designators.

        Returns:
            ``DataOption_Mode``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if particles is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, particles)

        self.value: typing.Final[tuple[any]] = types._Tuple([particles])
        self.particles: typing.Final[tuple[types.Designator]] = particles

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Mode`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Mode``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Mode._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        particles = types._Tuple(
            [types.Designator.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return DataOption_Mode(particles)
