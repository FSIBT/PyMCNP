import re
import copy
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Jints(FmeshOption):
    """
    Represents INP jints elements.

    Attributes:
        count: Number of mesh points y/z for rectangular/cylindrical geometry.
    """

    _KEYWORD = 'jints'

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'\Ajints( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``Jints``.

        Parameters:
            count: Number of mesh points y/z for rectangular/cylindrical geometry.

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
class JintsBuilder:
    """
    Builds ``Jints``.

    Attributes:
        count: Number of mesh points y/z for rectangular/cylindrical geometry.
    """

    count: str | int | types.Integer

    def build(self):
        """
        Builds ``JintsBuilder`` into ``Jints``.

        Returns:
            ``Jints`` for ``JintsBuilder``.
        """

        count = self.count
        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.Integer(self.count)
        elif isinstance(self.count, str):
            count = types.Integer.from_mcnp(self.count)

        return Jints(
            count=count,
        )

    @staticmethod
    def unbuild(ast: Jints):
        """
        Unbuilds ``Jints`` into ``JintsBuilder``

        Returns:
            ``JintsBuilder`` for ``Jints``.
        """

        return Jints(
            count=copy.deepcopy(ast.count),
        )
