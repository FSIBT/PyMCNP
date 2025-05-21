import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Lethargy(MplotOption):
    """
    Represents INP lethargy elements.

    Attributes:

    """

    _KEYWORD = 'lethargy'

    _ATTRS = {}

    _REGEX = re.compile(r'\Alethargy\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Lethargy``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class LethargyBuilder:
    """
    Builds ``Lethargy``.

    Attributes:

    """

    def build(self):
        """
        Builds ``LethargyBuilder`` into ``Lethargy``.

        Returns:
            ``Lethargy`` for ``LethargyBuilder``.
        """

        return Lethargy()

    @staticmethod
    def unbuild(ast: Lethargy):
        """
        Unbuilds ``Lethargy`` into ``LethargyBuilder``

        Returns:
            ``LethargyBuilder`` for ``Lethargy``.
        """

        return Lethargy()
