import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Below(MplotOption):
    """
    Represents INP below elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Abelow\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Below``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class BelowBuilder:
    """
    Builds ``Below``.

    Attributes:

    """

    def build(self):
        """
        Builds ``BelowBuilder`` into ``Below``.

        Returns:
            ``Below`` for ``BelowBuilder``.
        """

        return Below()
