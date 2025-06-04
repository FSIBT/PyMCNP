import re
import copy
import typing
import dataclasses


from ._option import MOption_0
from ....utils import types
from ....utils import errors


class Dlib(MOption_0):
    """
    Represents INP dlib elements.

    Attributes:
        abx: Default deuteron table identifier.
    """

    _KEYWORD = 'dlib'

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Adlib( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``Dlib``.

        Parameters:
            abx: Default deuteron table identifier.

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

        abx = self.abx
        if isinstance(self.abx, types.String):
            abx = self.abx
        elif isinstance(self.abx, str):
            abx = types.String.from_mcnp(self.abx)

        return Dlib(
            abx=abx,
        )

    @staticmethod
    def unbuild(ast: Dlib):
        """
        Unbuilds ``Dlib`` into ``DlibBuilder``

        Returns:
            ``DlibBuilder`` for ``Dlib``.
        """

        return Dlib(
            abx=copy.deepcopy(ast.abx),
        )
