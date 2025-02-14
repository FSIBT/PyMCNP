import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KpertOption_Erg(_option.KpertOption_, keyword='erg'):
    """
    Represents INP data card data option erg options.

    Attributes:
        energies: List of energies.
    """

    _REGEX = re.compile(r'\Aerg(( \S+)+)\Z')

    def __init__(self, energies: tuple[types.Real]):
        """
        Initializes ``KpertOption_Erg``.

        Parameters:
            energies: List of energies.

        Returns:
            ``KpertOption_Erg``.

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
        Generates ``KpertOption_Erg`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KpertOption_Erg``.

        Raises:
            McnpError: SYNTAX_KPERT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KpertOption_Erg._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_KPERT_OPTION, source)

        energies = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return KpertOption_Erg(energies)
