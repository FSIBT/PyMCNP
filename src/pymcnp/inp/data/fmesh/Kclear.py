import re
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Kclear(FmeshOption, keyword='kclear'):
    """
    Represents INP kclear elements.

    Attributes:
        count: KCODE cycles between zeros.
    """

    _ATTRS = {
        'count': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Akclear( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, count: types.IntegerOrJump):
        """
        Initializes ``Kclear``.

        Parameters:
            count: KCODE cycles between zeros.

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
class KclearBuilder:
    """
    Builds ``Kclear``.

    Attributes:
        count: KCODE cycles between zeros.
    """

    count: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``KclearBuilder`` into ``Kclear``.

        Returns:
            ``Kclear`` for ``KclearBuilder``.
        """

        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.IntegerOrJump(self.count)
        elif isinstance(self.count, str):
            count = types.IntegerOrJump.from_mcnp(self.count)

        return Kclear(
            count=count,
        )
