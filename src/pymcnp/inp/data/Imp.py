import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Imp(_option.DataOption):
    """
    Represents INP imp elements.

    Attributes:
        designator: Data card particle designator.
        importances: Cell importance.
    """

    _KEYWORD = 'imp'

    _ATTRS = {
        'designator': types.Designator,
        'importances': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aimp:(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, designator: types.Designator, importances: types.Tuple[types.Real]):
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
        self.importances: typing.Final[types.Tuple[types.Real]] = importances


@dataclasses.dataclass
class ImpBuilder(_option.DataOptionBuilder):
    """
    Builds ``Imp``.

    Attributes:
        designator: Data card particle designator.
        importances: Cell importance.
    """

    designator: str | types.Designator
    importances: list[str] | list[float] | list[types.Real]

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

        if self.importances:
            importances = []
            for item in self.importances:
                if isinstance(item, types.Real):
                    importances.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    importances.append(types.Real(item))
                elif isinstance(item, str):
                    importances.append(types.Real.from_mcnp(item))
            importances = types.Tuple(importances)
        else:
            importances = None

        return Imp(
            designator=designator,
            importances=importances,
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
            importances=copy.deepcopy(ast.importances),
        )
