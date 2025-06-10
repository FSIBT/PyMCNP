import re
import typing
import dataclasses


from . import _option
from .....utils import types


class All(_option.ContourOption):
    """
    Represents INP all elements.

    Attributes:

    """

    _KEYWORD = 'all'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aall\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``All``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class AllBuilder(_option.ContourOptionBuilder):
    """
    Builds ``All``.

    Attributes:

    """

    def build(self):
        """
        Builds ``AllBuilder`` into ``All``.

        Returns:
            ``All`` for ``AllBuilder``.
        """

        return All()

    @staticmethod
    def unbuild(ast: All):
        """
        Unbuilds ``All`` into ``AllBuilder``

        Returns:
            ``AllBuilder`` for ``All``.
        """

        return AllBuilder()
