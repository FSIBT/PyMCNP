import re

from . import block
from . import _option
from ... import types
from ... import errors


class Block(_option.DawwgOption):
    """
    Represents INP `block` elements.
    """

    _KEYWORD = 'block'

    _ATTRS = {
        'setting': types.Integer,
        'options': types.Tuple(block.BlockOption),
    }

    _REGEX = re.compile(rf'\Ablock( {types.Integer._REGEX.pattern[2:-2]})((?: (?:{block.BlockOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    def __init__(self, setting: str | int | types.Integer, options: list[str] | list[block.BlockOption] = None):
        """
        Initializes `Block`.

        Parameters:
            setting: Destination of key-value pairs.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.setting: types.Integer = setting
        self.options: types.Tuple(block.BlockOption) = options

    @property
    def setting(self) -> types.Integer:
        """
        Destination of key-value pairs

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._setting

    @setting.setter
    def setting(self, setting: str | int | types.Integer) -> None:
        """
        Sets `setting`.

        Parameters:
            setting: Destination of key-value pairs.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if setting is not None:
            if isinstance(setting, types.Integer):
                setting = setting
            elif isinstance(setting, int):
                setting = types.Integer(setting)
            elif isinstance(setting, str):
                setting = types.Integer.from_mcnp(setting)

        if setting is None or setting not in {1, 3, 5, 6}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self._setting: types.Integer = setting

    @property
    def options(self) -> types.Tuple(block.BlockOption):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[block.BlockOption]) -> None:
        """
        Sets `options`.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if options is not None:
            array = []
            for item in options:
                if isinstance(item, block.BlockOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(block.BlockOption.from_mcnp(item))
            options = types.Tuple(block.BlockOption)(array)

        self._options: types.Tuple(block.BlockOption) = options
