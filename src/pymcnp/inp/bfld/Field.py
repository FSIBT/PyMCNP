import re

from . import _option
from ... import types
from ... import errors


class Field(_option.BfldOption):
    """
    Represents INP `field` elements.
    """

    _KEYWORD = 'field'

    _ATTRS = {
        'strength_gradient': types.Real,
    }

    _REGEX = re.compile(rf'\Afield( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, strength_gradient: str | int | float | types.Real):
        """
        Initializes `Field`.

        Parameters:
            strength_gradient: Magnetic field strength/gradient.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.strength_gradient: types.Real = strength_gradient

    @property
    def strength_gradient(self) -> types.Real:
        """
        Magnetic field strength/gradient

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._strength_gradient

    @strength_gradient.setter
    def strength_gradient(self, strength_gradient: str | int | float | types.Real) -> None:
        """
        Sets `strength_gradient`.

        Parameters:
            strength_gradient: Magnetic field strength/gradient.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if strength_gradient is not None:
            if isinstance(strength_gradient, types.Real):
                strength_gradient = strength_gradient
            elif isinstance(strength_gradient, int) or isinstance(strength_gradient, float):
                strength_gradient = types.Real(strength_gradient)
            elif isinstance(strength_gradient, str):
                strength_gradient = types.Real.from_mcnp(strength_gradient)

        if strength_gradient is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, strength_gradient)

        self._strength_gradient: types.Real = strength_gradient
