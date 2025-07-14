import re

from . import _option
from ...utils import types
from ...utils import errors


class Imp(_option.DataOption):
    """
    Represents INP imp elements.
    """

    _KEYWORD = 'imp'

    _ATTRS = {
        'designator': types.Designator,
        'importances': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aimp:(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, designator: str | types.Designator, importances: list[str] | list[float] | list[types.Real]):
        """
        Initializes ``Imp``.

        Parameters:
            designator: Data card particle designator.
            importances: Cell importance.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.designator: types.Designator = designator
        self.importances: types.Tuple[types.Real] = importances

    @property
    def designator(self) -> types.Designator:
        """
        Data card particle designator

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._designator

    @designator.setter
    def designator(self, designator: str | types.Designator) -> None:
        """
        Sets ``designator``.

        Parameters:
            designator: Data card particle designator.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if designator is not None:
            if isinstance(designator, types.Designator):
                designator = designator
            elif isinstance(designator, str):
                designator = types.Designator.from_mcnp(designator)

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)

        self._designator: types.Designator = designator

    @property
    def importances(self) -> types.Tuple[types.Real]:
        """
        Cell importance

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._importances

    @importances.setter
    def importances(self, importances: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets ``importances``.

        Parameters:
            importances: Cell importance.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if importances is not None:
            array = []
            for item in importances:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            importances = types.Tuple(array)

        if importances is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, importances)

        self._importances: types.Tuple[types.Real] = importances
