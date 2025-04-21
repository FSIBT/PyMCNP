import re
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Dxc(CellOption, keyword='dxc'):
    """
    Represents INP dxc elements.

    Attributes:
        suffix: Cell option suffix.
        designator: Cell particle designator.
        probability: Cell probability of DXTRAN contribution.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'probability': types.Real,
    }

    _REGEX = re.compile(rf'\Adxc(\d+):(\S+)( {types.Real._REGEX.pattern})\Z')

    def __init__(
        self, suffix: types.Integer, designator: types.Designator, probability: types.Real
    ):
        """
        Initializes ``Dxc``.

        Parameters:
            suffix: Cell option suffix.
            designator: Cell particle designator.
            probability: Cell probability of DXTRAN contribution.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if probability is None or not (0 <= probability <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, probability)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                probability,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.probability: typing.Final[types.Real] = probability


@dataclasses.dataclass
class DxcBuilder:
    """
    Builds ``Dxc``.

    Attributes:
        suffix: Cell option suffix.
        designator: Cell particle designator.
        probability: Cell probability of DXTRAN contribution.
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

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

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
