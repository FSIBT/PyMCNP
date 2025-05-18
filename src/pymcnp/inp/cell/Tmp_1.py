import re
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Tmp_1(CellOption):
    """
    Represents INP tmp variation #1 elements.

    Attributes:
        temperature: Temperature at time index.
    """

    _ATTRS = {
        'temperature': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Atmp((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, temperature: types.Tuple[types.Real]):
        """
        Initializes ``Tmp_1``.

        Parameters:
            temperature: Temperature at time index.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if temperature is None or not (min(temperature) > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, temperature)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                temperature,
            ]
        )

        self.temperature: typing.Final[types.Tuple[types.Real]] = temperature


@dataclasses.dataclass
class TmpBuilder_1:
    """
    Builds ``Tmp_1``.

    Attributes:
        temperature: Temperature at time index.
    """

    temperature: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``TmpBuilder_1`` into ``Tmp_1``.

        Returns:
            ``Tmp_1`` for ``TmpBuilder_1``.
        """

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

        return Tmp_1(
            temperature=temperature,
        )
