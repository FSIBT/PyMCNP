import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Dxc(DataOption):
    """
    Represents INP dxc elements.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        probabilities: Probability of contribution to DXTRAN.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'probabilities': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Adxc(\d+):(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(
        self,
        suffix: types.Integer,
        designator: types.Designator,
        probabilities: types.Tuple[types.RealOrJump],
    ):
        """
        Initializes ``Dxc``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            probabilities: Probability of contribution to DXTRAN.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if probabilities is None or not (
            filter(lambda entry: not (0 <= entry <= 1), probabilities)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, probabilities)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                probabilities,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.probabilities: typing.Final[types.Tuple[types.RealOrJump]] = probabilities


@dataclasses.dataclass
class DxcBuilder:
    """
    Builds ``Dxc``.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        probabilities: Probability of contribution to DXTRAN.
    """

    suffix: str | int | types.Integer
    designator: str | types.Designator
    probabilities: list[str] | list[float] | list[types.RealOrJump]

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

        probabilities = []
        for item in self.probabilities:
            if isinstance(item, types.RealOrJump):
                probabilities.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                probabilities.append(types.RealOrJump(item))
            elif isinstance(item, str):
                probabilities.append(types.RealOrJump.from_mcnp(item))
        probabilities = types.Tuple(probabilities)

        return Dxc(
            suffix=suffix,
            designator=designator,
            probabilities=probabilities,
        )
