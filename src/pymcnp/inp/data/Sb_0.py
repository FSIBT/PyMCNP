import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Sb_0(_option.DataOption):
    """
    Represents INP sb variation #0 elements.

    Attributes:
        suffix: Data card option suffix.
        option: Bias kind setting.
        biases: Particle source biases.
    """

    _KEYWORD = 'sb'

    _ATTRS = {
        'suffix': types.Integer,
        'option': types.String,
        'biases': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Asb(\d+)( [dcvw])?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: types.Integer, biases: types.Tuple[types.Real], option: types.String = None):
        """
        Initializes ``Sb_0``.

        Parameters:
            suffix: Data card option suffix.
            option: Bias kind setting.
            biases: Particle source biases.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (1 <= suffix.value <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if option is not None and option not in {'d', 'c', 'v', 'w'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, option)
        if biases is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, biases)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                option,
                biases,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.option: typing.Final[types.String] = option
        self.biases: typing.Final[types.Tuple[types.Real]] = biases


@dataclasses.dataclass
class SbBuilder_0(_option.DataOptionBuilder):
    """
    Builds ``Sb_0``.

    Attributes:
        suffix: Data card option suffix.
        option: Bias kind setting.
        biases: Particle source biases.
    """

    suffix: str | int | types.Integer
    biases: list[str] | list[float] | list[types.Real]
    option: str | types.String = None

    def build(self):
        """
        Builds ``SbBuilder_0`` into ``Sb_0``.

        Returns:
            ``Sb_0`` for ``SbBuilder_0``.
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

        if self.biases:
            biases = []
            for item in self.biases:
                if isinstance(item, types.Real):
                    biases.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    biases.append(types.Real(item))
                elif isinstance(item, str):
                    biases.append(types.Real.from_mcnp(item))
            biases = types.Tuple(biases)
        else:
            biases = None

        return Sb_0(
            suffix=suffix,
            option=option,
            biases=biases,
        )

    @staticmethod
    def unbuild(ast: Sb_0):
        """
        Unbuilds ``Sb_0`` into ``SbBuilder_0``

        Returns:
            ``SbBuilder_0`` for ``Sb_0``.
        """

        return SbBuilder_0(
            suffix=copy.deepcopy(ast.suffix),
            option=copy.deepcopy(ast.option),
            biases=copy.deepcopy(ast.biases),
        )
