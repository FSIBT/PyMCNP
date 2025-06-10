import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Elpt(_option.DataOption):
    """
    Represents INP elpt elements.

    Attributes:
        cutoffs: Tuple of cell lower energy cutoffs.
    """

    _KEYWORD = 'elpt'

    _ATTRS = {
        'cutoffs': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aelpt((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, cutoffs: types.Tuple[types.Real]):
        """
        Initializes ``Elpt``.

        Parameters:
            cutoffs: Tuple of cell lower energy cutoffs.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if cutoffs is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cutoffs)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cutoffs,
            ]
        )

        self.cutoffs: typing.Final[types.Tuple[types.Real]] = cutoffs


@dataclasses.dataclass
class ElptBuilder(_option.DataOptionBuilder):
    """
    Builds ``Elpt``.

    Attributes:
        cutoffs: Tuple of cell lower energy cutoffs.
    """

    cutoffs: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``ElptBuilder`` into ``Elpt``.

        Returns:
            ``Elpt`` for ``ElptBuilder``.
        """

        if self.cutoffs:
            cutoffs = []
            for item in self.cutoffs:
                if isinstance(item, types.Real):
                    cutoffs.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    cutoffs.append(types.Real(item))
                elif isinstance(item, str):
                    cutoffs.append(types.Real.from_mcnp(item))
            cutoffs = types.Tuple(cutoffs)
        else:
            cutoffs = None

        return Elpt(
            cutoffs=cutoffs,
        )

    @staticmethod
    def unbuild(ast: Elpt):
        """
        Unbuilds ``Elpt`` into ``ElptBuilder``

        Returns:
            ``ElptBuilder`` for ``Elpt``.
        """

        return ElptBuilder(
            cutoffs=copy.deepcopy(ast.cutoffs),
        )
