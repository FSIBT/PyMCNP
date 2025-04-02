import re
import typing


from .option_ import ActOption_
from ....utils import types
from ....utils import errors


class Nonfiss(ActOption_, keyword='nonfiss'):
    """
    Represents INP nonfiss elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'kind': types.String,
    }

    _REGEX = re.compile(rf'\Anonfiss( {types.String._REGEX.pattern})\Z')

    def __init__(self, kind: types.String):
        """
        Initializes ``Nonfiss``.

        Parameters:
            kind: Type of delayed particle(s) to be produced by simple multi-particle reaction.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if kind is None or type not in {'none', 'n,p,e,f,a', 'all'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, kind)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                kind,
            ]
        )

        self.kind: typing.Final[types.String] = kind
