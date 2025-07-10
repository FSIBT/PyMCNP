import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Tmp(_option.LikeOption):
    """
    Represents INP tmp elements.

    Attributes:
        suffix: Thermal time index.
        temperature: Temperature at time index.
    """

    _KEYWORD = 'tmp'

    _ATTRS = {
        'suffix': types.Integer,
        'temperature': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Atmp(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, temperature: types.Tuple[types.Real], suffix: types.Integer = None):
        """
        Initializes ``Tmp``.

        Parameters:
            suffix: Thermal time index.
            temperature: Temperature at time index.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if temperature is None or not (min(map(lambda temp: temp, temperature)) > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, temperature)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                temperature,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.temperature: typing.Final[types.Tuple[types.Real]] = temperature


@dataclasses.dataclass
class TmpBuilder(_option.LikeOptionBuilder):
    """
    Builds ``Tmp``.

    Attributes:
        suffix: Thermal time index.
        temperature: Temperature at time index.
    """

    temperature: list[str] | list[float] | list[types.Real]
    suffix: str | int | types.Integer = None

    def build(self):
        """
        Builds ``TmpBuilder`` into ``Tmp``.

        Returns:
            ``Tmp`` for ``TmpBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if self.temperature:
            temperature = []
            for item in self.temperature:
                if isinstance(item, types.Real):
                    temperature.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    temperature.append(types.Real(item))
                elif isinstance(item, str):
                    temperature.append(types.Real.from_mcnp(item))
            temperature = types.Tuple(temperature)
        else:
            temperature = None

        return Tmp(
            suffix=suffix,
            temperature=temperature,
        )

    @staticmethod
    def unbuild(ast: Tmp):
        """
        Unbuilds ``Tmp`` into ``TmpBuilder``

        Returns:
            ``TmpBuilder`` for ``Tmp``.
        """

        return TmpBuilder(
            suffix=copy.deepcopy(ast.suffix),
            temperature=copy.deepcopy(ast.temperature),
        )
