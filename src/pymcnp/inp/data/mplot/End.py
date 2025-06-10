import re
import typing
import dataclasses


from . import _option
from ....utils import types


class End(_option.MplotOption):
    """
    Represents INP end elements.

    Attributes:

    """

    _KEYWORD = 'end'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aend\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``End``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class EndBuilder(_option.MplotOptionBuilder):
    """
    Builds ``End``.

    Attributes:

    """

    def build(self):
        """
        Builds ``EndBuilder`` into ``End``.

        Returns:
            ``End`` for ``EndBuilder``.
        """

        return End()

    @staticmethod
    def unbuild(ast: End):
        """
        Unbuilds ``End`` into ``EndBuilder``

        Returns:
            ``EndBuilder`` for ``End``.
        """

        return EndBuilder()
