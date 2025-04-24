import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Options(MplotOption, keyword='options'):
    """
    Represents INP options elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Aoptions\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Options``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class OptionsBuilder:
    """
    Builds ``Options``.

    Attributes:

    """

    def build(self):
        """
        Builds ``OptionsBuilder`` into ``Options``.

        Returns:
            ``Options`` for ``OptionsBuilder``.
        """

        return Options()
