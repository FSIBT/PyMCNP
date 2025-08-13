import re

from . import _entry
from ... import types
from ... import errors


class Diagnostic(_entry.DdEntry):
    """
    Represents INP `diagnostic` elements.
    """

    _KEYWORD = ''

    _ATTRS = {
        'playing_setting': types.Real,
        'printing_setting': types.Real,
    }

    _REGEX = re.compile(rf'\A({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, playing_setting: str | int | float | types.Real, printing_setting: str | int | float | types.Real):
        """
        Initializes `Diagnostic`.

        Parameters:
            playing_setting: Criterion for playing Russian roulette for DXTRAN.
            printing_setting: Criterion for printing diagnostics for large contributions for DXTRAN.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.playing_setting: types.Real = playing_setting
        self.printing_setting: types.Real = printing_setting

    @property
    def playing_setting(self) -> types.Real:
        """
        Criterion for playing Russian roulette for DXTRAN

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._playing_setting

    @playing_setting.setter
    def playing_setting(self, playing_setting: str | int | float | types.Real) -> None:
        """
        Sets `playing_setting`.

        Parameters:
            playing_setting: Criterion for playing Russian roulette for DXTRAN.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if playing_setting is not None:
            if isinstance(playing_setting, types.Real):
                playing_setting = playing_setting
            elif isinstance(playing_setting, int) or isinstance(playing_setting, float):
                playing_setting = types.Real(playing_setting)
            elif isinstance(playing_setting, str):
                playing_setting = types.Real.from_mcnp(playing_setting)

        if playing_setting is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, playing_setting)

        self._playing_setting: types.Real = playing_setting

    @property
    def printing_setting(self) -> types.Real:
        """
        Criterion for printing diagnostics for large contributions for DXTRAN

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._printing_setting

    @printing_setting.setter
    def printing_setting(self, printing_setting: str | int | float | types.Real) -> None:
        """
        Sets `printing_setting`.

        Parameters:
            printing_setting: Criterion for printing diagnostics for large contributions for DXTRAN.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if printing_setting is not None:
            if isinstance(printing_setting, types.Real):
                printing_setting = printing_setting
            elif isinstance(printing_setting, int) or isinstance(printing_setting, float):
                printing_setting = types.Real(printing_setting)
            elif isinstance(printing_setting, str):
                printing_setting = types.Real.from_mcnp(printing_setting)

        if printing_setting is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, printing_setting)

        self._printing_setting: types.Real = printing_setting
