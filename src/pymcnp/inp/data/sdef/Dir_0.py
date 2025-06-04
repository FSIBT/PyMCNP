import re
import copy
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

    _KEYWORD = 'dir'

    _ATTRS = {
        'cosine': types.Real,
    }

    _REGEX = re.compile(rf'\Adir( {types.Real._REGEX.pattern[2:-2]})?\Z')

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

    @staticmethod
    def unbuild(ast: Dir_0):
        """
        Unbuilds ``Dir_0`` into ``DirBuilder_0``

        Returns:
            ``DirBuilder_0`` for ``Dir_0``.
        """

        return Dir_0(
            cosine=copy.deepcopy(ast.cosine),
        )
