import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Noerrbar(_option.MplotOption):
    """
    Represents INP noerrbar elements.

    Attributes:

    """

    _KEYWORD = 'noerrbar'

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
class NoerrbarBuilder(_option.MplotOptionBuilder):
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

    @staticmethod
    def unbuild(ast: Noerrbar):
        """
        Unbuilds ``Noerrbar`` into ``NoerrbarBuilder``

        Returns:
            ``NoerrbarBuilder`` for ``Noerrbar``.
        """

        return NoerrbarBuilder()
