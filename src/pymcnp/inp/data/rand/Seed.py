import re
import typing
import dataclasses


from .option_ import RandOption_
from ....utils import types
from ....utils import errors


class Seed(RandOption_, keyword='seed'):
    """
    Represents INP seed elements.

    Attributes:
        seed: Random number generator seed.
    """

    _ATTRS = {
        'seed': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aseed( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, seed: types.IntegerOrJump):
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

        self.seed: typing.Final[types.IntegerOrJump] = seed


@dataclasses.dataclass
class SeedBuilder:
    """
    Builds ``Seed``.

    Attributes:
        seed: Random number generator seed.
    """

    seed: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``SeedBuilder`` into ``Seed``.

        Returns:
            ``Seed`` for ``SeedBuilder``.
        """

        if isinstance(self.seed, types.Integer):
            seed = self.seed
        elif isinstance(self.seed, int):
            seed = types.IntegerOrJump(self.seed)
        elif isinstance(self.seed, str):
            seed = types.IntegerOrJump.from_mcnp(self.seed)

        return Seed(
            seed=seed,
        )
