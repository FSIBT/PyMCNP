import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Thin(MplotOption):
    """
    Represents INP thin elements.

    Attributes:

    """

    _KEYWORD = 'thin'

    _ATTRS = {}

    _REGEX = re.compile(r'\Athin\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Thin``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class ThinBuilder:
    """
    Builds ``Thin``.

    Attributes:

    """

    def build(self):
        """
        Builds ``ThinBuilder`` into ``Thin``.

        Returns:
            ``Thin`` for ``ThinBuilder``.
        """

        return Thin()

    @staticmethod
    def unbuild(ast: Thin):
        """
        Unbuilds ``Thin`` into ``ThinBuilder``

        Returns:
            ``ThinBuilder`` for ``Thin``.
        """

        return Thin()
