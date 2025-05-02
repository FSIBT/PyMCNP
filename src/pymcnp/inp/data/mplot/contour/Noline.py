import re
import typing
import dataclasses


from ._option import ContourOption
from .....utils import types


class Noline(ContourOption):
    """
    Represents INP noline elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Anoline\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Noline``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class NolineBuilder:
    """
    Builds ``Noline``.

    Attributes:

    """

    def build(self):
        """
        Builds ``NolineBuilder`` into ``Noline``.

        Returns:
            ``Noline`` for ``NolineBuilder``.
        """

        return Noline()
