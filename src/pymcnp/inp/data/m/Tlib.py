import re
import typing
import dataclasses


from ._option import MOption
from ....utils import types
from ....utils import errors


class Tlib(MOption, keyword='tlib'):
    """
    Represents INP tlib elements.

    Attributes:
        abx: Default triton table identifier.
    """

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Atlib( {types.String._REGEX.pattern})\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``Tlib``.

        Parameters:
            abx: Default triton table identifier.

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
class TlibBuilder:
    """
    Builds ``Tlib``.

    Attributes:
        abx: Default triton table identifier.
    """

    abx: str | types.String

    def build(self):
        """
        Builds ``TlibBuilder`` into ``Tlib``.

        Returns:
            ``Tlib`` for ``TlibBuilder``.
        """

        if isinstance(self.abx, types.String):
            abx = self.abx
        elif isinstance(self.abx, str):
            abx = types.String.from_mcnp(self.abx)

        return Tlib(
            abx=abx,
        )
