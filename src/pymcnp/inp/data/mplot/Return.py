import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Return(_option.MplotOption):
    """
    Represents INP return elements.

    Attributes:

    """

    _KEYWORD = 'return'

    _ATTRS = {}

    _REGEX = re.compile(r'\Areturn\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Return``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class ReturnBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Return``.

    Attributes:

    """

    def build(self):
        """
        Builds ``ReturnBuilder`` into ``Return``.

        Returns:
            ``Return`` for ``ReturnBuilder``.
        """

        return Return()

    @staticmethod
    def unbuild(ast: Return):
        """
        Unbuilds ``Return`` into ``ReturnBuilder``

        Returns:
            ``ReturnBuilder`` for ``Return``.
        """

        return ReturnBuilder()
