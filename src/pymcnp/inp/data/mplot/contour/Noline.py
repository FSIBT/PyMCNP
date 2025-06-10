import re
import typing
import dataclasses


from . import _option
from .....utils import types


class Noline(_option.ContourOption):
    """
    Represents INP noline elements.

    Attributes:

    """

    _KEYWORD = 'noline'

    _ATTRS = {}

    _REGEX = re.compile(r'\Anoline\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Noline``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class NolineBuilder(_option.ContourOptionBuilder):
    """
    Builds ``Noline``.

    Attributes:

    """

    def build(self):
        """
        Builds ``NolineBuilder`` into ``Noline``.

        Returns:
            ``Noline`` for ``NolineBuilder``.
        """

        return Noline()

    @staticmethod
    def unbuild(ast: Noline):
        """
        Unbuilds ``Noline`` into ``NolineBuilder``

        Returns:
            ``NolineBuilder`` for ``Noline``.
        """

        return NolineBuilder()
