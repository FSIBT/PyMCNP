import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Tfc(MplotOption, keyword='tfc'):
    """
    Represents INP tfc elements.

    Attributes:
        x: Independent variable selector.
    """

    _ATTRS = {
        'x': types.String,
    }

    _REGEX = re.compile(rf'\Atfc( {types.String._REGEX.pattern})\Z')

    def __init__(self, x: types.String):
        """
        Initializes ``Tfc``.

        Parameters:
            x: Independent variable selector.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
            ]
        )

        self.x: typing.Final[types.String] = x


@dataclasses.dataclass
class TfcBuilder:
    """
    Builds ``Tfc``.

    Attributes:
        x: Independent variable selector.
    """

    x: str | types.String

    def build(self):
        """
        Builds ``TfcBuilder`` into ``Tfc``.

        Returns:
            ``Tfc`` for ``TfcBuilder``.
        """

        if isinstance(self.x, types.String):
            x = self.x
        elif isinstance(self.x, str):
            x = types.String.from_mcnp(self.x)

        return Tfc(
            x=x,
        )
