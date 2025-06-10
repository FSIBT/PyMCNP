import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types


class Zb(_option.DataOption):
    """
    Represents INP zb elements.

    Attributes:
        anything: Any parameters.
    """

    _KEYWORD = 'zb'

    _ATTRS = {
        'anything': types.String,
    }

    _REGEX = re.compile(rf'\Azb( {types.String._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, anything: types.String = None):
        """
        Initializes ``Zb``.

        Parameters:
            anything: Any parameters.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                anything,
            ]
        )

        self.anything: typing.Final[types.String] = anything


@dataclasses.dataclass
class ZbBuilder(_option.DataOptionBuilder):
    """
    Builds ``Zb``.

    Attributes:
        anything: Any parameters.
    """

    anything: str | types.String = None

    def build(self):
        """
        Builds ``ZbBuilder`` into ``Zb``.

        Returns:
            ``Zb`` for ``ZbBuilder``.
        """

        anything = self.anything
        if isinstance(self.anything, types.String):
            anything = self.anything
        elif isinstance(self.anything, str):
            anything = types.String.from_mcnp(self.anything)

        return Zb(
            anything=anything,
        )

    @staticmethod
    def unbuild(ast: Zb):
        """
        Unbuilds ``Zb`` into ``ZbBuilder``

        Returns:
            ``ZbBuilder`` for ``Zb``.
        """

        return ZbBuilder(
            anything=copy.deepcopy(ast.anything),
        )
