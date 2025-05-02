import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Wwt(DataOption):
    """
    Represents INP wwt elements.

    Attributes:
        designator: Data card particle designator.
        bounds: Upper time bound.
    """

    _ATTRS = {
        'designator': types.Designator,
        'bounds': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Awwt:(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, designator: types.Designator, bounds: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Wwt``.

        Parameters:
            designator: Data card particle designator.
            bounds: Upper time bound.

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
class WwtBuilder:
    """
    Builds ``Wwt``.

    Attributes:
        designator: Data card particle designator.
        bounds: Upper time bound.
    """

    designator: str | types.Designator
    bounds: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``WwtBuilder`` into ``Wwt``.

        Returns:
            ``Wwt`` for ``WwtBuilder``.
        """

        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        bounds = []
        for item in self.bounds:
            if isinstance(item, types.RealOrJump):
                bounds.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                bounds.append(types.RealOrJump(item))
            elif isinstance(item, str):
                bounds.append(types.RealOrJump.from_mcnp(item))
        bounds = types.Tuple(bounds)

        return Wwt(
            designator=designator,
            bounds=bounds,
        )
