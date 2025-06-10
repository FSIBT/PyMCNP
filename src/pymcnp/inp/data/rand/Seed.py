import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Seed(_option.RandOption):
    """
    Represents INP seed elements.

    Attributes:
        seed: Random number generator seed.
    """

    _KEYWORD = 'seed'

    _ATTRS = {
        'seed': types.Integer,
    }

    _REGEX = re.compile(rf'\Aseed( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, seed: types.Integer):
        """
        Initializes ``Seed``.

        Parameters:
            seed: Random number generator seed.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if seed is None or not (seed.value % 2 == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, seed)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                seed,
            ]
        )

        self.seed: typing.Final[types.Integer] = seed


@dataclasses.dataclass
class SeedBuilder(_option.RandOptionBuilder):
    """
    Builds ``Seed``.

    Attributes:
        seed: Random number generator seed.
    """

    seed: str | int | types.Integer

    def build(self):
        """
        Builds ``SeedBuilder`` into ``Seed``.

        Returns:
            ``Seed`` for ``SeedBuilder``.
        """

        seed = self.seed
        if isinstance(self.seed, types.Integer):
            seed = self.seed
        elif isinstance(self.seed, int):
            seed = types.Integer(self.seed)
        elif isinstance(self.seed, str):
            seed = types.Integer.from_mcnp(self.seed)

        return Seed(
            seed=seed,
        )

    @staticmethod
    def unbuild(ast: Seed):
        """
        Unbuilds ``Seed`` into ``SeedBuilder``

        Returns:
            ``SeedBuilder`` for ``Seed``.
        """

        return SeedBuilder(
            seed=copy.deepcopy(ast.seed),
        )
