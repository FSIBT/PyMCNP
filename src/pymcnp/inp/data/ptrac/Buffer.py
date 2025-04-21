import re
import typing
import dataclasses


from ._option import PtracOption
from ....utils import types
from ....utils import errors


class Buffer(PtracOption, keyword='buffer'):
    """
    Represents INP buffer elements.

    Attributes:
        storage: Amount of storage available for filtered events.
    """

    _ATTRS = {
        'storage': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Abuffer( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, storage: types.IntegerOrJump):
        """
        Initializes ``Buffer``.

        Parameters:
            storage: Amount of storage available for filtered events.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if storage is None or not (storage > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, storage)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                storage,
            ]
        )

        self.storage: typing.Final[types.IntegerOrJump] = storage


@dataclasses.dataclass
class BufferBuilder:
    """
    Builds ``Buffer``.

    Attributes:
        storage: Amount of storage available for filtered events.
    """

    storage: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``BufferBuilder`` into ``Buffer``.

        Returns:
            ``Buffer`` for ``BufferBuilder``.
        """

        if isinstance(self.storage, types.Integer):
            storage = self.storage
        elif isinstance(self.storage, int):
            storage = types.IntegerOrJump(self.storage)
        elif isinstance(self.storage, str):
            storage = types.IntegerOrJump.from_mcnp(self.storage)

        return Buffer(
            storage=storage,
        )
