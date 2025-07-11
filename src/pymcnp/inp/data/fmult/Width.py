import re

from . import _option
from ....utils import types
from ....utils import errors


class Width(_option.FmultOption):
    """
    Represents INP width elements.

    Attributes:
        width: Width for sampling spontaneous fission.
    """

    _KEYWORD = 'width'

    _ATTRS = {
        'width': types.Real,
    }

    _REGEX = re.compile(rf'\Awidth( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, width: str | int | float | types.Real):
        """
        Initializes ``Width``.

        Parameters:
            width: Width for sampling spontaneous fission.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.width: types.Real = width

    @property
    def width(self) -> types.Real:
        """
        Gets ``width``.

        Returns:
            ``width``.
        """

        return self._width

    @width.setter
    def width(self, width: str | int | float | types.Real) -> None:
        """
        Sets ``width``.

        Parameters:
            width: Width for sampling spontaneous fission.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if width is not None:
            if isinstance(width, types.Real):
                width = width
            elif isinstance(width, int):
                width = types.Real(width)
            elif isinstance(width, float):
                width = types.Real(width)
            elif isinstance(width, str):
                width = types.Real.from_mcnp(width)
            else:
                raise TypeError

        if width is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, width)

        self._width: types.Real = width
