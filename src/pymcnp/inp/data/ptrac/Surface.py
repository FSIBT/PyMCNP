import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Surface(_option.PtracOption):
    """
    Represents INP surface elements.

    Attributes:
        numbers: List of surface numbers for filtering.
    """

    _KEYWORD = 'surface'

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Asurface((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Surface``.

        Parameters:
            numbers: List of surface numbers for filtering.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if numbers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.numbers: typing.Final[types.Tuple[types.Integer]] = numbers


@dataclasses.dataclass
class SurfaceBuilder(_option.PtracOptionBuilder):
    """
    Builds ``Surface``.

    Attributes:
        numbers: List of surface numbers for filtering.
    """

    numbers: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``SurfaceBuilder`` into ``Surface``.

        Returns:
            ``Surface`` for ``SurfaceBuilder``.
        """

        if self.numbers:
            numbers = []
            for item in self.numbers:
                if isinstance(item, types.Integer):
                    numbers.append(item)
                elif isinstance(item, int):
                    numbers.append(types.Integer(item))
                elif isinstance(item, str):
                    numbers.append(types.Integer.from_mcnp(item))
            numbers = types.Tuple(numbers)
        else:
            numbers = None

        return Surface(
            numbers=numbers,
        )

    @staticmethod
    def unbuild(ast: Surface):
        """
        Unbuilds ``Surface`` into ``SurfaceBuilder``

        Returns:
            ``SurfaceBuilder`` for ``Surface``.
        """

        return SurfaceBuilder(
            numbers=copy.deepcopy(ast.numbers),
        )
