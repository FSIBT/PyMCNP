import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Below(_option.MplotOption):
    """
    Represents INP below elements.

    Attributes:

    """

    _KEYWORD = 'below'

    _ATTRS = {}

    _REGEX = re.compile(r'\Abelow\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Below``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class BelowBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Below``.

    Attributes:

    """

    def build(self):
        """
        Builds ``BelowBuilder`` into ``Below``.

        Returns:
            ``Below`` for ``BelowBuilder``.
        """

        return Below()

    @staticmethod
    def unbuild(ast: Below):
        """
        Unbuilds ``Below`` into ``BelowBuilder``

        Returns:
            ``BelowBuilder`` for ``Below``.
        """

        return BelowBuilder()
