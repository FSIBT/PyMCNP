import re

from . import _option
from ....utils import types
from ....utils import errors


class Thresh(_option.ActOption):
    """
    Represents INP thresh elements.

    Attributes:
        fraction: Fraction of highest-amplitude discrete delayed-gamma lines retained.
    """

    _KEYWORD = 'thresh'

    _ATTRS = {
        'fraction': types.Real,
    }

    _REGEX = re.compile(rf'\Athresh( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, fraction: str | int | float | types.Real):
        """
        Initializes ``Thresh``.

        Parameters:
            fraction: Fraction of highest-amplitude discrete delayed-gamma lines retained.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.fraction: types.Real = fraction

    @property
    def fraction(self) -> types.Real:
        """
        Gets ``fraction``.

        Returns:
            ``fraction``.
        """

        return self._fraction

    @fraction.setter
    def fraction(self, fraction: str | int | float | types.Real) -> None:
        """
        Sets ``fraction``.

        Parameters:
            fraction: Fraction of highest-amplitude discrete delayed-gamma lines retained.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if fraction is not None:
            if isinstance(fraction, types.Real):
                fraction = fraction
            elif isinstance(fraction, int):
                fraction = types.Real(fraction)
            elif isinstance(fraction, float):
                fraction = types.Real(fraction)
            elif isinstance(fraction, str):
                fraction = types.Real.from_mcnp(fraction)
            else:
                raise TypeError

        if fraction is None or not (fraction >= 0 and fraction <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fraction)

        self._fraction: types.Real = fraction
