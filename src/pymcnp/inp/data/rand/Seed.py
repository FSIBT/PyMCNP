import re
import typing


from .option_ import RandOption_
from ....utils import types
from ....utils import errors


class Seed(RandOption_, keyword='seed'):
    """
    Represents INP seed elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'seed': types.Integer,
    }

    _REGEX = re.compile(rf'\Aseed( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, seed: types.Integer):
        """
        Initializes ``Seed``.

        Parameters:
            seed: Random number generator seed.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if seed is None or not (seed.value % 2 == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, seed)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                seed,
            ]
        )

        self.seed: typing.Final[types.Integer] = seed
