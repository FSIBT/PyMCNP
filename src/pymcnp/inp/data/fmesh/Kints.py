import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Kints(_option.FmeshOption):
    """
    Represents INP kints elements.

    Attributes:
        count: Number of mesh points z/theta for rectangular/cylindrical geometry.
    """

    _KEYWORD = 'kints'

    _ATTRS = {
        'count': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Akints((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, count: types.Tuple[types.Integer]):
        """
        Initializes ``Kints``.

        Parameters:
            count: Number of mesh points z/theta for rectangular/cylindrical geometry.

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
class KintsBuilder(_option.FmeshOptionBuilder):
    """
    Builds ``Kints``.

    Attributes:
        count: Number of mesh points z/theta for rectangular/cylindrical geometry.
    """

    count: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``KintsBuilder`` into ``Kints``.

        Returns:
            ``Kints`` for ``KintsBuilder``.
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

        return Kints(
            count=count,
        )

    @staticmethod
    def unbuild(ast: Kints):
        """
        Unbuilds ``Kints`` into ``KintsBuilder``

        Returns:
            ``KintsBuilder`` for ``Kints``.
        """

        return KintsBuilder(
            count=copy.deepcopy(ast.count),
        )
