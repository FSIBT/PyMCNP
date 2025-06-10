import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Lin(_option.DfOption_1):
    """
    Represents INP lin elements.

    Attributes:

    """

    _KEYWORD = 'lin'

    _ATTRS = {}

    _REGEX = re.compile(r'\Alin\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Lin``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class LinBuilder(_option.DfOptionBuilder_1):
    """
    Builds ``Lin``.

    Attributes:

    """

    def build(self):
        """
        Builds ``LinBuilder`` into ``Lin``.

        Returns:
            ``Lin`` for ``LinBuilder``.
        """

        return Lin()

    @staticmethod
    def unbuild(ast: Lin):
        """
        Unbuilds ``Lin`` into ``LinBuilder``

        Returns:
            ``LinBuilder`` for ``Lin``.
        """

        return LinBuilder()
