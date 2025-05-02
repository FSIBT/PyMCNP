import re
import typing
import dataclasses


from ._option import FreeOption
from .....utils import types


class Noall(FreeOption):
    """
    Represents INP noall elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Anoall\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Noall``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class NoallBuilder:
    """
    Builds ``Noall``.

    Attributes:

    """

    def build(self):
        """
        Builds ``NoallBuilder`` into ``Noall``.

        Returns:
            ``Noall`` for ``NoallBuilder``.
        """

        return Noall()
