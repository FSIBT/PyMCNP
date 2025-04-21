import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Cut(DataOption, keyword='cut'):
    """
    Represents INP cut elements.

    Attributes:
        time_cutoff: Time cutoff in shakes.
        energy_cutoff: Lower energy cutoff.
        weight_cutoff1: Weight cutoff #1.
        weight_cutoff2: Weight cutoff #2.
        source_weight: Minimum source weight.
    """

    _ATTRS = {
        'time_cutoff': types.RealOrJump,
        'energy_cutoff': types.RealOrJump,
        'weight_cutoff1': types.RealOrJump,
        'weight_cutoff2': types.RealOrJump,
        'source_weight': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Acut( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        time_cutoff: types.RealOrJump,
        energy_cutoff: types.RealOrJump,
        weight_cutoff1: types.RealOrJump,
        weight_cutoff2: types.RealOrJump,
        source_weight: types.RealOrJump,
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
            InpError: SEMANTICS_OPTION.
        """

        if time_cutoff is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, time_cutoff)
        if energy_cutoff is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, energy_cutoff)
        if weight_cutoff1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, weight_cutoff1)
        if weight_cutoff2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, weight_cutoff2)
        if source_weight is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, source_weight)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                time_cutoff,
                energy_cutoff,
                weight_cutoff1,
                weight_cutoff2,
                source_weight,
            ]
        )

        self.time_cutoff: typing.Final[types.RealOrJump] = time_cutoff
        self.energy_cutoff: typing.Final[types.RealOrJump] = energy_cutoff
        self.weight_cutoff1: typing.Final[types.RealOrJump] = weight_cutoff1
        self.weight_cutoff2: typing.Final[types.RealOrJump] = weight_cutoff2
        self.source_weight: typing.Final[types.RealOrJump] = source_weight


@dataclasses.dataclass
class CutBuilder:
    """
    Builds ``Cut``.

    Attributes:
        time_cutoff: Time cutoff in shakes.
        energy_cutoff: Lower energy cutoff.
        weight_cutoff1: Weight cutoff #1.
        weight_cutoff2: Weight cutoff #2.
        source_weight: Minimum source weight.
    """

    time_cutoff: str | float | types.RealOrJump
    energy_cutoff: str | float | types.RealOrJump
    weight_cutoff1: str | float | types.RealOrJump
    weight_cutoff2: str | float | types.RealOrJump
    source_weight: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``CutBuilder`` into ``Cut``.

        Returns:
            ``Cut`` for ``CutBuilder``.
        """

        if isinstance(self.time_cutoff, types.Real):
            time_cutoff = self.time_cutoff
        elif isinstance(self.time_cutoff, float) or isinstance(self.time_cutoff, int):
            time_cutoff = types.RealOrJump(self.time_cutoff)
        elif isinstance(self.time_cutoff, str):
            time_cutoff = types.RealOrJump.from_mcnp(self.time_cutoff)

        if isinstance(self.energy_cutoff, types.Real):
            energy_cutoff = self.energy_cutoff
        elif isinstance(self.energy_cutoff, float) or isinstance(self.energy_cutoff, int):
            energy_cutoff = types.RealOrJump(self.energy_cutoff)
        elif isinstance(self.energy_cutoff, str):
            energy_cutoff = types.RealOrJump.from_mcnp(self.energy_cutoff)

        if isinstance(self.weight_cutoff1, types.Real):
            weight_cutoff1 = self.weight_cutoff1
        elif isinstance(self.weight_cutoff1, float) or isinstance(self.weight_cutoff1, int):
            weight_cutoff1 = types.RealOrJump(self.weight_cutoff1)
        elif isinstance(self.weight_cutoff1, str):
            weight_cutoff1 = types.RealOrJump.from_mcnp(self.weight_cutoff1)

        if isinstance(self.weight_cutoff2, types.Real):
            weight_cutoff2 = self.weight_cutoff2
        elif isinstance(self.weight_cutoff2, float) or isinstance(self.weight_cutoff2, int):
            weight_cutoff2 = types.RealOrJump(self.weight_cutoff2)
        elif isinstance(self.weight_cutoff2, str):
            weight_cutoff2 = types.RealOrJump.from_mcnp(self.weight_cutoff2)

        if isinstance(self.source_weight, types.Real):
            source_weight = self.source_weight
        elif isinstance(self.source_weight, float) or isinstance(self.source_weight, int):
            source_weight = types.RealOrJump(self.source_weight)
        elif isinstance(self.source_weight, str):
            source_weight = types.RealOrJump.from_mcnp(self.source_weight)

        return Cut(
            time_cutoff=time_cutoff,
            energy_cutoff=energy_cutoff,
            weight_cutoff1=weight_cutoff1,
            weight_cutoff2=weight_cutoff2,
            source_weight=source_weight,
        )
