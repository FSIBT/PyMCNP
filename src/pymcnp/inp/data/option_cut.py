import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Cut(_option.DataOption_, keyword='cut'):
    """
    Represents INP data card cut options.

    Attributes:
        time_cutoff: Time cutoff in shakes.
        energy_cutoff: Lower energy cutoff.
        weight_cutoff1: Weight cutoff #1.
        weight_cutoff2: Weight cutoff #2.
        source_weight: Minimum source weight.
    """

    _REGEX = re.compile(r'\Acut( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(
        self,
        time_cutoff: types.Real,
        energy_cutoff: types.Real,
        weight_cutoff1: types.Real,
        weight_cutoff2: types.Real,
        source_weight: types.Real,
    ):
        """
        Initializes ``DataOption_Cut``.

        Parameters:
            time_cutoff: Time cutoff in shakes.
            energy_cutoff: Lower energy cutoff.
            weight_cutoff1: Weight cutoff #1.
            weight_cutoff2: Weight cutoff #2.
            source_weight: Minimum source weight.

        Returns:
            ``DataOption_Cut``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if time_cutoff is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_cutoff)
        if energy_cutoff is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_cutoff)
        if weight_cutoff1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, weight_cutoff1)
        if weight_cutoff2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, weight_cutoff2)
        if source_weight is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, source_weight)

        self.value: typing.Final[tuple[any]] = types._Tuple(
            [time_cutoff, energy_cutoff, weight_cutoff1, weight_cutoff2, source_weight]
        )
        self.time_cutoff: typing.Final[types.Real] = time_cutoff
        self.energy_cutoff: typing.Final[types.Real] = energy_cutoff
        self.weight_cutoff1: typing.Final[types.Real] = weight_cutoff1
        self.weight_cutoff2: typing.Final[types.Real] = weight_cutoff2
        self.source_weight: typing.Final[types.Real] = source_weight

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Cut`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Cut``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Cut._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        time_cutoff = types.Real.from_mcnp(tokens[1])
        energy_cutoff = types.Real.from_mcnp(tokens[2])
        weight_cutoff1 = types.Real.from_mcnp(tokens[3])
        weight_cutoff2 = types.Real.from_mcnp(tokens[4])
        source_weight = types.Real.from_mcnp(tokens[5])

        return DataOption_Cut(
            time_cutoff, energy_cutoff, weight_cutoff1, weight_cutoff2, source_weight
        )
