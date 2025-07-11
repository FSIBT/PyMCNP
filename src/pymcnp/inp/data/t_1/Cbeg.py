import re

from . import _option
from ....utils import types
from ....utils import errors


class Cbeg(_option.TOption_1):
    """
    Represents INP cbeg elements.

    Attributes:
        time: Reference starting time.
    """

    _KEYWORD = 'cbeg'

    _ATTRS = {
        'time': types.Real,
    }

    _REGEX = re.compile(rf'\Acbeg( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, time: str | int | float | types.Real):
        """
        Initializes ``Cbeg``.

        Parameters:
            time: Reference starting time.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.time: types.Real = time

    @property
    def time(self) -> types.Real:
        """
        Gets ``time``.

        Returns:
            ``time``.
        """

        return self._time

    @time.setter
    def time(self, time: str | int | float | types.Real) -> None:
        """
        Sets ``time``.

        Parameters:
            time: Reference starting time.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if time is not None:
            if isinstance(time, types.Real):
                time = time
            elif isinstance(time, int):
                time = types.Real(time)
            elif isinstance(time, float):
                time = types.Real(time)
            elif isinstance(time, str):
                time = types.Real.from_mcnp(time)
            else:
                raise TypeError

        if time is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, time)

        self._time: types.Real = time
