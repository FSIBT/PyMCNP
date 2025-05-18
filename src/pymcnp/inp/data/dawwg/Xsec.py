import re
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

    _ATTRS = {
        'count': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Axsec( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, count: types.IntegerOrJump):
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

        self.count: typing.Final[types.IntegerOrJump] = count


@dataclasses.dataclass
class XsecBuilder:
    """
    Builds ``Xsec``.

    Attributes:
        count: Number of sample points for each direction in each mesh.
    """

    count: str | int | types.IntegerOrJump

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
            count = types.IntegerOrJump(self.count)
        elif isinstance(self.count, str):
            count = types.IntegerOrJump.from_mcnp(self.count)

        return Xsec(
            count=count,
        )
