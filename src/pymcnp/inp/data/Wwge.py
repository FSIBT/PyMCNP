import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Wwge(DataOption):
    """
    Represents INP wwge elements.

    Attributes:
        bounds: Upper energy bound for weight-window group to be generated.
    """

    _ATTRS = {
        'bounds': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Awwge((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, bounds: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Wwge``.

        Parameters:
            bounds: Upper energy bound for weight-window group to be generated.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if bounds is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bounds)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bounds,
            ]
        )

        self.bounds: typing.Final[types.Tuple[types.RealOrJump]] = bounds


@dataclasses.dataclass
class WwgeBuilder:
    """
    Builds ``Wwge``.

    Attributes:
        bounds: Upper energy bound for weight-window group to be generated.
    """

    bounds: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``WwgeBuilder`` into ``Wwge``.

        Returns:
            ``Wwge`` for ``WwgeBuilder``.
        """

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

        return Wwge(
            bounds=bounds,
        )
