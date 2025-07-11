import re

from . import _option
from .....utils import types
from .....utils import errors


class Epsi(_option.BlockOption):
    """
    Represents INP epsi elements.

    Attributes:
        setting: Convergence precision.
    """

    _KEYWORD = 'epsi'

    _ATTRS = {
        'setting': types.Real,
    }

    _REGEX = re.compile(rf'\Aepsi( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: str | int | float | types.Real):
        """
        Initializes ``Epsi``.

        Parameters:
            setting: Convergence precision.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.setting: types.Real = setting

    @property
    def setting(self) -> types.Real:
        """
        Gets ``setting``.

        Returns:
            ``setting``.
        """

        return self._setting

    @setting.setter
    def setting(self, setting: str | int | float | types.Real) -> None:
        """
        Sets ``setting``.

        Parameters:
            setting: Convergence precision.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if setting is not None:
            if isinstance(setting, types.Real):
                setting = setting
            elif isinstance(setting, int):
                setting = types.Real(setting)
            elif isinstance(setting, float):
                setting = types.Real(setting)
            elif isinstance(setting, str):
                setting = types.Real.from_mcnp(setting)
            else:
                raise TypeError

        if setting is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.Real = setting
