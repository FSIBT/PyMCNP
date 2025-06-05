import re
import copy
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Iints(FmeshOption):
    """
    Represents INP iints elements.

    Attributes:
        count: Number of mesh points x/r for rectangular/cylindrical geometry.
    """

    _KEYWORD = 'iints'

    _ATTRS = {
        'count': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Aiints((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, count: types.Tuple[types.Integer]):
        """
        Initializes ``Iints``.

        Parameters:
            count: Number of mesh points x/r for rectangular/cylindrical geometry.

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

        self.count: typing.Final[types.Tuple[types.Integer]] = count


@dataclasses.dataclass
class IintsBuilder:
    """
    Builds ``Iints``.

    Attributes:
        count: Number of mesh points x/r for rectangular/cylindrical geometry.
    """

    count: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``IintsBuilder`` into ``Iints``.

        Returns:
            ``Iints`` for ``IintsBuilder``.
        """

        if self.count:
            count = []
            for item in self.count:
                if isinstance(item, types.Integer):
                    count.append(item)
                elif isinstance(item, int):
                    count.append(types.Integer(item))
                elif isinstance(item, str):
                    count.append(types.Integer.from_mcnp(item))
            count = types.Tuple(count)
        else:
            count = None

        return Iints(
            count=count,
        )

    @staticmethod
    def unbuild(ast: Iints):
        """
        Unbuilds ``Iints`` into ``IintsBuilder``

        Returns:
            ``IintsBuilder`` for ``Iints``.
        """

        return Iints(
            count=copy.deepcopy(ast.count),
        )
