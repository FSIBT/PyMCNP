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
        'bounds': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Awwt:(\S+)((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, designator: types.Designator, bounds: types.Tuple[types.Real]):
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
        self.bounds: typing.Final[types.Tuple[types.Real]] = bounds


@dataclasses.dataclass
class WwtBuilder:
    """
    Builds ``Wwt``.

    Attributes:
        designator: Data card particle designator.
        bounds: Upper time bound.
    """

    designator: str | types.Designator
    bounds: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``WwtBuilder`` into ``Wwt``.

        Returns:
            ``Wwt`` for ``WwtBuilder``.
        """

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        if self.bounds:
            bounds = []
            for item in self.bounds:
                if isinstance(item, types.Real):
                    bounds.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    bounds.append(types.Real(item))
                elif isinstance(item, str):
                    bounds.append(types.Real.from_mcnp(item))
            bounds = types.Tuple(bounds)
        else:
            bounds = None

        return Wwt(
            designator=designator,
            bounds=bounds,
        )
