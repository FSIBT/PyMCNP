import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Nonorm(_option.MplotOption):
    """
    Represents INP nonorm elements.

    Attributes:

    """

    _KEYWORD = 'nonorm'

    _ATTRS = {}

    _REGEX = re.compile(r'\Anonorm\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Nonorm``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class NonormBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Nonorm``.

    Attributes:

    """

    def build(self):
        """
        Builds ``NonormBuilder`` into ``Nonorm``.

        Returns:
            ``Nonorm`` for ``NonormBuilder``.
        """

        return Nonorm()

    @staticmethod
    def unbuild(ast: Nonorm):
        """
        Unbuilds ``Nonorm`` into ``NonormBuilder``

        Returns:
            ``NonormBuilder`` for ``Nonorm``.
        """

        return NonormBuilder()
