import re

from . import ksen
from . import _card
from .. import types
from .. import errors


class Ksen(_card.Card):
    """
    Represents INP `ksen` cards.
    """

    _KEYWORD = 'ksen'

    _ATTRS = {
        'suffix': types.Integer,
        'sen': types.String,
        'options': types.Tuple(ksen.KsenOption),
    }

    _REGEX = re.compile(rf'\Aksen(\d+)( {types.String._REGEX.pattern[2:-2]})((?: (?:{ksen.KsenOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, sen: str | types.String, options: list[str] | list[ksen.KsenOption] = None):
        """
        Initializes `Ksen`.

        Parameters:
            suffix: Data card option suffix.
            sen: Type of sensitivity.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.sen: types.String = sen
        self.options: types.Tuple(ksen.KsenOption) = options

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets `suffix`.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        if suffix is None or not (suffix > 0 and suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def sen(self) -> types.String:
        """
        Type of sensitivity

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._sen

    @sen.setter
    def sen(self, sen: str | types.String) -> None:
        """
        Sets `sen`.

        Parameters:
            sen: Type of sensitivity.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if sen is not None:
            if isinstance(sen, types.String):
                sen = sen
            elif isinstance(sen, str):
                sen = types.String.from_mcnp(sen)

        if sen is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, sen)

        self._sen: types.String = sen

    @property
    def options(self) -> types.Tuple(ksen.KsenOption):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[ksen.KsenOption]) -> None:
        """
        Sets `options`.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if options is not None:
            array = []
            for item in options:
                if isinstance(item, ksen.KsenOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(ksen.KsenOption.from_mcnp(item))
            options = types.Tuple(ksen.KsenOption)(array)

        self._options: types.Tuple(ksen.KsenOption) = options
