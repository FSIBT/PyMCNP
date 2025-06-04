import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Awtab(DataOption):
    """
    Represents INP awtab elements.

    Attributes:
        weight_ratios: Tuple of atomic weight ratios.
    """

    _KEYWORD = 'awtab'

    _ATTRS = {
        'weight_ratios': types.Tuple[types.Substance],
    }

    _REGEX = re.compile(rf'\Aawtab((?: {types.Substance._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, weight_ratios: types.Tuple[types.Substance]):
        """
        Initializes ``Awtab``.

        Parameters:
            weight_ratios: Tuple of atomic weight ratios.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if weight_ratios is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, weight_ratios)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                weight_ratios,
            ]
        )

        self.weight_ratios: typing.Final[types.Tuple[types.Substance]] = weight_ratios


@dataclasses.dataclass
class AwtabBuilder:
    """
    Builds ``Awtab``.

    Attributes:
        weight_ratios: Tuple of atomic weight ratios.
    """

    weight_ratios: list[str] | list[types.Substance]

    def build(self):
        """
        Builds ``AwtabBuilder`` into ``Awtab``.

        Returns:
            ``Awtab`` for ``AwtabBuilder``.
        """

        if self.weight_ratios:
            weight_ratios = []
            for item in self.weight_ratios:
                if isinstance(item, types.Substance):
                    weight_ratios.append(item)
                elif isinstance(item, str):
                    weight_ratios.append(types.Substance.from_mcnp(item))
                else:
                    weight_ratios.append(item.build())
            weight_ratios = types.Tuple(weight_ratios)
        else:
            weight_ratios = None

        return Awtab(
            weight_ratios=weight_ratios,
        )

    @staticmethod
    def unbuild(ast: Awtab):
        """
        Unbuilds ``Awtab`` into ``AwtabBuilder``

        Returns:
            ``AwtabBuilder`` for ``Awtab``.
        """

        return Awtab(
            weight_ratios=copy.deepcopy(ast.weight_ratios),
        )
