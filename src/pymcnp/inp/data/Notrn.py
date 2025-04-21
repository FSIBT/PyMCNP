import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types


class Notrn(DataOption, keyword='notrn'):
    """
    Represents INP notrn elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Anotrn\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Notrn``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class NotrnBuilder:
    """
    Builds ``Notrn``.

    Attributes:

    """

    def build(self):
        """
        Builds ``NotrnBuilder`` into ``Notrn``.

        Returns:
            ``Notrn`` for ``NotrnBuilder``.
        """

        return Notrn()
