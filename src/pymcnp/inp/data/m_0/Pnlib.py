import re
import typing
import dataclasses


from ._option import MOption_0
from ....utils import types
from ....utils import errors


class Pnlib(MOption_0):
    """
    Represents INP pnlib elements.

    Attributes:
        abx: Default photonuclear table identifier.
    """

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Apnlib( {types.String._REGEX.pattern})\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``Pnlib``.

        Parameters:
            abx: Default photonuclear table identifier.

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
class PnlibBuilder:
    """
    Builds ``Pnlib``.

    Attributes:
        abx: Default photonuclear table identifier.
    """

    abx: str | types.String

    def build(self):
        """
        Builds ``PnlibBuilder`` into ``Pnlib``.

        Returns:
            ``Pnlib`` for ``PnlibBuilder``.
        """

        if isinstance(self.abx, types.String):
            abx = self.abx
        elif isinstance(self.abx, str):
            abx = types.String.from_mcnp(self.abx)

        return Pnlib(
            abx=abx,
        )
