import re

from . import _option
from ... import types
from ... import errors


class Refi(_option.MOption_0):
    """
    Represents INP `refi` elements.
    """

    _KEYWORD = 'refi'

    _ATTRS = {
        'refractive_index': types.Real,
    }

    _REGEX = re.compile(rf'\Arefi( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, refractive_index: str | int | float | types.Real):
        """
        Initializes `Refi`.

        Parameters:
            refractive_index: Refractive index constant.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.refractive_index: types.Real = refractive_index

    @property
    def refractive_index(self) -> types.Real:
        """
        Refractive index constant

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._refractive_index

    @refractive_index.setter
    def refractive_index(self, refractive_index: str | int | float | types.Real) -> None:
        """
        Sets `refractive_index`.

        Parameters:
            refractive_index: Refractive index constant.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if refractive_index is not None:
            if isinstance(refractive_index, types.Real):
                refractive_index = refractive_index
            elif isinstance(refractive_index, int) or isinstance(refractive_index, float):
                refractive_index = types.Real(refractive_index)
            elif isinstance(refractive_index, str):
                refractive_index = types.Real.from_mcnp(refractive_index)

        if refractive_index is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, refractive_index)

        self._refractive_index: types.Real = refractive_index
