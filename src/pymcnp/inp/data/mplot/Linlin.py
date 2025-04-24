import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Linlin(MplotOption, keyword='linlin'):
    """
    Represents INP linlin elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Alinlin\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Linlin``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class LinlinBuilder:
    """
    Builds ``Linlin``.

    Attributes:

    """

    def build(self):
        """
        Builds ``LinlinBuilder`` into ``Linlin``.

        Returns:
            ``Linlin`` for ``LinlinBuilder``.
        """

        return Linlin()
