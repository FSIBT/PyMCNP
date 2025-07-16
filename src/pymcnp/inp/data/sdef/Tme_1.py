import re

from . import _option
from .... import types
from .... import errors


class Tme_1(_option.SdefOption):
    """
    Represents INP tme variation #1 elements.
    """

    _KEYWORD = 'tme'

    _ATTRS = {
        'time': types.EmbeddedDistribution,
    }

    _REGEX = re.compile(rf'\Atme( {types.EmbeddedDistribution._REGEX.pattern[2:-2]})\Z')

    def __init__(self, time: str | types.EmbeddedDistribution):
        """
        Initializes ``Tme_1``.

        Parameters:
            time: Time in shakes.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.time: types.EmbeddedDistribution = time

    @property
    def time(self) -> types.EmbeddedDistribution:
        """
        Time in shakes

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._time

    @time.setter
    def time(self, time: str | types.EmbeddedDistribution) -> None:
        """
        Sets ``time``.

        Parameters:
            time: Time in shakes.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if time is not None:
            if isinstance(time, types.EmbeddedDistribution):
                time = time
            elif isinstance(time, str):
                time = types.EmbeddedDistribution.from_mcnp(time)

        if time is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, time)

        self._time: types.EmbeddedDistribution = time
