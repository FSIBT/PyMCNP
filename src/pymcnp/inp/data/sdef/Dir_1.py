import re

from . import _option
from .... import types


class Dir_1(_option.SdefOption):
    """
    Represents INP dir variation #1 elements.
    """

    _KEYWORD = 'dir'

    _ATTRS = {
        'cosine': types.Distribution,
    }

    _REGEX = re.compile(rf'\Adir( {types.Distribution._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, cosine: str | types.Distribution = None):
        """
        Initializes ``Dir_1``.

        Parameters:
            cosine: Cosine of the angle between VEC and particle.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.cosine: types.Distribution = cosine

    @property
    def cosine(self) -> types.Distribution:
        """
        Cosine of the angle between VEC and particle

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._cosine

    @cosine.setter
    def cosine(self, cosine: str | types.Distribution) -> None:
        """
        Sets ``cosine``.

        Parameters:
            cosine: Cosine of the angle between VEC and particle.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cosine is not None:
            if isinstance(cosine, types.Distribution):
                cosine = cosine
            elif isinstance(cosine, str):
                cosine = types.Distribution.from_mcnp(cosine)

        self._cosine: types.Distribution = cosine
