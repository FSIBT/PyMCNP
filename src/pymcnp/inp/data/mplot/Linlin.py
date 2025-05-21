import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Linlin(MplotOption):
    """
    Represents INP linlin elements.

    Attributes:

    """

    _KEYWORD = 'linlin'

    _ATTRS = {}

    _REGEX = re.compile(r'\Alinlin\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Linlin``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class LinlinBuilder:
    """
    Builds ``Linlin``.

    Attributes:

    """

    def build(self):
        """
        Builds ``LinlinBuilder`` into ``Linlin``.

        Returns:
            ``Linlin`` for ``LinlinBuilder``.
        """

        return Linlin()

    @staticmethod
    def unbuild(ast: Linlin):
        """
        Unbuilds ``Linlin`` into ``LinlinBuilder``

        Returns:
            ``LinlinBuilder`` for ``Linlin``.
        """

        return Linlin()
