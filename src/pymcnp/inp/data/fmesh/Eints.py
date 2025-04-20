import re
import typing
import dataclasses


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Eints(FmeshOption_, keyword='eints'):
    """
    Represents INP eints elements.

    Attributes:
        count: Number of mesh points for each mesh energy.
    """

    _ATTRS = {
        'count': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aeints( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, count: types.IntegerOrJump):
        """
        Initializes ``Eints``.

        Parameters:
            count: Number of mesh points for each mesh energy.

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
class EintsBuilder:
    """
    Builds ``Eints``.

    Attributes:
        count: Number of mesh points for each mesh energy.
    """

    count: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``EintsBuilder`` into ``Eints``.

        Returns:
            ``Eints`` for ``EintsBuilder``.
        """

        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.IntegerOrJump(self.count)
        elif isinstance(self.count, str):
            count = types.IntegerOrJump.from_mcnp(self.count)

        return Eints(
            count=count,
        )
