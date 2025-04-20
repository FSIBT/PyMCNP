import re
import typing
import dataclasses


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Imp(CellOption_, keyword='imp'):
    """
    Represents INP imp elements.

    Attributes:
        designator: Particle designator.
        importance: Cell particle importance.
    """

    _ATTRS = {
        'designator': types.Designator,
        'importance': types.Real,
    }

    _REGEX = re.compile(rf'\Aimp:(\S+)( {types.Real._REGEX.pattern})\Z')

    def __init__(self, designator: types.Designator, importance: types.Real):
        """
        Initializes ``Imp``.

        Parameters:
            designator: Particle designator.
            importance: Cell particle importance.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if importance is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, importance)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                importance,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.importance: typing.Final[types.Real] = importance


@dataclasses.dataclass
class ImpBuilder:
    """
    Builds ``Imp``.

    Attributes:
        designator: Particle designator.
        importance: Cell particle importance.
    """

    designator: str | types.Designator
    importance: str | float | types.Real

    def build(self):
        """
        Builds ``ImpBuilder`` into ``Imp``.

        Returns:
            ``Imp`` for ``ImpBuilder``.
        """

        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        if isinstance(self.importance, types.Real):
            importance = self.importance
        elif isinstance(self.importance, float) or isinstance(self.importance, int):
            importance = types.Real(self.importance)
        elif isinstance(self.importance, str):
            importance = types.Real.from_mcnp(self.importance)

        return Imp(
            designator=designator,
            importance=importance,
        )
