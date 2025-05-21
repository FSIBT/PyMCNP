import re
import copy
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Vol(CellOption):
    """
    Represents INP vol elements.

    Attributes:
        volume: Cell volume.
    """

    _KEYWORD = 'vol'

    _ATTRS = {
        'volume': types.Real,
    }

    _REGEX = re.compile(rf'\Avol( {types.Real._REGEX.pattern})\Z')

    def __init__(self, volume: types.Real):
        """
        Initializes ``Vol``.

        Parameters:
            volume: Cell volume.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if volume is None or not (volume.value >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, volume)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                volume,
            ]
        )

        self.volume: typing.Final[types.Real] = volume


@dataclasses.dataclass
class VolBuilder:
    """
    Builds ``Vol``.

    Attributes:
        volume: Cell volume.
    """

    volume: str | float | types.Real

    def build(self):
        """
        Builds ``VolBuilder`` into ``Vol``.

        Returns:
            ``Vol`` for ``VolBuilder``.
        """

        volume = self.volume
        if isinstance(self.volume, types.Real):
            volume = self.volume
        elif isinstance(self.volume, float) or isinstance(self.volume, int):
            volume = types.Real(self.volume)
        elif isinstance(self.volume, str):
            volume = types.Real.from_mcnp(self.volume)

        return Vol(
            volume=volume,
        )

    @staticmethod
    def unbuild(ast: Vol):
        """
        Unbuilds ``Vol`` into ``VolBuilder``

        Returns:
            ``VolBuilder`` for ``Vol``.
        """

        return Vol(
            volume=copy.deepcopy(ast.volume),
        )
