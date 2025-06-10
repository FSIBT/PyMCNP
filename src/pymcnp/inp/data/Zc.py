import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types


class Zc(_option.DataOption):
    """
    Represents INP zc elements.

    Attributes:
        anything: Any parameters.
    """

    _KEYWORD = 'zc'

    _ATTRS = {
        'anything': types.String,
    }

    _REGEX = re.compile(rf'\Azc( {types.String._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, anything: types.String = None):
        """
        Initializes ``Zc``.

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
class ZcBuilder(_option.DataOptionBuilder):
    """
    Builds ``Zc``.

    Attributes:
        anything: Any parameters.
    """

    anything: str | types.String = None

    def build(self):
        """
        Builds ``ZcBuilder`` into ``Zc``.

        Returns:
            ``Zc`` for ``ZcBuilder``.
        """

        anything = self.anything
        if isinstance(self.anything, types.String):
            anything = self.anything
        elif isinstance(self.anything, str):
            anything = types.String.from_mcnp(self.anything)

        return Zc(
            anything=anything,
        )

    @staticmethod
    def unbuild(ast: Zc):
        """
        Unbuilds ``Zc`` into ``ZcBuilder``

        Returns:
            ``ZcBuilder`` for ``Zc``.
        """

        return ZcBuilder(
            anything=copy.deepcopy(ast.anything),
        )
