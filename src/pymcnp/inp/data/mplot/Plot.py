import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Plot(MplotOption):
    """
    Represents INP plot elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Aplot\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Plot``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class PlotBuilder:
    """
    Builds ``Plot``.

    Attributes:

    """

    def build(self):
        """
        Builds ``PlotBuilder`` into ``Plot``.

        Returns:
            ``Plot`` for ``PlotBuilder``.
        """

        return Plot()
