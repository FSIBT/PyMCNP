import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KsenOption_Ein(_option.KsenOption_, keyword='ein'):
    """
    Represents INP data card data option ein options.

    Attributes:
        energies: List of ranges for incident energies.
    """

    _REGEX = re.compile(r'\Aein(( \S+)+)\Z')

    def __init__(self, energies: tuple[types.Real]):
        """
        Initializes ``KsenOption_Ein``.

        Parameters:
            energies: List of ranges for incident energies.

        Returns:
            ``KsenOption_Ein``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if energies is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, energies)

        self.value: typing.Final[tuple[any]] = types._Tuple([energies])
        self.energies: typing.Final[tuple[types.Real]] = energies

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KsenOption_Ein`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KsenOption_Ein``.

        Raises:
            McnpError: SYNTAX_KSEN_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KsenOption_Ein._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_KSEN_OPTION, source)

        energies = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return KsenOption_Ein(energies)
