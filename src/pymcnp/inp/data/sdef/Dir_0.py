import re
import typing
import dataclasses


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Dir_0(SdefOption_, keyword='dir'):
    """
    Represents INP dir variation #0 elements.

    Attributes:
        cosine: Cosine of the angle between VEC and particle.
    """

    _ATTRS = {
        'cosine': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Adir( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, cosine: types.RealOrJump):
        """
        Initializes ``Dir_0``.

        Parameters:
            cosine: Cosine of the angle between VEC and particle.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if cosine is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cosine)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cosine,
            ]
        )

        self.cosine: typing.Final[types.RealOrJump] = cosine


@dataclasses.dataclass
class DirBuilder_0:
    """
    Builds ``Dir_0``.

    Attributes:
        cosine: Cosine of the angle between VEC and particle.
    """

    cosine: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``DirBuilder_0`` into ``Dir_0``.

        Returns:
            ``Dir_0`` for ``DirBuilder_0``.
        """

        if isinstance(self.cosine, types.Real):
            cosine = self.cosine
        elif isinstance(self.cosine, float) or isinstance(self.cosine, int):
            cosine = types.RealOrJump(self.cosine)
        elif isinstance(self.cosine, str):
            cosine = types.RealOrJump.from_mcnp(self.cosine)

        return Dir_0(
            cosine=cosine,
        )
