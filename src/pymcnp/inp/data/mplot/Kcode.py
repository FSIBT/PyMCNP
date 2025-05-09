import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Kcode(MplotOption):
    """
    Represents INP kcode elements.

    Attributes:
        i: Lifetime to remove.
    """

    _ATTRS = {
        'i': types.Integer,
    }

    _REGEX = re.compile(rf'\Akcode( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, i: types.Integer):
        """
        Initializes ``Kcode``.

        Parameters:
            i: Lifetime to remove.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if i is None or not (1 <= i <= 6 or 11 <= i <= 19):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                i,
            ]
        )

        self.i: typing.Final[types.Integer] = i


@dataclasses.dataclass
class KcodeBuilder:
    """
    Builds ``Kcode``.

    Attributes:
        i: Lifetime to remove.
    """

    i: str | int | types.Integer

    def build(self):
        """
        Builds ``KcodeBuilder`` into ``Kcode``.

        Returns:
            ``Kcode`` for ``KcodeBuilder``.
        """

        if isinstance(self.i, types.Integer):
            i = self.i
        elif isinstance(self.i, int):
            i = types.Integer(self.i)
        elif isinstance(self.i, str):
            i = types.Integer.from_mcnp(self.i)

        return Kcode(
            i=i,
        )
