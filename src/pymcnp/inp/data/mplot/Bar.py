import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Bar(_option.MplotOption):
    """
    Represents INP bar elements.

    Attributes:

    """

    _KEYWORD = 'bar'

    _ATTRS = {}

    _REGEX = re.compile(r'\Abar\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Bar``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class BarBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Bar``.

    Attributes:

    """

    def build(self):
        """
        Builds ``BarBuilder`` into ``Bar``.

        Returns:
            ``Bar`` for ``BarBuilder``.
        """

        return Bar()

    @staticmethod
    def unbuild(ast: Bar):
        """
        Unbuilds ``Bar`` into ``BarBuilder``

        Returns:
            ``BarBuilder`` for ``Bar``.
        """

        return BarBuilder()
