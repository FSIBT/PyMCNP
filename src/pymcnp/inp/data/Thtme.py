import re

from . import _option
from ... import types
from ... import errors


class Thtme(_option.DataOption):
    """
    Represents INP thtme elements.
    """

    _KEYWORD = 'thtme'

    _ATTRS = {
        'times': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Athtme((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, times: list[str] | list[float] | list[types.Real]):
        """
        Initializes ``Thtme``.

        Parameters:
            times: Tuple of times when thermal temperatures are specified.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.times: types.Tuple[types.Real] = times

    @property
    def times(self) -> types.Tuple[types.Real]:
        """
        Tuple of times when thermal temperatures are specified

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._times

    @times.setter
    def times(self, times: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets ``times``.

        Parameters:
            times: Tuple of times when thermal temperatures are specified.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if times is not None:
            array = []
            for item in times:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            times = types.Tuple(array)

        if times is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, times)

        self._times: types.Tuple[types.Real] = times
