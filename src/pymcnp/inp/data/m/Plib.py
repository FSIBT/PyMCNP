import re
import typing


from .option_ import MOption_
from ....utils import types
from ....utils import errors


class Plib(MOption_, keyword='plib'):
    """
    Represents INP plib elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'plib( {types.String._REGEX.pattern})')

    def __init__(self, abx: types.String):
        """
        Initializes ``Plib``.

        Parameters:
            abx: Default photoatomic table identifier.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if abx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, abx)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                abx,
            ]
        )

        self.abx: typing.Final[types.String] = abx
