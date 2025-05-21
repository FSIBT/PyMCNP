import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Plinear(MplotOption):
    """
    Represents INP plinear elements.

    Attributes:

    """

    _KEYWORD = 'plinear'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aplinear\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Plinear``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class PlinearBuilder:
    """
    Builds ``Plinear``.

    Attributes:

    """

    def build(self):
        """
        Builds ``PlinearBuilder`` into ``Plinear``.

        Returns:
            ``Plinear`` for ``PlinearBuilder``.
        """

        return Plinear()

    @staticmethod
    def unbuild(ast: Plinear):
        """
        Unbuilds ``Plinear`` into ``PlinearBuilder``

        Returns:
            ``PlinearBuilder`` for ``Plinear``.
        """

        return Plinear()
