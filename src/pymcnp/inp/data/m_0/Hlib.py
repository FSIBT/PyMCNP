import re
import typing
import dataclasses


from ._option import MOption_0
from ....utils import types
from ....utils import errors


class Hlib(MOption_0):
    """
    Represents INP hlib elements.

    Attributes:
        abx: Default proton table identifier.
    """

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Ahlib( {types.String._REGEX.pattern})\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``Hlib``.

        Parameters:
            abx: Default proton table identifier.

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
class HlibBuilder:
    """
    Builds ``Hlib``.

    Attributes:
        abx: Default proton table identifier.
    """

    abx: str | types.String

    def build(self):
        """
        Builds ``HlibBuilder`` into ``Hlib``.

        Returns:
            ``Hlib`` for ``HlibBuilder``.
        """

        if isinstance(self.abx, types.String):
            abx = self.abx
        elif isinstance(self.abx, str):
            abx = types.String.from_mcnp(self.abx)

        return Hlib(
            abx=abx,
        )
