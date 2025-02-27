import re
import typing


from .option_ import MOption_
from ....utils import types
from ....utils import errors


class Pnlib(MOption_, keyword='pnlib'):
    """
    Represents INP pnlib elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(r'pnlib( \S+)')

    def __init__(self, abx: types.String):
        """
        Initializes ``Pnlib``.

        Parameters:
            abx: Default photonuclear table identifier.

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
