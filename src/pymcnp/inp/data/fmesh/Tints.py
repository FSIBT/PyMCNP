import re
import copy
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Tints(FmeshOption):
    """
    Represents INP tints elements.

    Attributes:
        count: Number of mesh points for each mesh time.
    """

    _KEYWORD = 'tints'

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'\Atints( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``Tints``.

        Parameters:
            count: Number of mesh points for each mesh time.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if count is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, count)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                count,
            ]
        )

        self.count: typing.Final[types.Integer] = count


@dataclasses.dataclass
class TintsBuilder:
    """
    Builds ``Tints``.

    Attributes:
        count: Number of mesh points for each mesh time.
    """

    count: str | int | types.Integer

    def build(self):
        """
        Builds ``TintsBuilder`` into ``Tints``.

        Returns:
            ``Tints`` for ``TintsBuilder``.
        """

        count = self.count
        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.Integer(self.count)
        elif isinstance(self.count, str):
            count = types.Integer.from_mcnp(self.count)

        return Tints(
            count=count,
        )

    @staticmethod
    def unbuild(ast: Tints):
        """
        Unbuilds ``Tints`` into ``TintsBuilder``

        Returns:
            ``TintsBuilder`` for ``Tints``.
        """

        return Tints(
            count=copy.deepcopy(ast.count),
        )
