import re
import typing
import dataclasses


from ._option import ContourOption
from .....utils import types


class Lin(ContourOption):
    """
    Represents INP lin elements.

    Attributes:

    """

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
class LinBuilder:
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
