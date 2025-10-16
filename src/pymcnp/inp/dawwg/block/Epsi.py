import re

from . import _option
from .... import types
from .... import errors


class Epsi(_option.BlockOption):
    """
    Represents INP `epsi` elements.
    """

    _KEYWORD = 'epsi'

    _ATTRS = {
        'setting': types.Real,
    }

    _REGEX = re.compile(rf'\Aepsi( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, setting: str | int | float | types.Real):
        """
        Initializes `Epsi`.

        Parameters:
            setting: Convergence precision.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.setting: types.Real = setting

    @property
    def setting(self) -> types.Real:
        """
        Convergence precision

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._setting

    @setting.setter
    def setting(self, setting: str | int | float | types.Real) -> None:
        """
        Sets `setting`.

        Parameters:
            setting: Convergence precision.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if setting is not None:
            if isinstance(setting, types.Real):
                setting = setting
            elif isinstance(setting, int) or isinstance(setting, float):
                setting = types.Real(setting)
            elif isinstance(setting, str):
                setting = types.Real.from_mcnp(setting)

        if setting is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.Real = setting
