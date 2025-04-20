import re
import typing
import dataclasses


from .option_ import MOption_
from ....utils import types
from ....utils import errors


class Plib(MOption_, keyword='plib'):
    """
    Represents INP plib elements.

    Attributes:
        abx: Default photoatomic table identifier.
    """

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Aplib( {types.String._REGEX.pattern})\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``Plib``.

        Parameters:
            abx: Default photoatomic table identifier.

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
class PlibBuilder:
    """
    Builds ``Plib``.

    Attributes:
        abx: Default photoatomic table identifier.
    """

    abx: str | types.String

    def build(self):
        """
        Builds ``PlibBuilder`` into ``Plib``.

        Returns:
            ``Plib`` for ``PlibBuilder``.
        """

        if isinstance(self.abx, types.String):
            abx = self.abx
        elif isinstance(self.abx, str):
            abx = types.String.from_mcnp(self.abx)

        return Plib(
            abx=abx,
        )
