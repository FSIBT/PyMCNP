import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Imp(DataOption, keyword='imp'):
    """
    Represents INP imp elements.

    Attributes:
        designator: Data card particle designator.
        importances: Cell importance.
    """

    _ATTRS = {
        'designator': types.Designator,
        'importances': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aimp:(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, designator: types.Designator, importances: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Imp``.

        Parameters:
            designator: Data card particle designator.
            importances: Cell importance.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if importances is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, importances)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                importances,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.importances: typing.Final[types.Tuple[types.RealOrJump]] = importances


@dataclasses.dataclass
class ImpBuilder:
    """
    Builds ``Imp``.

    Attributes:
        designator: Data card particle designator.
        importances: Cell importance.
    """

    designator: str | types.Designator
    importances: list[str] | list[float] | list[types.RealOrJump]

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

        importances = []
        for item in self.importances:
            if isinstance(item, types.RealOrJump):
                importances.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                importances.append(types.RealOrJump(item))
            elif isinstance(item, str):
                importances.append(types.RealOrJump.from_mcnp(item))
        importances = types.Tuple(importances)

        return Imp(
            designator=designator,
            importances=importances,
        )
