import re

from . import _option
from ....utils import types
from ....utils import errors


class Tme_1(_option.SdefOption):
    """
    Represents INP tme variation #1 elements.
    """

    _KEYWORD = 'tme'

    _ATTRS = {
        'time': types.EmbeddedDistributionNumber,
    }

    _REGEX = re.compile(rf'\Atme( {types.EmbeddedDistributionNumber._REGEX.pattern[2:-2]})\Z')

    def __init__(self, time: str | types.EmbeddedDistributionNumber):
        """
        Initializes ``Tme_1``.

        Parameters:
            time: Time in shakes.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.time: types.EmbeddedDistributionNumber = time

    @property
    def time(self) -> types.EmbeddedDistributionNumber:
        """
        Time in shakes

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._time

    @time.setter
    def time(self, time: str | types.EmbeddedDistributionNumber) -> None:
        """
        Sets ``time``.

        Parameters:
            time: Time in shakes.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if time is not None:
            if isinstance(time, types.EmbeddedDistributionNumber):
                time = time
            elif isinstance(time, str):
                time = types.EmbeddedDistributionNumber.from_mcnp(time)

        if time is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, time)

        self._time: types.EmbeddedDistributionNumber = time
