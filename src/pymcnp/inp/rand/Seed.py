import re

from . import _option
from ... import types
from ... import errors


class Seed(_option.RandOption):
    """
    Represents INP `seed` elements.
    """

    _KEYWORD = 'seed'

    _ATTRS = {
        'seed': types.Integer,
    }

    _REGEX = re.compile(rf'\Aseed( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, seed: str | int | types.Integer):
        """
        Initializes `Seed`.

        Parameters:
            seed: Random number generator seed.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.seed: types.Integer = seed

    @property
    def seed(self) -> types.Integer:
        """
        Random number generator seed

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._seed

    @seed.setter
    def seed(self, seed: str | int | types.Integer) -> None:
        """
        Sets `seed`.

        Parameters:
            seed: Random number generator seed.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if seed is not None:
            if isinstance(seed, types.Integer):
                seed = seed
            elif isinstance(seed, int):
                seed = types.Integer(seed)
            elif isinstance(seed, str):
                seed = types.Integer.from_mcnp(seed)

        if seed is None or not (seed % 2 == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, seed)

        self._seed: types.Integer = seed
