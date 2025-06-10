import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Iptal(_option.MplotOption):
    """
    Represents INP iptal elements.

    Attributes:

    """

    _KEYWORD = 'iptal'

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
class IptalBuilder(_option.MplotOptionBuilder):
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

    @staticmethod
    def unbuild(ast: Iptal):
        """
        Unbuilds ``Iptal`` into ``IptalBuilder``

        Returns:
            ``IptalBuilder`` for ``Iptal``.
        """

        return IptalBuilder()
