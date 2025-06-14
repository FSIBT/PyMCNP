import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Imp(_option.CellOption):
    """
    Represents INP imp elements.

    Attributes:
        designator: Data option particle designator.
        importance: Cell particle importance.
    """

    _KEYWORD = 'imp'

    _ATTRS = {
        'designator': types.Designator,
        'importance': types.Real,
    }

    _REGEX = re.compile(rf'\Aimp:(\S+)( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, designator: types.Designator, importance: types.Real):
        """
        Initializes ``Imp``.

        Parameters:
            designator: Data option particle designator.
            importance: Cell particle importance.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if importance is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, importance)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                importance,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.importance: typing.Final[types.Real] = importance


@dataclasses.dataclass
class ImpBuilder(_option.CellOptionBuilder):
    """
    Builds ``Imp``.

    Attributes:
        designator: Data option particle designator.
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

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        importance = self.importance
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

    @staticmethod
    def unbuild(ast: Imp):
        """
        Unbuilds ``Imp`` into ``ImpBuilder``

        Returns:
            ``ImpBuilder`` for ``Imp``.
        """

        return ImpBuilder(
            designator=copy.deepcopy(ast.designator),
            importance=copy.deepcopy(ast.importance),
        )
