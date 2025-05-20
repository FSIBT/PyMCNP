import re
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Eints(FmeshOption):
    """
    Represents INP eints elements.

    Attributes:
        count: Number of mesh points for each mesh energy.
    """

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'\Aeints( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``Eints``.

        Parameters:
            count: Number of mesh points for each mesh energy.

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
class EintsBuilder:
    """
    Builds ``Eints``.

    Attributes:
        count: Number of mesh points for each mesh energy.
    """

    count: str | int | types.Integer

    def build(self):
        """
        Builds ``EintsBuilder`` into ``Eints``.

        Returns:
            ``Eints`` for ``EintsBuilder``.
        """

        count = self.count
        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.Integer(self.count)
        elif isinstance(self.count, str):
            count = types.Integer.from_mcnp(self.count)

        return Eints(
            count=count,
        )
