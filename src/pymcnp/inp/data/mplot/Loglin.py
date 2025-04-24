import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Loglin(MplotOption, keyword='loglin'):
    """
    Represents INP loglin elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Aloglin\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Loglin``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class LoglinBuilder:
    """
    Builds ``Loglin``.

    Attributes:

    """

    def build(self):
        """
        Builds ``LoglinBuilder`` into ``Loglin``.

        Returns:
            ``Loglin`` for ``LoglinBuilder``.
        """

        return Loglin()
