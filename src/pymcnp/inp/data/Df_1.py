import re

from . import df_1
from . import _option
from ... import types
from ... import errors


class Df_1(_option.DataOption):
    """
    Represents INP df variation #1 elements.
    """

    _KEYWORD = 'df'

    _ATTRS = {
        'suffix': types.Integer,
        'options': types.Tuple(df_1.DfOption_1),
    }

    _REGEX = re.compile(rf'\Adf(\d+)((?: (?:{df_1.DfOption_1._REGEX.pattern[2:-2]}))+?)\Z')

    def __init__(self, suffix: str | int | types.Integer, options: list[str] | list[df_1.DfOption_1]):
        """
        Initializes ``Df_1``.

        Parameters:
            suffix: Data card option suffix.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.options: types.Tuple(df_1.DfOption_1) = options

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

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def options(self) -> types.Tuple(df_1.DfOption_1):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[df_1.DfOption_1]) -> None:
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
                if isinstance(item, df_1.DfOption_1):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(df_1.DfOption_1.from_mcnp(item))
            options = types.Tuple(df_1.DfOption_1)(array)

        if options is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, options)

        self._options: types.Tuple(df_1.DfOption_1) = options
