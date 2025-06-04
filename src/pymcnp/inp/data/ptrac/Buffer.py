import re
import copy
import typing
import dataclasses


from ._option import PtracOption
from ....utils import types
from ....utils import errors


class Buffer(PtracOption):
    """
    Represents INP buffer elements.

    Attributes:
        storage: Amount of storage available for filtered events.
    """

    _KEYWORD = 'buffer'

    _ATTRS = {
        'storage': types.Integer,
    }

    _REGEX = re.compile(rf'\Abuffer( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, storage: types.Integer):
        """
        Initializes ``Buffer``.

        Parameters:
            storage: Amount of storage available for filtered events.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if storage is None or not (storage.value > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, storage)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                storage,
            ]
        )

        self.storage: typing.Final[types.Integer] = storage


@dataclasses.dataclass
class BufferBuilder:
    """
    Builds ``Buffer``.

    Attributes:
        storage: Amount of storage available for filtered events.
    """

    storage: str | int | types.Integer

    def build(self):
        """
        Builds ``BufferBuilder`` into ``Buffer``.

        Returns:
            ``Buffer`` for ``BufferBuilder``.
        """

        storage = self.storage
        if isinstance(self.storage, types.Integer):
            storage = self.storage
        elif isinstance(self.storage, int):
            storage = types.Integer(self.storage)
        elif isinstance(self.storage, str):
            storage = types.Integer.from_mcnp(self.storage)

        return Buffer(
            storage=storage,
        )

    @staticmethod
    def unbuild(ast: Buffer):
        """
        Unbuilds ``Buffer`` into ``BufferBuilder``

        Returns:
            ``BufferBuilder`` for ``Buffer``.
        """

        return Buffer(
            storage=copy.deepcopy(ast.storage),
        )
