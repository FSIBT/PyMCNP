import re

from . import _option
from ... import types
from ... import errors


class Length(_option.EmbedOption):
    """
    Represents INP `length` elements.
    """

    _KEYWORD = 'length'

    _ATTRS = {
        'factor': types.Real,
    }

    _REGEX = re.compile(rf'\Alength( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, factor: str | int | float | types.Real):
        """
        Initializes `Length`.

        Parameters:
            factor: Conversion factor to centimeters for all mesh dimentions.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.factor: types.Real = factor

    @property
    def factor(self) -> types.Real:
        """
        Conversion factor to centimeters for all mesh dimentions

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._factor

    @factor.setter
    def factor(self, factor: str | int | float | types.Real) -> None:
        """
        Sets `factor`.

        Parameters:
            factor: Conversion factor to centimeters for all mesh dimentions.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if factor is not None:
            if isinstance(factor, types.Real):
                factor = factor
            elif isinstance(factor, int) or isinstance(factor, float):
                factor = types.Real(factor)
            elif isinstance(factor, str):
                factor = types.Real.from_mcnp(factor)

        if factor is None or not (factor > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, factor)

        self._factor: types.Real = factor
