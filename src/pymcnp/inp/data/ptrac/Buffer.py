import re
import typing


from .option_ import PtracOption_
from ....utils import types
from ....utils import errors


class Buffer(PtracOption_, keyword='buffer'):
    """
    Represents INP buffer elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if storage is None or not (storage > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, storage)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                storage,
            ]
        )

        self.storage: typing.Final[types.IntegerOrJump] = storage
