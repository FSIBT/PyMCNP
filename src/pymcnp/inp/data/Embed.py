import re

from . import embed
from . import _option
from ...utils import types
from ...utils import errors


class Embed(_option.DataOption):
    """
    Represents INP embed elements.
    """

    _KEYWORD = 'embed'

    _ATTRS = {
        'suffix': types.Integer,
        'options': types.Tuple[embed.EmbedOption],
    }

    _REGEX = re.compile(rf'\Aembed(\d+)?((?: (?:{embed.EmbedOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, suffix: str | int | types.Integer, options: list[str] | list[embed.EmbedOption] = None):
        """
        Initializes ``Embed``.

        Parameters:
            suffix: Data card option suffix.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.options: types.Tuple[embed.EmbedOption] = options

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
    def options(self) -> types.Tuple[embed.EmbedOption]:
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[embed.EmbedOption]) -> None:
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
                if isinstance(item, embed.EmbedOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(embed.EmbedOption.from_mcnp(item))
            options = types.Tuple(array)

        self._options: types.Tuple[embed.EmbedOption] = options
