import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Tfc(_option.MplotOption):
    """
    Represents INP tfc elements.

    Attributes:
        x: Independent variable selector.
    """

    _KEYWORD = 'tfc'

    _ATTRS = {
        'x': types.String,
    }

    _REGEX = re.compile(rf'\Atfc( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, x: types.String):
        """
        Initializes ``Tfc``.

        Parameters:
            x: Independent variable selector.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
            ]
        )

        self.x: typing.Final[types.String] = x


@dataclasses.dataclass
class TfcBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Tfc``.

    Attributes:
        x: Independent variable selector.
    """

    x: str | types.String

    def build(self):
        """
        Builds ``TfcBuilder`` into ``Tfc``.

        Returns:
            ``Tfc`` for ``TfcBuilder``.
        """

        x = self.x
        if isinstance(self.x, types.String):
            x = self.x
        elif isinstance(self.x, str):
            x = types.String.from_mcnp(self.x)

        return Tfc(
            x=x,
        )

    @staticmethod
    def unbuild(ast: Tfc):
        """
        Unbuilds ``Tfc`` into ``TfcBuilder``

        Returns:
            ``TfcBuilder`` for ``Tfc``.
        """

        return TfcBuilder(
            x=copy.deepcopy(ast.x),
        )
