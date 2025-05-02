import re
import typing
import dataclasses


from ._option import MOption_0
from ....utils import types
from ....utils import errors


class Slib(MOption_0):
    """
    Represents INP slib elements.

    Attributes:
        abx: Default helion table identifier.
    """

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Aslib( {types.String._REGEX.pattern})\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``Slib``.

        Parameters:
            abx: Default helion table identifier.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if abx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, abx)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                abx,
            ]
        )

        self.abx: typing.Final[types.String] = abx


@dataclasses.dataclass
class SlibBuilder:
    """
    Builds ``Slib``.

    Attributes:
        abx: Default helion table identifier.
    """

    abx: str | types.String

    def build(self):
        """
        Builds ``SlibBuilder`` into ``Slib``.

        Returns:
            ``Slib`` for ``SlibBuilder``.
        """

        if isinstance(self.abx, types.String):
            abx = self.abx
        elif isinstance(self.abx, str):
            abx = types.String.from_mcnp(self.abx)

        return Slib(
            abx=abx,
        )
