import re
import copy
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Tmp_0(CellOption):
    """
    Represents INP tmp variation #0 elements.

    Attributes:
        suffix: Thermal time index.
        temperature: Temperature at time index.
    """

    _KEYWORD = 'tmp'

    _ATTRS = {
        'suffix': types.Integer,
        'temperature': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Atmp(\d+)((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, suffix: types.Integer, temperature: types.Tuple[types.Real]):
        """
        Initializes ``Tmp_0``.

        Parameters:
            suffix: Thermal time index.
            temperature: Temperature at time index.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if temperature is None or not (min(map(lambda temp: temp.value, temperature)) > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, temperature)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                temperature,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.temperature: typing.Final[types.Tuple[types.Real]] = temperature


@dataclasses.dataclass
class TmpBuilder_0:
    """
    Builds ``Tmp_0``.

    Attributes:
        suffix: Thermal time index.
        temperature: Temperature at time index.
    """

    suffix: str | int | types.Integer
    temperature: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``TmpBuilder_0`` into ``Tmp_0``.

        Returns:
            ``Tmp_0`` for ``TmpBuilder_0``.
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

        return Tmp_0(
            suffix=suffix,
            temperature=temperature,
        )

    @staticmethod
    def unbuild(ast: Tmp_0):
        """
        Unbuilds ``Tmp_0`` into ``TmpBuilder_0``

        Returns:
            ``TmpBuilder_0`` for ``Tmp_0``.
        """

        return Tmp_0(
            suffix=copy.deepcopy(ast.suffix),
            temperature=copy.deepcopy(ast.temperature),
        )
