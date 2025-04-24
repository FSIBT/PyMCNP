import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Hist(MplotOption, keyword='hist'):
    """
    Represents INP hist elements.

    Attributes:

    """

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
class HistBuilder:
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
