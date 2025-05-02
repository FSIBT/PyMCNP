import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class End(MplotOption):
    """
    Represents INP end elements.

    Attributes:

    """

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
class EndBuilder:
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
