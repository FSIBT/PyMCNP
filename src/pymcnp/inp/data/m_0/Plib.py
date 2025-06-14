import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Plib(_option.MOption_0):
    """
    Represents INP plib elements.

    Attributes:
        abx: Default photoatomic table identifier.
    """

    _KEYWORD = 'plib'

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Aplib( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``Plib``.

        Parameters:
            abx: Default photoatomic table identifier.

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
class PlibBuilder(_option.MOptionBuilder_0):
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

        abx = self.abx
        if isinstance(self.abx, types.String):
            abx = self.abx
        elif isinstance(self.abx, str):
            abx = types.String.from_mcnp(self.abx)

        return Plib(
            abx=abx,
        )

    @staticmethod
    def unbuild(ast: Plib):
        """
        Unbuilds ``Plib`` into ``PlibBuilder``

        Returns:
            ``PlibBuilder`` for ``Plib``.
        """

        return PlibBuilder(
            abx=copy.deepcopy(ast.abx),
        )
