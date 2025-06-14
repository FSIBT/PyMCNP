import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Pd(_option.CellOption):
    """
    Represents INP pd elements.

    Attributes:
        suffix: Cell option suffix.
        probability: Cell probability of DXTRAN contribution.
    """

    _KEYWORD = 'pd'

    _ATTRS = {
        'suffix': types.Integer,
        'probability': types.Real,
    }

    _REGEX = re.compile(rf'\Apd(\d+)( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, suffix: types.Integer, probability: types.Real):
        """
        Initializes ``Pd``.

        Parameters:
            suffix: Cell option suffix.
            probability: Cell probability of DXTRAN contribution.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if probability is None or not (0 <= probability.value <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, probability)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                probability,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.probability: typing.Final[types.Real] = probability


@dataclasses.dataclass
class PdBuilder(_option.CellOptionBuilder):
    """
    Builds ``Pd``.

    Attributes:
        suffix: Cell option suffix.
        probability: Cell probability of DXTRAN contribution.
    """

    suffix: str | int | types.Integer
    probability: str | float | types.Real

    def build(self):
        """
        Builds ``PdBuilder`` into ``Pd``.

        Returns:
            ``Pd`` for ``PdBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        probability = self.probability
        if isinstance(self.probability, types.Real):
            probability = self.probability
        elif isinstance(self.probability, float) or isinstance(self.probability, int):
            probability = types.Real(self.probability)
        elif isinstance(self.probability, str):
            probability = types.Real.from_mcnp(self.probability)

        return Pd(
            suffix=suffix,
            probability=probability,
        )

    @staticmethod
    def unbuild(ast: Pd):
        """
        Unbuilds ``Pd`` into ``PdBuilder``

        Returns:
            ``PdBuilder`` for ``Pd``.
        """

        return PdBuilder(
            suffix=copy.deepcopy(ast.suffix),
            probability=copy.deepcopy(ast.probability),
        )
