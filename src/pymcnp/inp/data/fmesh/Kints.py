import re
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Kints(FmeshOption):
    """
    Represents INP kints elements.

    Attributes:
        count: Number of mesh points z/theta for rectangular/cylindrical geometry.
    """

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'\Akints( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``Kints``.

        Parameters:
            count: Number of mesh points z/theta for rectangular/cylindrical geometry.

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
class KintsBuilder:
    """
    Builds ``Kints``.

    Attributes:
        count: Number of mesh points z/theta for rectangular/cylindrical geometry.
    """

    count: str | int | types.Integer

    def build(self):
        """
        Builds ``KintsBuilder`` into ``Kints``.

        Returns:
            ``Kints`` for ``KintsBuilder``.
        """

        count = self.count
        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.Integer(self.count)
        elif isinstance(self.count, str):
            count = types.Integer.from_mcnp(self.count)

        return Kints(
            count=count,
        )
