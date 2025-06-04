import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Cut(DataOption):
    """
    Represents INP cut elements.

    Attributes:
        designator: Data option particle designator.
        time_cutoff: Time cutoff in shakes.
        energy_cutoff: Lower energy cutoff.
        weight_cutoff1: Weight cutoff #1.
        weight_cutoff2: Weight cutoff #2.
        source_weight: Minimum source weight.
    """

    _KEYWORD = 'cut'

    _ATTRS = {
        'designator': types.Designator,
        'time_cutoff': types.Real,
        'energy_cutoff': types.Real,
        'weight_cutoff1': types.Real,
        'weight_cutoff2': types.Real,
        'source_weight': types.Real,
    }

    _REGEX = re.compile(
        rf'\Acut:(\S+)( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        designator: types.Designator,
        time_cutoff: types.Real = None,
        energy_cutoff: types.Real = None,
        weight_cutoff1: types.Real = None,
        weight_cutoff2: types.Real = None,
        source_weight: types.Real = None,
    ):
        """
        Initializes ``Cut``.

        Parameters:
            designator: Data option particle designator.
            time_cutoff: Time cutoff in shakes.
            energy_cutoff: Lower energy cutoff.
            weight_cutoff1: Weight cutoff #1.
            weight_cutoff2: Weight cutoff #2.
            source_weight: Minimum source weight.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                time_cutoff,
                energy_cutoff,
                weight_cutoff1,
                weight_cutoff2,
                source_weight,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.time_cutoff: typing.Final[types.Real] = time_cutoff
        self.energy_cutoff: typing.Final[types.Real] = energy_cutoff
        self.weight_cutoff1: typing.Final[types.Real] = weight_cutoff1
        self.weight_cutoff2: typing.Final[types.Real] = weight_cutoff2
        self.source_weight: typing.Final[types.Real] = source_weight


@dataclasses.dataclass
class CutBuilder:
    """
    Builds ``Cut``.

    Attributes:
        designator: Data option particle designator.
        time_cutoff: Time cutoff in shakes.
        energy_cutoff: Lower energy cutoff.
        weight_cutoff1: Weight cutoff #1.
        weight_cutoff2: Weight cutoff #2.
        source_weight: Minimum source weight.
    """

    designator: str | types.Designator
    time_cutoff: str | float | types.Real = None
    energy_cutoff: str | float | types.Real = None
    weight_cutoff1: str | float | types.Real = None
    weight_cutoff2: str | float | types.Real = None
    source_weight: str | float | types.Real = None

    def build(self):
        """
        Builds ``CutBuilder`` into ``Cut``.

        Returns:
            ``Cut`` for ``CutBuilder``.
        """

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        time_cutoff = self.time_cutoff
        if isinstance(self.time_cutoff, types.Real):
            time_cutoff = self.time_cutoff
        elif isinstance(self.time_cutoff, float) or isinstance(self.time_cutoff, int):
            time_cutoff = types.Real(self.time_cutoff)
        elif isinstance(self.time_cutoff, str):
            time_cutoff = types.Real.from_mcnp(self.time_cutoff)

        energy_cutoff = self.energy_cutoff
        if isinstance(self.energy_cutoff, types.Real):
            energy_cutoff = self.energy_cutoff
        elif isinstance(self.energy_cutoff, float) or isinstance(self.energy_cutoff, int):
            energy_cutoff = types.Real(self.energy_cutoff)
        elif isinstance(self.energy_cutoff, str):
            energy_cutoff = types.Real.from_mcnp(self.energy_cutoff)

        weight_cutoff1 = self.weight_cutoff1
        if isinstance(self.weight_cutoff1, types.Real):
            weight_cutoff1 = self.weight_cutoff1
        elif isinstance(self.weight_cutoff1, float) or isinstance(self.weight_cutoff1, int):
            weight_cutoff1 = types.Real(self.weight_cutoff1)
        elif isinstance(self.weight_cutoff1, str):
            weight_cutoff1 = types.Real.from_mcnp(self.weight_cutoff1)

        weight_cutoff2 = self.weight_cutoff2
        if isinstance(self.weight_cutoff2, types.Real):
            weight_cutoff2 = self.weight_cutoff2
        elif isinstance(self.weight_cutoff2, float) or isinstance(self.weight_cutoff2, int):
            weight_cutoff2 = types.Real(self.weight_cutoff2)
        elif isinstance(self.weight_cutoff2, str):
            weight_cutoff2 = types.Real.from_mcnp(self.weight_cutoff2)

        source_weight = self.source_weight
        if isinstance(self.source_weight, types.Real):
            source_weight = self.source_weight
        elif isinstance(self.source_weight, float) or isinstance(self.source_weight, int):
            source_weight = types.Real(self.source_weight)
        elif isinstance(self.source_weight, str):
            source_weight = types.Real.from_mcnp(self.source_weight)

        return Cut(
            designator=designator,
            time_cutoff=time_cutoff,
            energy_cutoff=energy_cutoff,
            weight_cutoff1=weight_cutoff1,
            weight_cutoff2=weight_cutoff2,
            source_weight=source_weight,
        )

    @staticmethod
    def unbuild(ast: Cut):
        """
        Unbuilds ``Cut`` into ``CutBuilder``

        Returns:
            ``CutBuilder`` for ``Cut``.
        """

        return Cut(
            designator=copy.deepcopy(ast.designator),
            time_cutoff=copy.deepcopy(ast.time_cutoff),
            energy_cutoff=copy.deepcopy(ast.energy_cutoff),
            weight_cutoff1=copy.deepcopy(ast.weight_cutoff1),
            weight_cutoff2=copy.deepcopy(ast.weight_cutoff2),
            source_weight=copy.deepcopy(ast.source_weight),
        )
