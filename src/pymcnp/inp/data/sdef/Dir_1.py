import re
import copy
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types


class Dir_1(SdefOption):
    """
    Represents INP dir variation #1 elements.

    Attributes:
        cosine: Cosine of the angle between VEC and particle.
    """

    _KEYWORD = 'dir'

    _ATTRS = {
        'cosine': types.DistributionNumber,
    }

    _REGEX = re.compile(rf'\Adir( {types.DistributionNumber._REGEX.pattern})?\Z')

    def __init__(self, cosine: types.DistributionNumber = None):
        """
        Initializes ``Dir_1``.

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

        self.cosine: typing.Final[types.DistributionNumber] = cosine


@dataclasses.dataclass
class DirBuilder_1:
    """
    Builds ``Dir_1``.

    Attributes:
        cosine: Cosine of the angle between VEC and particle.
    """

    cosine: str | types.DistributionNumber = None

    def build(self):
        """
        Builds ``DirBuilder_1`` into ``Dir_1``.

        Returns:
            ``Dir_1`` for ``DirBuilder_1``.
        """

        cosine = self.cosine
        if isinstance(self.cosine, types.DistributionNumber):
            cosine = self.cosine
        elif isinstance(self.cosine, str):
            cosine = types.DistributionNumber.from_mcnp(self.cosine)

        return Dir_1(
            cosine=cosine,
        )

    @staticmethod
    def unbuild(ast: Dir_1):
        """
        Unbuilds ``Dir_1`` into ``DirBuilder_1``

        Returns:
            ``DirBuilder_1`` for ``Dir_1``.
        """

        return Dir_1(
            cosine=copy.deepcopy(ast.cosine),
        )
