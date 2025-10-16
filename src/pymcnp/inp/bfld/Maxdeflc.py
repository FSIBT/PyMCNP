import re

from . import _option
from ... import types
from ... import errors


class Maxdeflc(_option.BfldOption):
    """
    Represents INP `maxdeflc` elements.
    """

    _KEYWORD = 'maxdeflc'

    _ATTRS = {
        'angle': types.Real,
    }

    _REGEX = re.compile(rf'\Amaxdeflc( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, angle: str | int | float | types.Real):
        """
        Initializes `Maxdeflc`.

        Parameters:
            angle: Maximum deflection angles.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.angle: types.Real = angle

    @property
    def angle(self) -> types.Real:
        """
        Maximum deflection angles

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._angle

    @angle.setter
    def angle(self, angle: str | int | float | types.Real) -> None:
        """
        Sets `angle`.

        Parameters:
            angle: Maximum deflection angles.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if angle is not None:
            if isinstance(angle, types.Real):
                angle = angle
            elif isinstance(angle, int) or isinstance(angle, float):
                angle = types.Real(angle)
            elif isinstance(angle, str):
                angle = types.Real.from_mcnp(angle)

        if angle is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, angle)

        self._angle: types.Real = angle
