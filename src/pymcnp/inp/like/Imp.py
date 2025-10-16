import re

from . import _option
from ... import types
from ... import errors


class Imp(_option.LikeOption):
    """
    Represents INP `imp` elements.
    """

    _KEYWORD = 'imp'

    _ATTRS = {
        'designator': types.Designator,
        'importance': types.Real,
    }

    _REGEX = re.compile(rf'\Aimp:(\S+)( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, designator: str | types.Designator, importance: str | int | float | types.Real):
        """
        Initializes `Imp`.

        Parameters:
            designator: Data option particle designator.
            importance: Cell particle importance.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.designator: types.Designator = designator
        self.importance: types.Real = importance

    @property
    def designator(self) -> types.Designator:
        """
        Gets `designator`.

        Returns:
            `designator`.
        """

        return self._designator

    @designator.setter
    def designator(self, designator: str | types.Designator) -> None:
        """
        Sets `designator`.

        Parameters:
            designator: Data option particle designator.

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
    def importance(self) -> types.Real:
        """
        Gets `importance`.

        Returns:
            `importance`.
        """

        return self._importance

    @importance.setter
    def importance(self, importance: str | int | float | types.Real) -> None:
        """
        Sets `importance`.

        Parameters:
            importance: Cell particle importance.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if importance is not None:
            if isinstance(importance, types.Real):
                importance = importance
            elif isinstance(importance, int) or isinstance(importance, float):
                importance = types.Real(importance)
            elif isinstance(importance, str):
                importance = types.Real.from_mcnp(importance)

        if importance is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, importance)

        self._importance: types.Real = importance
