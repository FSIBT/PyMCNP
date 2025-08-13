import re

from . import tme_1
from . import _option
from ... import errors


class Tme_1(_option.SdefOption):
    """
    Represents INP `tme` elements variation #1.
    """

    _KEYWORD = 'tme'

    _ATTRS = {
        'time': tme_1.Embedded,
    }

    _REGEX = re.compile(rf'\Atme( {tme_1.Embedded._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, time: str | tme_1.Embedded):
        """
        Initializes `Tme_1`.

        Parameters:
            time: Time in shakes.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.time: tme_1.Embedded = time

    @property
    def time(self) -> tme_1.Embedded:
        """
        Time in shakes

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._time

    @time.setter
    def time(self, time: str | tme_1.Embedded) -> None:
        """
        Sets `time`.

        Parameters:
            time: Time in shakes.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if time is not None:
            if isinstance(time, tme_1.Embedded):
                time = time
            elif isinstance(time, str):
                time = tme_1.Embedded.from_mcnp(time)

        if time is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, time)

        self._time: tme_1.Embedded = time
