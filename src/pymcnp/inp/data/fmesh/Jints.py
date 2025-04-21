import re
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Jints(FmeshOption, keyword='jints'):
    """
    Represents INP jints elements.

    Attributes:
        count: Number of mesh points y/z for rectangular/cylindrical geometry.
    """

    _ATTRS = {
        'count': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Ajints( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, count: types.IntegerOrJump):
        """
        Initializes ``Jints``.

        Parameters:
            count: Number of mesh points y/z for rectangular/cylindrical geometry.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if count is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, count)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                count,
            ]
        )

        self.count: typing.Final[types.IntegerOrJump] = count


@dataclasses.dataclass
class JintsBuilder:
    """
    Builds ``Jints``.

    Attributes:
        count: Number of mesh points y/z for rectangular/cylindrical geometry.
    """

    count: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``JintsBuilder`` into ``Jints``.

        Returns:
            ``Jints`` for ``JintsBuilder``.
        """

        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.IntegerOrJump(self.count)
        elif isinstance(self.count, str):
            count = types.IntegerOrJump.from_mcnp(self.count)

        return Jints(
            count=count,
        )
