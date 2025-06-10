import re
import typing
import dataclasses


from . import _option
from .....utils import types


class Line(_option.ContourOption):
    """
    Represents INP line elements.

    Attributes:

    """

    _KEYWORD = 'line'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aline\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Line``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class LineBuilder(_option.ContourOptionBuilder):
    """
    Builds ``Line``.

    Attributes:

    """

    def build(self):
        """
        Builds ``LineBuilder`` into ``Line``.

        Returns:
            ``Line`` for ``LineBuilder``.
        """

        return Line()

    @staticmethod
    def unbuild(ast: Line):
        """
        Unbuilds ``Line`` into ``LineBuilder``

        Returns:
            ``LineBuilder`` for ``Line``.
        """

        return LineBuilder()
