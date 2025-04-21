import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Sb_0(DataOption, keyword='sb'):
    """
    Represents INP sb variation #0 elements.

    Attributes:
        suffix: Data card option suffix.
        option: Bias kind setting.
        biases: Particle source biases.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'option': types.String,
        'biases': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Asb(\d+)( [dcvw])?((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(
        self,
        suffix: types.Integer,
        biases: types.Tuple[types.RealOrJump],
        option: types.String = None,
    ):
        """
        Initializes ``Sb_0``.

        Parameters:
            suffix: Data card option suffix.
            option: Bias kind setting.
            biases: Particle source biases.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if option is not None and option not in {'d', 'c', 'v', 'w'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, option)
        if biases is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, biases)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                option,
                biases,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.option: typing.Final[types.String] = option
        self.biases: typing.Final[types.Tuple[types.RealOrJump]] = biases


@dataclasses.dataclass
class SbBuilder_0:
    """
    Builds ``Sb_0``.

    Attributes:
        suffix: Data card option suffix.
        option: Bias kind setting.
        biases: Particle source biases.
    """

    suffix: str | int | types.Integer
    biases: list[str] | list[float] | list[types.RealOrJump]
    option: str | types.String = None

    def build(self):
        """
        Builds ``SbBuilder_0`` into ``Sb_0``.

        Returns:
            ``Sb_0`` for ``SbBuilder_0``.
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

        biases = []
        for item in self.biases:
            if isinstance(item, types.RealOrJump):
                biases.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                biases.append(types.RealOrJump(item))
            elif isinstance(item, str):
                biases.append(types.RealOrJump.from_mcnp(item))
        biases = types.Tuple(biases)

        return Sb_0(
            suffix=suffix,
            option=option,
            biases=biases,
        )
