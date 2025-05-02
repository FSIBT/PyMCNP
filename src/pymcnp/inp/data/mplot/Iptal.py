import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Iptal(MplotOption):
    """
    Represents INP iptal elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Aiptal\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Iptal``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class IptalBuilder:
    """
    Builds ``Iptal``.

    Attributes:

    """

    def build(self):
        """
        Builds ``IptalBuilder`` into ``Iptal``.

        Returns:
            ``Iptal`` for ``IptalBuilder``.
        """

        return Iptal()
