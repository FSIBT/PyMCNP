import re
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types


class Dir_0(SdefOption):
    """
    Represents INP dir variation #0 elements.

    Attributes:
        cosine: Cosine of the angle between VEC and particle.
    """

    _ATTRS = {
        'cosine': types.Real,
    }

    _REGEX = re.compile(rf'\Adir( {types.Real._REGEX.pattern})?\Z')

    def __init__(self, cosine: types.Real = None):
        """
        Initializes ``Dir_0``.

        Parameters:
            cosine: Cosine of the angle between VEC and particle.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cosine,
            ]
        )

        self.cosine: typing.Final[types.Real] = cosine


@dataclasses.dataclass
class DirBuilder_0:
    """
    Builds ``Dir_0``.

    Attributes:
        cosine: Cosine of the angle between VEC and particle.
    """

    cosine: str | float | types.Real = None

    def build(self):
        """
        Builds ``DirBuilder_0`` into ``Dir_0``.

        Returns:
            ``Dir_0`` for ``DirBuilder_0``.
        """

        cosine = self.cosine
        if isinstance(self.cosine, types.Real):
            cosine = self.cosine
        elif isinstance(self.cosine, float) or isinstance(self.cosine, int):
            cosine = types.Real(self.cosine)
        elif isinstance(self.cosine, str):
            cosine = types.Real.from_mcnp(self.cosine)

        return Dir_0(
            cosine=cosine,
        )
