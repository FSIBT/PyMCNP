import re

from . import _option
from ... import types
from ... import errors


class Ext_0(_option.SdefOption):
    """
    Represents INP `ext` elements variation #0.
    """

    _KEYWORD = 'ext'

    _ATTRS = {
        'distance_cosine': types.Real,
    }

    _REGEX = re.compile(rf'\Aext( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, distance_cosine: str | int | float | types.Real):
        """
        Initializes `Ext_0`.

        Parameters:
            distance_cosine: Distance for POS along AXS or Cosine of angle from AXS.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.distance_cosine: types.Real = distance_cosine

    @property
    def distance_cosine(self) -> types.Real:
        """
        Distance for POS along AXS or Cosine of angle from AXS

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._distance_cosine

    @distance_cosine.setter
    def distance_cosine(self, distance_cosine: str | int | float | types.Real) -> None:
        """
        Sets `distance_cosine`.

        Parameters:
            distance_cosine: Distance for POS along AXS or Cosine of angle from AXS.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if distance_cosine is not None:
            if isinstance(distance_cosine, types.Real):
                distance_cosine = distance_cosine
            elif isinstance(distance_cosine, int) or isinstance(distance_cosine, float):
                distance_cosine = types.Real(distance_cosine)
            elif isinstance(distance_cosine, str):
                distance_cosine = types.Real.from_mcnp(distance_cosine)

        if distance_cosine is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, distance_cosine)

        self._distance_cosine: types.Real = distance_cosine
