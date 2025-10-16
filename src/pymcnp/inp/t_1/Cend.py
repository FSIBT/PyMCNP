import re

from . import _option
from ... import types
from ... import errors


class Cend(_option.TOption_1):
    """
    Represents INP `cend` elements.
    """

    _KEYWORD = 'cend'

    _ATTRS = {
        'time': types.Real,
    }

    _REGEX = re.compile(rf'\Acend( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, time: str | int | float | types.Real):
        """
        Initializes `Cend`.

        Parameters:
            time: Reference ending time.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.time: types.Real = time

    @property
    def time(self) -> types.Real:
        """
        Reference ending time

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._time

    @time.setter
    def time(self, time: str | int | float | types.Real) -> None:
        """
        Sets `time`.

        Parameters:
            time: Reference ending time.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if time is not None:
            if isinstance(time, types.Real):
                time = time
            elif isinstance(time, int) or isinstance(time, float):
                time = types.Real(time)
            elif isinstance(time, str):
                time = types.Real.from_mcnp(time)

        if time is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, time)

        self._time: types.Real = time
