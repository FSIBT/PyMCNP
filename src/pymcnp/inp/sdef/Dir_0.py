import re

from . import _option
from ... import types


class Dir_0(_option.SdefOption):
    """
    Represents INP `dir` elements variation #0.
    """

    _KEYWORD = 'dir'

    _ATTRS = {
        'cosine': types.Real,
    }

    _REGEX = re.compile(rf'\Adir( {types.Real._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)

    def __init__(self, cosine: str | int | float | types.Real = None):
        """
        Initializes `Dir_0`.

        Parameters:
            cosine: Cosine of the angle between VEC and particle.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.cosine: types.Real = cosine

    @property
    def cosine(self) -> types.Real:
        """
        Cosine of the angle between VEC and particle

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._cosine

    @cosine.setter
    def cosine(self, cosine: str | int | float | types.Real) -> None:
        """
        Sets `cosine`.

        Parameters:
            cosine: Cosine of the angle between VEC and particle.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cosine is not None:
            if isinstance(cosine, types.Real):
                cosine = cosine
            elif isinstance(cosine, int) or isinstance(cosine, float):
                cosine = types.Real(cosine)
            elif isinstance(cosine, str):
                cosine = types.Real.from_mcnp(cosine)

        self._cosine: types.Real = cosine
