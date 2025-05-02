import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Bar(MplotOption):
    """
    Represents INP bar elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Abar\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Bar``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class BarBuilder:
    """
    Builds ``Bar``.

    Attributes:

    """

    def build(self):
        """
        Builds ``BarBuilder`` into ``Bar``.

        Returns:
            ``Bar`` for ``BarBuilder``.
        """

        return Bar()
