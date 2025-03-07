import re
import typing


from .option_ import EmbeeOption_
from ....utils import types
from ....utils import errors


class Mtype(EmbeeOption_, keyword='mtype'):
    """
    Represents INP mtype elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'kind': types.String,
    }

    _REGEX = re.compile(rf'mtype( {types.String._REGEX.pattern})')

    def __init__(self, kind: types.String):
        """
        Initializes ``Mtype``.

        Parameters:
            kind: Multiplier type.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if kind is None or type not in {
            'flux',
            'isotropic',
            'population',
            'reaction',
            'source',
            'track',
        }:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, kind)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                kind,
            ]
        )

        self.kind: typing.Final[types.String] = kind
