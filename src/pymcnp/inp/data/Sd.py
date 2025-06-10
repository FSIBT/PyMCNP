import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Sd(_option.DataOption):
    """
    Represents INP sd elements.

    Attributes:
        suffix: Data card option suffix.
        information: Area, volume, or mass by segmented, surface/cell.
    """

    _KEYWORD = 'sd'

    _ATTRS = {
        'suffix': types.Integer,
        'information': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Asd(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: types.Integer, information: types.Tuple[types.Real]):
        """
        Initializes ``Sd``.

        Parameters:
            suffix: Data card option suffix.
            information: Area, volume, or mass by segmented, surface/cell.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if information is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, information)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                information,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.information: typing.Final[types.Tuple[types.Real]] = information


@dataclasses.dataclass
class SdBuilder(_option.DataOptionBuilder):
    """
    Builds ``Sd``.

    Attributes:
        suffix: Data card option suffix.
        information: Area, volume, or mass by segmented, surface/cell.
    """

    suffix: str | int | types.Integer
    information: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``SdBuilder`` into ``Sd``.

        Returns:
            ``Sd`` for ``SdBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if self.information:
            information = []
            for item in self.information:
                if isinstance(item, types.Real):
                    information.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    information.append(types.Real(item))
                elif isinstance(item, str):
                    information.append(types.Real.from_mcnp(item))
            information = types.Tuple(information)
        else:
            information = None

        return Sd(
            suffix=suffix,
            information=information,
        )

    @staticmethod
    def unbuild(ast: Sd):
        """
        Unbuilds ``Sd`` into ``SdBuilder``

        Returns:
            ``SdBuilder`` for ``Sd``.
        """

        return SdBuilder(
            suffix=copy.deepcopy(ast.suffix),
            information=copy.deepcopy(ast.information),
        )
