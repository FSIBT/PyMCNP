import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Hlib(_option.MOption_0):
    """
    Represents INP hlib elements.

    Attributes:
        abx: Default proton table identifier.
    """

    _KEYWORD = 'hlib'

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Ahlib( {types.String._REGEX.pattern[2:-2]})\Z')

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
class HlibBuilder(_option.MOptionBuilder_0):
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

        abx = self.abx
        if isinstance(self.abx, types.String):
            abx = self.abx
        elif isinstance(self.abx, str):
            abx = types.String.from_mcnp(self.abx)

        return Hlib(
            abx=abx,
        )

    @staticmethod
    def unbuild(ast: Hlib):
        """
        Unbuilds ``Hlib`` into ``HlibBuilder``

        Returns:
            ``HlibBuilder`` for ``Hlib``.
        """

        return HlibBuilder(
            abx=copy.deepcopy(ast.abx),
        )
