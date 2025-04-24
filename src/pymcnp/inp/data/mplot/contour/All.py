import re
import typing
import dataclasses


from ._option import ContourOption
from .....utils import types


class All(ContourOption, keyword='all'):
    """
    Represents INP all elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Aall\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``All``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class AllBuilder:
    """
    Builds ``All``.

    Attributes:

    """

    def build(self):
        """
        Builds ``AllBuilder`` into ``All``.

        Returns:
            ``All`` for ``AllBuilder``.
        """

        return All()
