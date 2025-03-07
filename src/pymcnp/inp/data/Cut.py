import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Cut(DataOption_, keyword='cut'):
    """
    Represents INP cut elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'time_cutoff': types.Real,
        'energy_cutoff': types.Real,
        'weight_cutoff1': types.Real,
        'weight_cutoff2': types.Real,
        'source_weight': types.Real,
    }

    _REGEX = re.compile(
        rf'cut( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
    )

    def __init__(
        self,
        time_cutoff: types.Real,
        energy_cutoff: types.Real,
        weight_cutoff1: types.Real,
        weight_cutoff2: types.Real,
        source_weight: types.Real,
    ):
        """
        Initializes ``Cut``.

        Parameters:
            time_cutoff: Time cutoff in shakes.
            energy_cutoff: Lower energy cutoff.
            weight_cutoff1: Weight cutoff #1.
            weight_cutoff2: Weight cutoff #2.
            source_weight: Minimum source weight.

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

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                time_cutoff,
                energy_cutoff,
                weight_cutoff1,
                weight_cutoff2,
                source_weight,
            ]
        )

        self.time_cutoff: typing.Final[types.Real] = time_cutoff
        self.energy_cutoff: typing.Final[types.Real] = energy_cutoff
        self.weight_cutoff1: typing.Final[types.Real] = weight_cutoff1
        self.weight_cutoff2: typing.Final[types.Real] = weight_cutoff2
        self.source_weight: typing.Final[types.Real] = source_weight
