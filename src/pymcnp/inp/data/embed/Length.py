import re

from . import _option
from ....utils import types
from ....utils import errors


class Length(_option.EmbedOption):
    """
    Represents INP length elements.

    Attributes:
        factor: Conversion factor to centimeters for all mesh dimentions.
    """

    _KEYWORD = 'length'

    _ATTRS = {
        'factor': types.Real,
    }

    _REGEX = re.compile(rf'\Alength( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, factor: str | int | float | types.Real):
        """
        Initializes ``Length``.

        Parameters:
            factor: Conversion factor to centimeters for all mesh dimentions.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.factor: types.Real = factor

    @property
    def factor(self) -> types.Real:
        """
        Gets ``factor``.

        Returns:
            ``factor``.
        """

        return self._factor

    @factor.setter
    def factor(self, factor: str | int | float | types.Real) -> None:
        """
        Sets ``factor``.

        Parameters:
            factor: Conversion factor to centimeters for all mesh dimentions.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if factor is not None:
            if isinstance(factor, types.Real):
                factor = factor
            elif isinstance(factor, int):
                factor = types.Real(factor)
            elif isinstance(factor, float):
                factor = types.Real(factor)
            elif isinstance(factor, str):
                factor = types.Real.from_mcnp(factor)
            else:
                raise TypeError

        if factor is None or not (factor > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, factor)

        self._factor: types.Real = factor
