import re

from . import _option
from ... import types
from ... import errors


class Ext_1(_option.SdefOption):
    """
    Represents INP `ext` elements variation #1.
    """

    _KEYWORD = 'ext'

    _ATTRS = {
        'distance_cosine': types.Distribution,
    }

    _REGEX = re.compile(rf'\Aext( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, distance_cosine: str | types.Distribution):
        """
        Initializes `Ext_1`.

        Parameters:
            distance_cosine: Distance for POS along AXS or Cosine of angle from AXS.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.distance_cosine: types.Distribution = distance_cosine

    @property
    def distance_cosine(self) -> types.Distribution:
        """
        Distance for POS along AXS or Cosine of angle from AXS

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._distance_cosine

    @distance_cosine.setter
    def distance_cosine(self, distance_cosine: str | types.Distribution) -> None:
        """
        Sets `distance_cosine`.

        Parameters:
            distance_cosine: Distance for POS along AXS or Cosine of angle from AXS.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if distance_cosine is not None:
            if isinstance(distance_cosine, types.Distribution):
                distance_cosine = distance_cosine
            elif isinstance(distance_cosine, str):
                distance_cosine = types.Distribution.from_mcnp(distance_cosine)

        if distance_cosine is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, distance_cosine)

        self._distance_cosine: types.Distribution = distance_cosine
