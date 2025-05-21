import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Sp_0(DataOption):
    """
    Represents INP sp variation #0 elements.

    Attributes:
        suffix: Data card option suffix.
        option: Probability kind setting.
        probabilities: Particle source probabilities.
    """

    _KEYWORD = 'sp'

    _ATTRS = {
        'suffix': types.Integer,
        'option': types.String,
        'probabilities': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Asp(\d+)( [dcvw])?((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(
        self,
        suffix: types.Integer,
        probabilities: types.Tuple[types.Real],
        option: types.String = None,
    ):
        """
        Initializes ``Sp_0``.

        Parameters:
            suffix: Data card option suffix.
            option: Probability kind setting.
            probabilities: Particle source probabilities.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (1 <= suffix.value <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if option is not None and option not in {'d', 'c', 'v', 'w'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, option)
        if probabilities is None or not (
            filter(lambda entry: not (0 <= entry.value <= 1), probabilities)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, probabilities)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                option,
                probabilities,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.option: typing.Final[types.String] = option
        self.probabilities: typing.Final[types.Tuple[types.Real]] = probabilities


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
    probabilities: list[str] | list[float] | list[types.Real]
    option: str | types.String = None

    def build(self):
        """
        Builds ``SpBuilder_0`` into ``Sp_0``.

        Returns:
            ``Sp_0`` for ``SpBuilder_0``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        option = self.option
        if isinstance(self.option, types.String):
            option = self.option
        elif isinstance(self.option, str):
            option = types.String.from_mcnp(self.option)

        if self.probabilities:
            probabilities = []
            for item in self.probabilities:
                if isinstance(item, types.Real):
                    probabilities.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    probabilities.append(types.Real(item))
                elif isinstance(item, str):
                    probabilities.append(types.Real.from_mcnp(item))
            probabilities = types.Tuple(probabilities)
        else:
            probabilities = None

        return Sp_0(
            suffix=suffix,
            option=option,
            probabilities=probabilities,
        )

    @staticmethod
    def unbuild(ast: Sp_0):
        """
        Unbuilds ``Sp_0`` into ``SpBuilder_0``

        Returns:
            ``SpBuilder_0`` for ``Sp_0``.
        """

        return Sp_0(
            suffix=copy.deepcopy(ast.suffix),
            option=copy.deepcopy(ast.option),
            probabilities=copy.deepcopy(ast.probabilities),
        )
