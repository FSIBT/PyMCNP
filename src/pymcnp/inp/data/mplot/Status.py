import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Status(MplotOption):
    """
    Represents INP status elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Astatus\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Status``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class StatusBuilder:
    """
    Builds ``Status``.

    Attributes:

    """

    def build(self):
        """
        Builds ``StatusBuilder`` into ``Status``.

        Returns:
            ``Status`` for ``StatusBuilder``.
        """

        return Status()
