import re
import copy
import typing
import dataclasses


from ._option import DawwgOption
from ....utils import types
from ....utils import errors


class Xsec(DawwgOption):
    """
    Represents INP xsec elements.

    Attributes:
        count: Number of sample points for each direction in each mesh.
    """

    _KEYWORD = 'xsec'

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'\Axsec( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``Xsec``.

        Parameters:
            count: Number of sample points for each direction in each mesh.

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
class XsecBuilder:
    """
    Builds ``Xsec``.

    Attributes:
        count: Number of sample points for each direction in each mesh.
    """

    count: str | int | types.Integer

    def build(self):
        """
        Builds ``XsecBuilder`` into ``Xsec``.

        Returns:
            ``Xsec`` for ``XsecBuilder``.
        """

        count = self.count
        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.Integer(self.count)
        elif isinstance(self.count, str):
            count = types.Integer.from_mcnp(self.count)

        return Xsec(
            count=count,
        )

    @staticmethod
    def unbuild(ast: Xsec):
        """
        Unbuilds ``Xsec`` into ``XsecBuilder``

        Returns:
            ``XsecBuilder`` for ``Xsec``.
        """

        return Xsec(
            count=copy.deepcopy(ast.count),
        )
