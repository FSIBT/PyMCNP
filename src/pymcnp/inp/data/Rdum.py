import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Rdum(DataOption):
    """
    Represents INP rdum elements.

    Attributes:
        floats: Floating point array.
    """

    _KEYWORD = 'rdum'

    _ATTRS = {
        'floats': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Ardum((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, floats: types.Tuple[types.Real]):
        """
        Initializes ``Rdum``.

        Parameters:
            floats: Floating point array.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if floats is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, floats)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                floats,
            ]
        )

        self.floats: typing.Final[types.Tuple[types.Real]] = floats


@dataclasses.dataclass
class RdumBuilder:
    """
    Builds ``Rdum``.

    Attributes:
        floats: Floating point array.
    """

    floats: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``RdumBuilder`` into ``Rdum``.

        Returns:
            ``Rdum`` for ``RdumBuilder``.
        """

        if self.floats:
            floats = []
            for item in self.floats:
                if isinstance(item, types.Real):
                    floats.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    floats.append(types.Real(item))
                elif isinstance(item, str):
                    floats.append(types.Real.from_mcnp(item))
            floats = types.Tuple(floats)
        else:
            floats = None

        return Rdum(
            floats=floats,
        )

    @staticmethod
    def unbuild(ast: Rdum):
        """
        Unbuilds ``Rdum`` into ``RdumBuilder``

        Returns:
            ``RdumBuilder`` for ``Rdum``.
        """

        return Rdum(
            floats=copy.deepcopy(ast.floats),
        )
