import re
import typing
import dataclasses


from ._option import TOption_1
from ....utils import types
from ....utils import errors


class Csub(TOption_1):
    """
    Represents INP csub elements.

    Attributes:
        count: Number of subdivisions to use.
    """

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'\Acsub( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``Csub``.

        Parameters:
            count: Number of subdivisions to use.

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
class CsubBuilder:
    """
    Builds ``Csub``.

    Attributes:
        count: Number of subdivisions to use.
    """

    count: str | int | types.Integer

    def build(self):
        """
        Builds ``CsubBuilder`` into ``Csub``.

        Returns:
            ``Csub`` for ``CsubBuilder``.
        """

        count = self.count
        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.Integer(self.count)
        elif isinstance(self.count, str):
            count = types.Integer.from_mcnp(self.count)

        return Csub(
            count=count,
        )
