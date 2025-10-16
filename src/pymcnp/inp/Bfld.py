import re

from . import bfld
from . import _card
from .. import types
from .. import errors


class Bfld(_card.Card):
    """
    Represents INP bfld cards.
    """

    _KEYWORD = 'bfld'

    _ATTRS = {
        'suffix': types.Integer,
        'kind': types.String,
        'options': types.Tuple(bfld.BfldOption),
    }

    _REGEX = re.compile(rf'\Abfld(\d+)( {types.String._REGEX.pattern[2:-2]})((?: (?:{bfld.BfldOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, kind: str | types.String, options: list[str] | list[bfld.BfldOption] = None):
        """
        Initializes `Bfld`.

        Parameters:
            suffix: Data card option suffix.
            kind: Magnetic field type.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.kind: types.String = kind
        self.options: types.Tuple(bfld.BfldOption) = options

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

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def kind(self) -> types.String:
        """
        Magnetic field type

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._kind

    @kind.setter
    def kind(self, kind: str | types.String) -> None:
        """
        Sets `kind`.

        Parameters:
            kind: Magnetic field type.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if kind is not None:
            if isinstance(kind, types.String):
                kind = kind
            elif isinstance(kind, str):
                kind = types.String.from_mcnp(kind)

        if kind is None or kind.value.lower() not in {'const', 'quad', 'quadff'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, kind)

        self._kind: types.String = kind

    @property
    def options(self) -> types.Tuple(bfld.BfldOption):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[bfld.BfldOption]) -> None:
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
                if isinstance(item, bfld.BfldOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(bfld.BfldOption.from_mcnp(item))
            options = types.Tuple(bfld.BfldOption)(array)

        self._options: types.Tuple(bfld.BfldOption) = options
