import re
import typing
import dataclasses


from ._option import MOption
from ....utils import types
from ....utils import errors


class Alib(MOption, keyword='alib'):
    """
    Represents INP alib elements.

    Attributes:
        abx: Default alpha table identifier.
    """

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Aalib( {types.String._REGEX.pattern})\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``Alib``.

        Parameters:
            abx: Default alpha table identifier.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if abx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, abx)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                abx,
            ]
        )

        self.abx: typing.Final[types.String] = abx


@dataclasses.dataclass
class AlibBuilder:
    """
    Builds ``Alib``.

    Attributes:
        abx: Default alpha table identifier.
    """

    abx: str | types.String

    def build(self):
        """
        Builds ``AlibBuilder`` into ``Alib``.

        Returns:
            ``Alib`` for ``AlibBuilder``.
        """

        if isinstance(self.abx, types.String):
            abx = self.abx
        elif isinstance(self.abx, str):
            abx = types.String.from_mcnp(self.abx)

        return Alib(
            abx=abx,
        )
