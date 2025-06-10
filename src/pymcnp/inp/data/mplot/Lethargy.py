import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Lethargy(_option.MplotOption):
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
class LethargyBuilder(_option.MplotOptionBuilder):
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

        return LethargyBuilder()
