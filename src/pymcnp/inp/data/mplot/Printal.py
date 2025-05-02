import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Printal(MplotOption):
    """
    Represents INP printal elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Aprintal\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Printal``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class PrintalBuilder:
    """
    Builds ``Printal``.

    Attributes:

    """

    def build(self):
        """
        Builds ``PrintalBuilder`` into ``Printal``.

        Returns:
            ``Printal`` for ``PrintalBuilder``.
        """

        return Printal()
