import re

from . import _option
from ....utils import types
from ....utils import errors


class Maxstep(_option.BfldOption):
    """
    Represents INP maxstep elements.

    Attributes:
        size: Maximum step size.
    """

    _KEYWORD = 'maxstep'

    _ATTRS = {
        'size': types.Real,
    }

    _REGEX = re.compile(rf'\Amaxstep( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, size: str | int | float | types.Real):
        """
        Initializes ``Maxstep``.

        Parameters:
            size: Maximum step size.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.size: types.Real = size

    @property
    def size(self) -> types.Real:
        """
        Gets ``size``.

        Returns:
            ``size``.
        """

        return self._size

    @size.setter
    def size(self, size: str | int | float | types.Real) -> None:
        """
        Sets ``size``.

        Parameters:
            size: Maximum step size.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if size is not None:
            if isinstance(size, types.Real):
                size = size
            elif isinstance(size, int):
                size = types.Real(size)
            elif isinstance(size, float):
                size = types.Real(size)
            elif isinstance(size, str):
                size = types.Real.from_mcnp(size)
            else:
                raise TypeError

        if size is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, size)

        self._size: types.Real = size
