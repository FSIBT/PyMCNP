import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Nonorm(MplotOption):
    """
    Represents INP nonorm elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Anonorm\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Nonorm``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class NonormBuilder:
    """
    Builds ``Nonorm``.

    Attributes:

    """

    def build(self):
        """
        Builds ``NonormBuilder`` into ``Nonorm``.

        Returns:
            ``Nonorm`` for ``NonormBuilder``.
        """

        return Nonorm()
