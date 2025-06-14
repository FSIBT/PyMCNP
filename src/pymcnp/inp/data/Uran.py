import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Uran(_option.DataOption):
    """
    Represents INP uran elements.

    Attributes:
        transformations: Tuple of stochastic transformations.
    """

    _KEYWORD = 'uran'

    _ATTRS = {
        'transformations': types.Tuple[types.Stochastic],
    }

    _REGEX = re.compile(r'\Auran((?: \S+ \S+ \S+ \S+)+?)\Z')

    def __init__(self, transformations: types.Tuple[types.Stochastic]):
        """
        Initializes ``Uran``.

        Parameters:
            transformations: Tuple of stochastic transformations.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if transformations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, transformations)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                transformations,
            ]
        )

        self.transformations: typing.Final[types.Tuple[types.Stochastic]] = transformations


@dataclasses.dataclass
class UranBuilder(_option.DataOptionBuilder):
    """
    Builds ``Uran``.

    Attributes:
        transformations: Tuple of stochastic transformations.
    """

    transformations: list[str] | list[types.Stochastic]

    def build(self):
        """
        Builds ``UranBuilder`` into ``Uran``.

        Returns:
            ``Uran`` for ``UranBuilder``.
        """

        if self.transformations:
            transformations = []
            for item in self.transformations:
                if isinstance(item, types.Stochastic):
                    transformations.append(item)
                elif isinstance(item, str):
                    transformations.append(types.Stochastic.from_mcnp(item))
            transformations = types.Tuple(transformations)
        else:
            transformations = None

        return Uran(
            transformations=transformations,
        )

    @staticmethod
    def unbuild(ast: Uran):
        """
        Unbuilds ``Uran`` into ``UranBuilder``

        Returns:
            ``UranBuilder`` for ``Uran``.
        """

        return UranBuilder(
            transformations=copy.deepcopy(ast.transformations),
        )
