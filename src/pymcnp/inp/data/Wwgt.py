import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Wwgt(DataOption_, keyword='wwgt'):
    """
    Represents INP wwgt elements.

    Attributes:
        bounds: Upper time bound for weight-window group to be generated.
    """

    _ATTRS = {
        'bounds': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Awwgt((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, bounds: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Wwgt``.

        Parameters:
            bounds: Upper time bound for weight-window group to be generated.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if bounds is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bounds)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bounds,
            ]
        )

        self.bounds: typing.Final[types.Tuple[types.RealOrJump]] = bounds


@dataclasses.dataclass
class WwgtBuilder:
    """
    Builds ``Wwgt``.

    Attributes:
        bounds: Upper time bound for weight-window group to be generated.
    """

    bounds: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``WwgtBuilder`` into ``Wwgt``.

        Returns:
            ``Wwgt`` for ``WwgtBuilder``.
        """

        bounds = []
        for item in self.bounds:
            if isinstance(item, types.RealOrJump):
                bounds.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                bounds.append(types.RealOrJump(item))
            elif isinstance(item, str):
                bounds.append(types.RealOrJump.from_mcnp(item))
        bounds = types.Tuple(bounds)

        return Wwgt(
            bounds=bounds,
        )
