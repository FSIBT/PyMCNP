import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Xs(DataOption, keyword='xs'):
    """
    Represents INP xs elements.

    Attributes:
        suffix: Data card option suffix.
        weight_ratios: Tuple of atomic weight ratios.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'weight_ratios': types.Tuple[types.Substance],
    }

    _REGEX = re.compile(rf'\Axs(\d+)((?: {types.Substance._REGEX.pattern})+?)\Z')

    def __init__(self, suffix: types.Integer, weight_ratios: types.Tuple[types.Substance]):
        """
        Initializes ``Xs``.

        Parameters:
            suffix: Data card option suffix.
            weight_ratios: Tuple of atomic weight ratios.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if weight_ratios is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, weight_ratios)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                weight_ratios,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.weight_ratios: typing.Final[types.Tuple[types.Substance]] = weight_ratios


@dataclasses.dataclass
class XsBuilder:
    """
    Builds ``Xs``.

    Attributes:
        suffix: Data card option suffix.
        weight_ratios: Tuple of atomic weight ratios.
    """

    suffix: str | int | types.Integer
    weight_ratios: list[str] | list[types.Substance]

    def build(self):
        """
        Builds ``XsBuilder`` into ``Xs``.

        Returns:
            ``Xs`` for ``XsBuilder``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        weight_ratios = []
        for item in self.weight_ratios:
            if isinstance(item, types.Substance):
                weight_ratios.append(item)
            elif isinstance(item, str):
                weight_ratios.append(types.Substance.from_mcnp(item))
            else:
                weight_ratios.append(item.build())
        weight_ratios = types.Tuple(weight_ratios)

        return Xs(
            suffix=suffix,
            weight_ratios=weight_ratios,
        )
