import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types


class Za(_option.DataOption):
    """
    Represents INP za elements.

    Attributes:
        anything: Any parameters.
    """

    _KEYWORD = 'za'

    _ATTRS = {
        'anything': types.String,
    }

    _REGEX = re.compile(rf'\Aza( {types.String._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, anything: types.String = None):
        """
        Initializes ``Za``.

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
class ZaBuilder(_option.DataOptionBuilder):
    """
    Builds ``Za``.

    Attributes:
        anything: Any parameters.
    """

    anything: str | types.String = None

    def build(self):
        """
        Builds ``ZaBuilder`` into ``Za``.

        Returns:
            ``Za`` for ``ZaBuilder``.
        """

        anything = self.anything
        if isinstance(self.anything, types.String):
            anything = self.anything
        elif isinstance(self.anything, str):
            anything = types.String.from_mcnp(self.anything)

        return Za(
            anything=anything,
        )

    @staticmethod
    def unbuild(ast: Za):
        """
        Unbuilds ``Za`` into ``ZaBuilder``

        Returns:
            ``ZaBuilder`` for ``Za``.
        """

        return ZaBuilder(
            anything=copy.deepcopy(ast.anything),
        )
