import re
import copy
import typing
import dataclasses


from ._option import MOption_0
from ....utils import types
from ....utils import errors


class Tlib(MOption_0):
    """
    Represents INP tlib elements.

    Attributes:
        abx: Default triton table identifier.
    """

    _KEYWORD = 'tlib'

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Atlib( {types.String._REGEX.pattern[2:-2]})\Z')

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

        abx = self.abx
        if isinstance(self.abx, types.String):
            abx = self.abx
        elif isinstance(self.abx, str):
            abx = types.String.from_mcnp(self.abx)

        return Tlib(
            abx=abx,
        )

    @staticmethod
    def unbuild(ast: Tlib):
        """
        Unbuilds ``Tlib`` into ``TlibBuilder``

        Returns:
            ``TlibBuilder`` for ``Tlib``.
        """

        return Tlib(
            abx=copy.deepcopy(ast.abx),
        )
