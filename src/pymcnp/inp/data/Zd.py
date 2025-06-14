import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types


class Zd(_option.DataOption):
    """
    Represents INP zd elements.

    Attributes:
        anything: Any parameters.
    """

    _KEYWORD = 'zd'

    _ATTRS = {
        'anything': types.String,
    }

    _REGEX = re.compile(rf'\Azd( {types.String._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, anything: types.String = None):
        """
        Initializes ``Zd``.

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
class ZdBuilder(_option.DataOptionBuilder):
    """
    Builds ``Zd``.

    Attributes:
        anything: Any parameters.
    """

    anything: str | types.String = None

    def build(self):
        """
        Builds ``ZdBuilder`` into ``Zd``.

        Returns:
            ``Zd`` for ``ZdBuilder``.
        """

        anything = self.anything
        if isinstance(self.anything, types.String):
            anything = self.anything
        elif isinstance(self.anything, str):
            anything = types.String.from_mcnp(self.anything)

        return Zd(
            anything=anything,
        )

    @staticmethod
    def unbuild(ast: Zd):
        """
        Unbuilds ``Zd`` into ``ZdBuilder``

        Returns:
            ``ZdBuilder`` for ``Zd``.
        """

        return ZdBuilder(
            anything=copy.deepcopy(ast.anything),
        )
