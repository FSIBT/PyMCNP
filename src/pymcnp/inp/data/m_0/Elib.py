import re
import typing
import dataclasses


from ._option import MOption_0
from ....utils import types
from ....utils import errors


class Elib(MOption_0, keyword='elib'):
    """
    Represents INP elib elements.

    Attributes:
        abx: Default electron table identifier.
    """

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Aelib( {types.String._REGEX.pattern})\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``Elib``.

        Parameters:
            abx: Default electron table identifier.

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
class ElibBuilder:
    """
    Builds ``Elib``.

    Attributes:
        abx: Default electron table identifier.
    """

    abx: str | types.String

    def build(self):
        """
        Builds ``ElibBuilder`` into ``Elib``.

        Returns:
            ``Elib`` for ``ElibBuilder``.
        """

        if isinstance(self.abx, types.String):
            abx = self.abx
        elif isinstance(self.abx, str):
            abx = types.String.from_mcnp(self.abx)

        return Elib(
            abx=abx,
        )
