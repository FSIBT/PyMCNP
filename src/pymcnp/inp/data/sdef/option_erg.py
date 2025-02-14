import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Erg(_option.SdefOption_, keyword='erg'):
    """
    Represents INP data card data option erg options.

    Attributes:
        energy: Kinetic energy.
    """

    _REGEX = re.compile(r'\Aerg( \S+)\Z')

    def __init__(self, energy: types.Real):
        """
        Initializes ``SdefOption_Erg``.

        Parameters:
            energy: Kinetic energy.

        Returns:
            ``SdefOption_Erg``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if energy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, energy)

        self.value: typing.Final[tuple[any]] = types._Tuple([energy])
        self.energy: typing.Final[types.Real] = energy

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Erg`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Erg``.

        Raises:
            McnpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Erg._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SDEF_OPTION, source)

        energy = types.Real.from_mcnp(tokens[1])

        return SdefOption_Erg(energy)
