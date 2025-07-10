import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Dxc(_option.LikeOption):
    """
    Represents INP dxc elements.

    Attributes:
        suffix: Like option suffix.
        designator: Like particle designator.
        probability: Like probability of DXTRAN contribution.
    """

    _KEYWORD = 'dxc'

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'probability': types.Real,
    }

    _REGEX = re.compile(rf'\Adxc(\d+):(\S+)( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, suffix: types.Integer, designator: types.Designator, probability: types.Real):
        """
        Initializes ``Dxc``.

        Parameters:
            suffix: Like option suffix.
            designator: Like particle designator.
            probability: Like probability of DXTRAN contribution.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if probability is None or not (probability >= 0 and probability <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, probability)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                probability,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.probability: typing.Final[types.Real] = probability


@dataclasses.dataclass
class DxcBuilder(_option.LikeOptionBuilder):
    """
    Builds ``Dxc``.

    Attributes:
        suffix: Like option suffix.
        designator: Like particle designator.
        probability: Like probability of DXTRAN contribution.
    """

    suffix: str | int | types.Integer
    designator: str | types.Designator
    probability: str | float | types.Real

    def build(self):
        """
        Builds ``DxcBuilder`` into ``Dxc``.

        Returns:
            ``Dxc`` for ``DxcBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        probability = self.probability
        if isinstance(self.probability, types.Real):
            probability = self.probability
        elif isinstance(self.probability, float) or isinstance(self.probability, int):
            probability = types.Real(self.probability)
        elif isinstance(self.probability, str):
            probability = types.Real.from_mcnp(self.probability)

        return Dxc(
            suffix=suffix,
            designator=designator,
            probability=probability,
        )

    @staticmethod
    def unbuild(ast: Dxc):
        """
        Unbuilds ``Dxc`` into ``DxcBuilder``

        Returns:
            ``DxcBuilder`` for ``Dxc``.
        """

        return DxcBuilder(
            suffix=copy.deepcopy(ast.suffix),
            designator=copy.deepcopy(ast.designator),
            probability=copy.deepcopy(ast.probability),
        )
