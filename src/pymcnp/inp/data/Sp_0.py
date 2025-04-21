import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Sp_0(DataOption, keyword='sp'):
    """
    Represents INP sp variation #0 elements.

    Attributes:
        suffix: Data card option suffix.
        option: Probability kind setting.
        probabilities: Particle source probabilities.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'option': types.String,
        'probabilities': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Asp(\d+)( [dcvw])?((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(
        self,
        suffix: types.Integer,
        probabilities: types.Tuple[types.RealOrJump],
        option: types.String = None,
    ):
        """
        Initializes ``Sp_0``.

        Parameters:
            suffix: Data card option suffix.
            option: Probability kind setting.
            probabilities: Particle source probabilities.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if option is not None and option not in {'d', 'c', 'v', 'w'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, option)
        if probabilities is None or not (
            filter(lambda entry: not (0 <= entry <= 1), probabilities)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, probabilities)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                option,
                probabilities,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.option: typing.Final[types.String] = option
        self.probabilities: typing.Final[types.Tuple[types.RealOrJump]] = probabilities


@dataclasses.dataclass
class SpBuilder_0:
    """
    Builds ``Sp_0``.

    Attributes:
        suffix: Data card option suffix.
        option: Probability kind setting.
        probabilities: Particle source probabilities.
    """

    suffix: str | int | types.Integer
    probabilities: list[str] | list[float] | list[types.RealOrJump]
    option: str | types.String = None

    def build(self):
        """
        Builds ``SpBuilder_0`` into ``Sp_0``.

        Returns:
            ``Sp_0`` for ``SpBuilder_0``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        option = None
        if isinstance(self.option, types.String):
            option = self.option
        elif isinstance(self.option, str):
            option = types.String.from_mcnp(self.option)

        probabilities = []
        for item in self.probabilities:
            if isinstance(item, types.RealOrJump):
                probabilities.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                probabilities.append(types.RealOrJump(item))
            elif isinstance(item, str):
                probabilities.append(types.RealOrJump.from_mcnp(item))
        probabilities = types.Tuple(probabilities)

        return Sp_0(
            suffix=suffix,
            option=option,
            probabilities=probabilities,
        )
