import re
import typing
import dataclasses


from ._option import BfldOption
from ....utils import types
from ....utils import errors


class Axs(BfldOption):
    """
    Represents INP axs elements.

    Attributes:
        vector: Direction of the cosines of the quadropole beam axis.
    """

    _ATTRS = {
        'vector': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aaxs((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, vector: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Axs``.

        Parameters:
            vector: Direction of the cosines of the quadropole beam axis.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if vector is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vector)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                vector,
            ]
        )

        self.vector: typing.Final[types.Tuple[types.RealOrJump]] = vector


@dataclasses.dataclass
class AxsBuilder:
    """
    Builds ``Axs``.

    Attributes:
        vector: Direction of the cosines of the quadropole beam axis.
    """

    vector: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``AxsBuilder`` into ``Axs``.

        Returns:
            ``Axs`` for ``AxsBuilder``.
        """

        if self.vector:
            vector = []
            for item in self.vector:
                if isinstance(item, types.RealOrJump):
                    vector.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    vector.append(types.RealOrJump(item))
                elif isinstance(item, str):
                    vector.append(types.RealOrJump.from_mcnp(item))
            vector = types.Tuple(vector)
        else:
            vector = None

        return Axs(
            vector=vector,
        )
