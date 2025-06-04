import re
import copy
import typing
import dataclasses


from ._option import KsenOption
from ....utils import types
from ....utils import errors


class Cos(KsenOption):
    """
    Represents INP cos elements.

    Attributes:
        cosines: Range of direction-change cosines.
    """

    _KEYWORD = 'cos'

    _ATTRS = {
        'cosines': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Acos((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, cosines: types.Tuple[types.Real]):
        """
        Initializes ``Cos``.

        Parameters:
            cosines: Range of direction-change cosines.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if cosines is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cosines)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cosines,
            ]
        )

        self.cosines: typing.Final[types.Tuple[types.Real]] = cosines


@dataclasses.dataclass
class CosBuilder:
    """
    Builds ``Cos``.

    Attributes:
        cosines: Range of direction-change cosines.
    """

    cosines: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``CosBuilder`` into ``Cos``.

        Returns:
            ``Cos`` for ``CosBuilder``.
        """

        if self.cosines:
            cosines = []
            for item in self.cosines:
                if isinstance(item, types.Real):
                    cosines.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    cosines.append(types.Real(item))
                elif isinstance(item, str):
                    cosines.append(types.Real.from_mcnp(item))
            cosines = types.Tuple(cosines)
        else:
            cosines = None

        return Cos(
            cosines=cosines,
        )

    @staticmethod
    def unbuild(ast: Cos):
        """
        Unbuilds ``Cos`` into ``CosBuilder``

        Returns:
            ``CosBuilder`` for ``Cos``.
        """

        return Cos(
            cosines=copy.deepcopy(ast.cosines),
        )
