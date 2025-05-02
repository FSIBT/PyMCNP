import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Help(MplotOption):
    """
    Represents INP help elements.

    Attributes:

    """

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
class HelpBuilder:
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
