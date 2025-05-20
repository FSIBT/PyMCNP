import re
import typing
import dataclasses


from ._option import ActOption
from ....utils import types
from ....utils import errors


class Nap(ActOption):
    """
    Represents INP nap elements.

    Attributes:
        count: Number of activation products.
    """

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'\Anap( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``Nap``.

        Parameters:
            count: Number of activation products.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if count is None or not (count.value >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, count)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                count,
            ]
        )

        self.count: typing.Final[types.Integer] = count


@dataclasses.dataclass
class NapBuilder:
    """
    Builds ``Nap``.

    Attributes:
        count: Number of activation products.
    """

    count: str | int | types.Integer

    def build(self):
        """
        Builds ``NapBuilder`` into ``Nap``.

        Returns:
            ``Nap`` for ``NapBuilder``.
        """

        count = self.count
        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.Integer(self.count)
        elif isinstance(self.count, str):
            count = types.Integer.from_mcnp(self.count)

        return Nap(
            count=count,
        )
