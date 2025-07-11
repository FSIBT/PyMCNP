import re

from . import _option
from ....utils import types
from ....utils import errors


class Field(_option.BfldOption):
    """
    Represents INP field elements.

    Attributes:
        strength_gradient: Magnetic field strength/gradient.
    """

    _KEYWORD = 'field'

    _ATTRS = {
        'strength_gradient': types.Real,
    }

    _REGEX = re.compile(rf'\Afield( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, strength_gradient: str | int | float | types.Real):
        """
        Initializes ``Field``.

        Parameters:
            strength_gradient: Magnetic field strength/gradient.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.strength_gradient: types.Real = strength_gradient

    @property
    def strength_gradient(self) -> types.Real:
        """
        Gets ``strength_gradient``.

        Returns:
            ``strength_gradient``.
        """

        return self._strength_gradient

    @strength_gradient.setter
    def strength_gradient(self, strength_gradient: str | int | float | types.Real) -> None:
        """
        Sets ``strength_gradient``.

        Parameters:
            strength_gradient: Magnetic field strength/gradient.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if strength_gradient is not None:
            if isinstance(strength_gradient, types.Real):
                strength_gradient = strength_gradient
            elif isinstance(strength_gradient, int):
                strength_gradient = types.Real(strength_gradient)
            elif isinstance(strength_gradient, float):
                strength_gradient = types.Real(strength_gradient)
            elif isinstance(strength_gradient, str):
                strength_gradient = types.Real.from_mcnp(strength_gradient)
            else:
                raise TypeError

        if strength_gradient is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, strength_gradient)

        self._strength_gradient: types.Real = strength_gradient
