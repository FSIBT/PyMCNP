import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Tmp(_option.DataOption):
    """
    Represents INP tmp elements.

    Attributes:
        suffix: Data card option suffix.
        temperatures: Cell temperatrues.
    """

    _KEYWORD = 'tmp'

    _ATTRS = {
        'suffix': types.Integer,
        'temperatures': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Atmp(\d+)?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, temperatures: types.Tuple[types.Real], suffix: types.Integer = None):
        """
        Initializes ``Tmp``.

        Parameters:
            suffix: Data card option suffix.
            temperatures: Cell temperatrues.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if temperatures is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, temperatures)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                temperatures,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.temperatures: typing.Final[types.Tuple[types.Real]] = temperatures


@dataclasses.dataclass
class TmpBuilder(_option.DataOptionBuilder):
    """
    Builds ``Tmp``.

    Attributes:
        suffix: Data card option suffix.
        temperatures: Cell temperatrues.
    """

    temperatures: list[str] | list[float] | list[types.Real]
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

        if self.temperatures:
            temperatures = []
            for item in self.temperatures:
                if isinstance(item, types.Real):
                    temperatures.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    temperatures.append(types.Real(item))
                elif isinstance(item, str):
                    temperatures.append(types.Real.from_mcnp(item))
            temperatures = types.Tuple(temperatures)
        else:
            temperatures = None

        return Tmp(
            suffix=suffix,
            temperatures=temperatures,
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
            temperatures=copy.deepcopy(ast.temperatures),
        )
