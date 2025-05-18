import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Embdb(DataOption):
    """
    Represents INP embdb elements.

    Attributes:
        suffix: Data card option suffix.
        bounds: Tuple of upper dose energy bounds.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'bounds': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aembdb(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, suffix: types.Integer, bounds: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Embdb``.

        Parameters:
            suffix: Data card option suffix.
            bounds: Tuple of upper dose energy bounds.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if bounds is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bounds)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bounds,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.bounds: typing.Final[types.Tuple[types.RealOrJump]] = bounds


@dataclasses.dataclass
class EmbdbBuilder:
    """
    Builds ``Embdb``.

    Attributes:
        suffix: Data card option suffix.
        bounds: Tuple of upper dose energy bounds.
    """

    suffix: str | int | types.Integer
    bounds: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``EmbdbBuilder`` into ``Embdb``.

        Returns:
            ``Embdb`` for ``EmbdbBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if self.bounds:
            bounds = []
            for item in self.bounds:
                if isinstance(item, types.RealOrJump):
                    bounds.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    bounds.append(types.RealOrJump(item))
                elif isinstance(item, str):
                    bounds.append(types.RealOrJump.from_mcnp(item))
            bounds = types.Tuple(bounds)
        else:
            bounds = None

        return Embdb(
            suffix=suffix,
            bounds=bounds,
        )
