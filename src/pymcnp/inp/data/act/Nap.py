import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Nap(_option.ActOption):
    """
    Represents INP nap elements.

    Attributes:
        count: Number of activation products.
    """

    _KEYWORD = 'nap'

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'\Anap( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``Nap``.

        Parameters:
            count: Number of activation products.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if count is None or not (count.value >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, count)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                count,
            ]
        )

        self.count: typing.Final[types.Integer] = count


@dataclasses.dataclass
class NapBuilder(_option.ActOptionBuilder):
    """
    Builds ``Nap``.

    Attributes:
        count: Number of activation products.
    """

    count: str | int | types.Integer

    def build(self):
        """
        Builds ``NapBuilder`` into ``Nap``.

        Returns:
            ``Nap`` for ``NapBuilder``.
        """

        count = self.count
        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.Integer(self.count)
        elif isinstance(self.count, str):
            count = types.Integer.from_mcnp(self.count)

        return Nap(
            count=count,
        )

    @staticmethod
    def unbuild(ast: Nap):
        """
        Unbuilds ``Nap`` into ``NapBuilder``

        Returns:
            ``NapBuilder`` for ``Nap``.
        """

        return NapBuilder(
            count=copy.deepcopy(ast.count),
        )
