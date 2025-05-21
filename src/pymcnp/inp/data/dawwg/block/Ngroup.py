import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Ngroup(BlockOption):
    """
    Represents INP ngroup elements.

    Attributes:
        value: Number of energy groups.
    """

    _KEYWORD = 'ngroup'

    _ATTRS = {
        'value': types.Integer,
    }

    _REGEX = re.compile(rf'\Angroup( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, value: types.Integer):
        """
        Initializes ``Ngroup``.

        Parameters:
            value: Number of energy groups.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if value is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, value)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                value,
            ]
        )

        self.value: typing.Final[types.Integer] = value


@dataclasses.dataclass
class NgroupBuilder:
    """
    Builds ``Ngroup``.

    Attributes:
        value: Number of energy groups.
    """

    value: str | int | types.Integer

    def build(self):
        """
        Builds ``NgroupBuilder`` into ``Ngroup``.

        Returns:
            ``Ngroup`` for ``NgroupBuilder``.
        """

        value = self.value
        if isinstance(self.value, types.Integer):
            value = self.value
        elif isinstance(self.value, int):
            value = types.Integer(self.value)
        elif isinstance(self.value, str):
            value = types.Integer.from_mcnp(self.value)

        return Ngroup(
            value=value,
        )

    @staticmethod
    def unbuild(ast: Ngroup):
        """
        Unbuilds ``Ngroup`` into ``NgroupBuilder``

        Returns:
            ``NgroupBuilder`` for ``Ngroup``.
        """

        return Ngroup(
            value=copy.deepcopy(ast.value),
        )
