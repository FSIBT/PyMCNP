import re

from . import _option
from ....utils import types


class Dir_1(_option.SdefOption):
    """
    Represents INP dir variation #1 elements.

    Attributes:
        cosine: Cosine of the angle between VEC and particle.
    """

    _KEYWORD = 'dir'

    _ATTRS = {
        'cosine': types.DistributionNumber,
    }

    _REGEX = re.compile(rf'\Adir( {types.DistributionNumber._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, cosine: str | types.DistributionNumber = None):
        """
        Initializes ``Dir_1``.

        Parameters:
            cosine: Cosine of the angle between VEC and particle.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.cosine: types.DistributionNumber = cosine

    @property
    def cosine(self) -> types.DistributionNumber:
        """
        Gets ``cosine``.

        Returns:
            ``cosine``.
        """

        return self._cosine

    @cosine.setter
    def cosine(self, cosine: str | types.DistributionNumber) -> None:
        """
        Sets ``cosine``.

        Parameters:
            cosine: Cosine of the angle between VEC and particle.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cosine is not None:
            if isinstance(cosine, types.DistributionNumber):
                cosine = cosine
            elif isinstance(cosine, str):
                cosine = types.DistributionNumber.from_mcnp(cosine)
            else:
                raise TypeError

        self._cosine: types.DistributionNumber = cosine
