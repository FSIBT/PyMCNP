import re

from . import _option
from ... import types
from ... import errors


class Width(_option.FmultOption):
    """
    Represents INP `width` elements.
    """

    _KEYWORD = 'width'

    _ATTRS = {
        'width': types.Real,
    }

    _REGEX = re.compile(rf'\Awidth( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, width: str | int | float | types.Real):
        """
        Initializes `Width`.

        Parameters:
            width: Width for sampling spontaneous fission.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.width: types.Real = width

    @property
    def width(self) -> types.Real:
        """
        Width for sampling spontaneous fission

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._width

    @width.setter
    def width(self, width: str | int | float | types.Real) -> None:
        """
        Sets `width`.

        Parameters:
            width: Width for sampling spontaneous fission.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if width is not None:
            if isinstance(width, types.Real):
                width = width
            elif isinstance(width, int) or isinstance(width, float):
                width = types.Real(width)
            elif isinstance(width, str):
                width = types.Real.from_mcnp(width)

        if width is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, width)

        self._width: types.Real = width
