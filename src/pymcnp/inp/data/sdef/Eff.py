import re

from . import _option
from .... import types
from .... import errors


class Eff(_option.SdefOption):
    """
    Represents INP eff elements.
    """

    _KEYWORD = 'eff'

    _ATTRS = {
        'criterion': types.Real,
    }

    _REGEX = re.compile(rf'\Aeff( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, criterion: str | int | float | types.Real):
        """
        Initializes ``Eff``.

        Parameters:
            criterion: Rejection efficiency criterion for position sampling.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.criterion: types.Real = criterion

    @property
    def criterion(self) -> types.Real:
        """
        Rejection efficiency criterion for position sampling

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._criterion

    @criterion.setter
    def criterion(self, criterion: str | int | float | types.Real) -> None:
        """
        Sets ``criterion``.

        Parameters:
            criterion: Rejection efficiency criterion for position sampling.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if criterion is not None:
            if isinstance(criterion, types.Real):
                criterion = criterion
            elif isinstance(criterion, int) or isinstance(criterion, float):
                criterion = types.Real(criterion)
            elif isinstance(criterion, str):
                criterion = types.Real.from_mcnp(criterion)

        if criterion is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, criterion)

        self._criterion: types.Real = criterion
