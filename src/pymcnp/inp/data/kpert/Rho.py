import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Rho(_option.KpertOption):
    """
    Represents INP rho elements.

    Attributes:
        densities: List of densities.
    """

    _KEYWORD = 'rho'

    _ATTRS = {
        'densities': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Arho((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, densities: types.Tuple[types.Real]):
        """
        Initializes ``Rho``.

        Parameters:
            densities: List of densities.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if densities is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, densities)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                densities,
            ]
        )

        self.densities: typing.Final[types.Tuple[types.Real]] = densities


@dataclasses.dataclass
class RhoBuilder(_option.KpertOptionBuilder):
    """
    Builds ``Rho``.

    Attributes:
        densities: List of densities.
    """

    densities: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``RhoBuilder`` into ``Rho``.

        Returns:
            ``Rho`` for ``RhoBuilder``.
        """

        if self.densities:
            densities = []
            for item in self.densities:
                if isinstance(item, types.Real):
                    densities.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    densities.append(types.Real(item))
                elif isinstance(item, str):
                    densities.append(types.Real.from_mcnp(item))
            densities = types.Tuple(densities)
        else:
            densities = None

        return Rho(
            densities=densities,
        )

    @staticmethod
    def unbuild(ast: Rho):
        """
        Unbuilds ``Rho`` into ``RhoBuilder``

        Returns:
            ``RhoBuilder`` for ``Rho``.
        """

        return RhoBuilder(
            densities=copy.deepcopy(ast.densities),
        )
