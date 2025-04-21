import re
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Tmp(CellOption, keyword='tmp'):
    """
    Represents INP tmp elements.

    Attributes:
        suffix: Cell option suffix.
        temperature: Cell temperature at suffix time index.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'temperature': types.Real,
    }

    _REGEX = re.compile(rf'\Atmp(\d+)( {types.Real._REGEX.pattern})\Z')

    def __init__(self, suffix: types.Integer, temperature: types.Real):
        """
        Initializes ``Tmp``.

        Parameters:
            suffix: Cell option suffix.
            temperature: Cell temperature at suffix time index.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if temperature is None or not (temperature > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, temperature)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                temperature,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.temperature: typing.Final[types.Real] = temperature


@dataclasses.dataclass
class TmpBuilder:
    """
    Builds ``Tmp``.

    Attributes:
        suffix: Cell option suffix.
        temperature: Cell temperature at suffix time index.
    """

    suffix: str | int | types.Integer
    temperature: str | float | types.Real

    def build(self):
        """
        Builds ``TmpBuilder`` into ``Tmp``.

        Returns:
            ``Tmp`` for ``TmpBuilder``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if isinstance(self.temperature, types.Real):
            temperature = self.temperature
        elif isinstance(self.temperature, float) or isinstance(self.temperature, int):
            temperature = types.Real(self.temperature)
        elif isinstance(self.temperature, str):
            temperature = types.Real.from_mcnp(self.temperature)

        return Tmp(
            suffix=suffix,
            temperature=temperature,
        )
