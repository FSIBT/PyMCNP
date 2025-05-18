import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Wwe(DataOption):
    """
    Represents INP wwe elements.

    Attributes:
        designator: Data card particle designator.
        bounds: Upper energy/time bound.
    """

    _ATTRS = {
        'designator': types.Designator,
        'bounds': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Awwe:(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, designator: types.Designator, bounds: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Wwe``.

        Parameters:
            designator: Data card particle designator.
            bounds: Upper energy/time bound.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if bounds is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bounds)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bounds,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.bounds: typing.Final[types.Tuple[types.RealOrJump]] = bounds


@dataclasses.dataclass
class WweBuilder:
    """
    Builds ``Wwe``.

    Attributes:
        designator: Data card particle designator.
        bounds: Upper energy/time bound.
    """

    designator: str | types.Designator
    bounds: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``WweBuilder`` into ``Wwe``.

        Returns:
            ``Wwe`` for ``WweBuilder``.
        """

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

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

        return Wwe(
            designator=designator,
            bounds=bounds,
        )
