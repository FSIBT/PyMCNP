import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Par(SdefOption_, keyword='par'):
    """
    Represents INP par elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'kind': types.String,
    }

    _REGEX = re.compile(rf'par( {types.String._REGEX.pattern})')

    def __init__(self, kind: types.String):
        """
        Initializes ``Par``.

        Parameters:
            kind: Source particle type.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if kind is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, kind)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                kind,
            ]
        )

        self.kind: typing.Final[types.String] = kind
