import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Elib(_option.MOption_0):
    """
    Represents INP elib elements.

    Attributes:
        abx: Default electron table identifier.
    """

    _KEYWORD = 'elib'

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Aelib( {types.String._REGEX.pattern[2:-2]})\Z')

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
class ElibBuilder(_option.MOptionBuilder_0):
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

        abx = self.abx
        if isinstance(self.abx, types.String):
            abx = self.abx
        elif isinstance(self.abx, str):
            abx = types.String.from_mcnp(self.abx)

        return Elib(
            abx=abx,
        )

    @staticmethod
    def unbuild(ast: Elib):
        """
        Unbuilds ``Elib`` into ``ElibBuilder``

        Returns:
            ``ElibBuilder`` for ``Elib``.
        """

        return ElibBuilder(
            abx=copy.deepcopy(ast.abx),
        )
