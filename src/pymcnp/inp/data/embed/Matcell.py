import re
import copy
import typing
import dataclasses


from ._option import EmbedOption
from ....utils import types
from ....utils import errors


class Matcell(EmbedOption):
    """
    Represents INP matcell elements.

    Attributes:
        pairs: Tuple of material-cell paris.
    """

    _KEYWORD = 'matcell'

    _ATTRS = {
        'pairs': types.Tuple[types.Matcell],
    }

    _REGEX = re.compile(rf'\Amatcell((?: {types.Matcell._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, pairs: types.Tuple[types.Matcell]):
        """
        Initializes ``Matcell``.

        Parameters:
            pairs: Tuple of material-cell paris.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if pairs is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, pairs)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                pairs,
            ]
        )

        self.pairs: typing.Final[types.Tuple[types.Matcell]] = pairs


@dataclasses.dataclass
class MatcellBuilder:
    """
    Builds ``Matcell``.

    Attributes:
        pairs: Tuple of material-cell paris.
    """

    pairs: list[str] | list[types.Matcell]

    def build(self):
        """
        Builds ``MatcellBuilder`` into ``Matcell``.

        Returns:
            ``Matcell`` for ``MatcellBuilder``.
        """

        if self.pairs:
            pairs = []
            for item in self.pairs:
                if isinstance(item, types.Matcell):
                    pairs.append(item)
                elif isinstance(item, str):
                    pairs.append(types.Matcell.from_mcnp(item))
                else:
                    pairs.append(item.build())
            pairs = types.Tuple(pairs)
        else:
            pairs = None

        return Matcell(
            pairs=pairs,
        )

    @staticmethod
    def unbuild(ast: Matcell):
        """
        Unbuilds ``Matcell`` into ``MatcellBuilder``

        Returns:
            ``MatcellBuilder`` for ``Matcell``.
        """

        return Matcell(
            pairs=copy.deepcopy(ast.pairs),
        )
