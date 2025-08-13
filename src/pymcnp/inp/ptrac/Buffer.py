import re

from . import _option
from ... import types
from ... import errors


class Buffer(_option.PtracOption):
    """
    Represents INP `buffer` elements.
    """

    _KEYWORD = 'buffer'

    _ATTRS = {
        'storage': types.Integer,
    }

    _REGEX = re.compile(rf'\Abuffer( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, storage: str | int | types.Integer):
        """
        Initializes `Buffer`.

        Parameters:
            storage: Amount of storage available for filtered events.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.storage: types.Integer = storage

    @property
    def storage(self) -> types.Integer:
        """
        Amount of storage available for filtered events

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._storage

    @storage.setter
    def storage(self, storage: str | int | types.Integer) -> None:
        """
        Sets `storage`.

        Parameters:
            storage: Amount of storage available for filtered events.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if storage is not None:
            if isinstance(storage, types.Integer):
                storage = storage
            elif isinstance(storage, int):
                storage = types.Integer(storage)
            elif isinstance(storage, str):
                storage = types.Integer.from_mcnp(storage)

        if storage is None or not (storage > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, storage)

        self._storage: types.Integer = storage
