import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PertOption_Erg(_option.PertOption_, keyword='erg'):
    """
    Represents INP data card data option erg options.

    Attributes:
        energy_lower_bound: Lower bound for energy pertubation.
        energy_upper_bound: Upper bound for energy pertubation.
    """

    _REGEX = re.compile(r'\Aerg( \S+)( \S+)\Z')

    def __init__(self, energy_lower_bound: types.Real, energy_upper_bound: types.Real):
        """
        Initializes ``PertOption_Erg``.

        Parameters:
            energy_lower_bound: Lower bound for energy pertubation.
            energy_upper_bound: Upper bound for energy pertubation.

        Returns:
            ``PertOption_Erg``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if energy_lower_bound is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, energy_lower_bound)
        if energy_upper_bound is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, energy_upper_bound)

        self.value: typing.Final[tuple[any]] = types._Tuple(
            [energy_lower_bound, energy_upper_bound]
        )
        self.energy_lower_bound: typing.Final[types.Real] = energy_lower_bound
        self.energy_upper_bound: typing.Final[types.Real] = energy_upper_bound

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PertOption_Erg`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PertOption_Erg``.

        Raises:
            McnpError: SYNTAX_PERT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PertOption_Erg._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_PERT_OPTION, source)

        energy_lower_bound = types.Real.from_mcnp(tokens[1])
        energy_upper_bound = types.Real.from_mcnp(tokens[2])

        return PertOption_Erg(energy_lower_bound, energy_upper_bound)
