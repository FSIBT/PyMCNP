import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Slib(_option.MOption_0):
    """
    Represents INP slib elements.

    Attributes:
        abx: Default helion table identifier.
    """

    _KEYWORD = 'slib'

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Aslib( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``Slib``.

        Parameters:
            abx: Default helion table identifier.

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
class SlibBuilder(_option.MOptionBuilder_0):
    """
    Builds ``Slib``.

    Attributes:
        abx: Default helion table identifier.
    """

    abx: str | types.String

    def build(self):
        """
        Builds ``SlibBuilder`` into ``Slib``.

        Returns:
            ``Slib`` for ``SlibBuilder``.
        """

        abx = self.abx
        if isinstance(self.abx, types.String):
            abx = self.abx
        elif isinstance(self.abx, str):
            abx = types.String.from_mcnp(self.abx)

        return Slib(
            abx=abx,
        )

    @staticmethod
    def unbuild(ast: Slib):
        """
        Unbuilds ``Slib`` into ``SlibBuilder``

        Returns:
            ``SlibBuilder`` for ``Slib``.
        """

        return SlibBuilder(
            abx=copy.deepcopy(ast.abx),
        )
