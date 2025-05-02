import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Loglog(MplotOption):
    """
    Represents INP loglog elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Aloglog\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Loglog``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class LoglogBuilder:
    """
    Builds ``Loglog``.

    Attributes:

    """

    def build(self):
        """
        Builds ``LoglogBuilder`` into ``Loglog``.

        Returns:
            ``Loglog`` for ``LoglogBuilder``.
        """

        return Loglog()
