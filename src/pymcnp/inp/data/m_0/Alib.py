import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Alib(_option.MOption_0):
    """
    Represents INP alib elements.

    Attributes:
        abx: Default alpha table identifier.
    """

    _KEYWORD = 'alib'

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Aalib( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``Alib``.

        Parameters:
            abx: Default alpha table identifier.

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
class AlibBuilder(_option.MOptionBuilder_0):
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

        abx = self.abx
        if isinstance(self.abx, types.String):
            abx = self.abx
        elif isinstance(self.abx, str):
            abx = types.String.from_mcnp(self.abx)

        return Alib(
            abx=abx,
        )

    @staticmethod
    def unbuild(ast: Alib):
        """
        Unbuilds ``Alib`` into ``AlibBuilder``

        Returns:
            ``AlibBuilder`` for ``Alib``.
        """

        return AlibBuilder(
            abx=copy.deepcopy(ast.abx),
        )
