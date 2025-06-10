import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Hist(_option.MplotOption):
    """
    Represents INP hist elements.

    Attributes:

    """

    _KEYWORD = 'hist'

    _ATTRS = {}

    _REGEX = re.compile(r'\Ahist\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Hist``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class HistBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Hist``.

    Attributes:

    """

    def build(self):
        """
        Builds ``HistBuilder`` into ``Hist``.

        Returns:
            ``Hist`` for ``HistBuilder``.
        """

        return Hist()

    @staticmethod
    def unbuild(ast: Hist):
        """
        Unbuilds ``Hist`` into ``HistBuilder``

        Returns:
            ``HistBuilder`` for ``Hist``.
        """

        return HistBuilder()
