import re
import typing
import dataclasses

from ._option import Df_1Option
from ....utils import types
from ....utils import errors


class Lin(Df_1Option, keyword='log'):
    """
    Represents INP log elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Alog\Z')

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


