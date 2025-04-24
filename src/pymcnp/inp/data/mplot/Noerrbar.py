import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Noerrbar(MplotOption, keyword='noerrbar'):
    """
    Represents INP noerrbar elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Anoerrbar\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Noerrbar``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class NoerrbarBuilder:
    """
    Builds ``Noerrbar``.

    Attributes:

    """

    def build(self):
        """
        Builds ``NoerrbarBuilder`` into ``Noerrbar``.

        Returns:
            ``Noerrbar`` for ``NoerrbarBuilder``.
        """

        return Noerrbar()
