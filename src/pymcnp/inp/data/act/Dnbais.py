import re
import copy
import typing
import dataclasses


from ._option import ActOption
from ....utils import types
from ....utils import errors


class Dnbais(ActOption):
    """
    Represents INP dnbais elements.

    Attributes:
        count: Maximum number of neutrons generated per reaction.
    """

    _KEYWORD = 'dnbais'

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'\Adnbais( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``Dnbais``.

        Parameters:
            count: Maximum number of neutrons generated per reaction.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if count is None or not (0 <= count.value <= 10):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, count)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                count,
            ]
        )

        self.count: typing.Final[types.Integer] = count


@dataclasses.dataclass
class DnbaisBuilder:
    """
    Builds ``Dnbais``.

    Attributes:
        count: Maximum number of neutrons generated per reaction.
    """

    count: str | int | types.Integer

    def build(self):
        """
        Builds ``DnbaisBuilder`` into ``Dnbais``.

        Returns:
            ``Dnbais`` for ``DnbaisBuilder``.
        """

        count = self.count
        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.Integer(self.count)
        elif isinstance(self.count, str):
            count = types.Integer.from_mcnp(self.count)

        return Dnbais(
            count=count,
        )

    @staticmethod
    def unbuild(ast: Dnbais):
        """
        Unbuilds ``Dnbais`` into ``DnbaisBuilder``

        Returns:
            ``DnbaisBuilder`` for ``Dnbais``.
        """

        return Dnbais(
            count=copy.deepcopy(ast.count),
        )
