import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Return(MplotOption):
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
class ReturnBuilder:
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

        return Return()
