import re

from . import kpert
from . import _option
from ... import types
from ... import errors


class Kpert(_option.DataOption):
    """
    Represents INP kpert elements.
    """

    _KEYWORD = 'kpert'

    _ATTRS = {
        'suffix': types.Integer,
        'options': types.Tuple(kpert.KpertOption),
    }

    _REGEX = re.compile(rf'\Akpert(\d+)((?: (?:{kpert.KpertOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, suffix: str | int | types.Integer, options: list[str] | list[kpert.KpertOption] = None):
        """
        Initializes ``Kpert``.

        Parameters:
            suffix: Data card option suffix.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.options: types.Tuple(kpert.KpertOption) = options

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

        if suffix is None or not (suffix > 0 and suffix <= 10_000):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def options(self) -> types.Tuple(kpert.KpertOption):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[kpert.KpertOption]) -> None:
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
                if isinstance(item, kpert.KpertOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(kpert.KpertOption.from_mcnp(item))
            options = types.Tuple(kpert.KpertOption)(array)

        self._options: types.Tuple(kpert.KpertOption) = options
