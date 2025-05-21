import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Linlog(MplotOption):
    """
    Represents INP linlog elements.

    Attributes:

    """

    _KEYWORD = 'linlog'

    _ATTRS = {}

    _REGEX = re.compile(r'\Alinlog\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Linlog``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class LinlogBuilder:
    """
    Builds ``Linlog``.

    Attributes:

    """

    def build(self):
        """
        Builds ``LinlogBuilder`` into ``Linlog``.

        Returns:
            ``Linlog`` for ``LinlogBuilder``.
        """

        return Linlog()

    @staticmethod
    def unbuild(ast: Linlog):
        """
        Unbuilds ``Linlog`` into ``LinlogBuilder``

        Returns:
            ``LinlogBuilder`` for ``Linlog``.
        """

        return Linlog()
