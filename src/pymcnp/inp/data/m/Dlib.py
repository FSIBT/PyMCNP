import re
import typing
import dataclasses


from ._option import MOption
from ....utils import types
from ....utils import errors


class Dlib(MOption, keyword='dlib'):
    """
    Represents INP dlib elements.

    Attributes:
        abx: Default deuteron table identifier.
    """

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Adlib( {types.String._REGEX.pattern})\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``Dlib``.

        Parameters:
            abx: Default deuteron table identifier.

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
class DlibBuilder:
    """
    Builds ``Dlib``.

    Attributes:
        abx: Default deuteron table identifier.
    """

    abx: str | types.String

    def build(self):
        """
        Builds ``DlibBuilder`` into ``Dlib``.

        Returns:
            ``Dlib`` for ``DlibBuilder``.
        """

        if isinstance(self.abx, types.String):
            abx = self.abx
        elif isinstance(self.abx, str):
            abx = types.String.from_mcnp(self.abx)

        return Dlib(
            abx=abx,
        )
