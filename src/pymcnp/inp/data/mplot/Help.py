import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Help(_option.MplotOption):
    """
    Represents INP help elements.

    Attributes:

    """

    _KEYWORD = 'help'

    _ATTRS = {}

    _REGEX = re.compile(r'\Ahelp\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Help``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class HelpBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Help``.

    Attributes:

    """

    def build(self):
        """
        Builds ``HelpBuilder`` into ``Help``.

        Returns:
            ``Help`` for ``HelpBuilder``.
        """

        return Help()

    @staticmethod
    def unbuild(ast: Help):
        """
        Unbuilds ``Help`` into ``HelpBuilder``

        Returns:
            ``HelpBuilder`` for ``Help``.
        """

        return HelpBuilder()
