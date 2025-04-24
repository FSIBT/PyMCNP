import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Plinear(MplotOption, keyword='plinear'):
    """
    Represents INP plinear elements.

    Attributes:

    """

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
