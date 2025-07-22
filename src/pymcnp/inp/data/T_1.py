import re

from . import t_1
from . import _option
from ... import types
from ... import errors


class T_1(_option.DataOption):
    """
    Represents INP t variation #1 elements.
    """

    _KEYWORD = 't'

    _ATTRS = {
        'suffix': types.Integer,
        'options': types.Tuple(t_1.TOption_1),
    }

    _REGEX = re.compile(rf'\At(\d+)((?: (?:{t_1.TOption_1._REGEX.pattern[2:-2]}))+?)\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, options: list[str] | list[t_1.TOption_1]):
        """
        Initializes ``T_1``.

        Parameters:
            suffix: Data card option suffix.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.options: types.Tuple(t_1.TOption_1) = options

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets ``suffix``.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def options(self) -> types.Tuple(t_1.TOption_1):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[t_1.TOption_1]) -> None:
        """
        Sets ``options``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if options is not None:
            array = []
            for item in options:
                if isinstance(item, t_1.TOption_1):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(t_1.TOption_1.from_mcnp(item))
            options = types.Tuple(t_1.TOption_1)(array)

        if options is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, options)

        self._options: types.Tuple(t_1.TOption_1) = options
