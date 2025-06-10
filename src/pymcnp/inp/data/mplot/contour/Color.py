import re
import typing
import dataclasses


from . import _option
from .....utils import types


class Color(_option.ContourOption):
    """
    Represents INP color elements.

    Attributes:

    """

    _KEYWORD = 'color'

    _ATTRS = {}

    _REGEX = re.compile(r'\Acolor\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Color``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class ColorBuilder(_option.ContourOptionBuilder):
    """
    Builds ``Color``.

    Attributes:

    """

    def build(self):
        """
        Builds ``ColorBuilder`` into ``Color``.

        Returns:
            ``Color`` for ``ColorBuilder``.
        """

        return Color()

    @staticmethod
    def unbuild(ast: Color):
        """
        Unbuilds ``Color`` into ``ColorBuilder``

        Returns:
            ``ColorBuilder`` for ``Color``.
        """

        return ColorBuilder()
