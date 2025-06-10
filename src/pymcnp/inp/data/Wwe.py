import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Wwe(_option.DataOption):
    """
    Represents INP wwe elements.

    Attributes:
        designator: Data card particle designator.
        bounds: Upper energy/time bound.
    """

    _KEYWORD = 'wwe'

    _ATTRS = {
        'designator': types.Designator,
        'bounds': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Awwe:(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, designator: types.Designator, bounds: types.Tuple[types.Real]):
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
        self.bounds: typing.Final[types.Tuple[types.Real]] = bounds


@dataclasses.dataclass
class WweBuilder(_option.DataOptionBuilder):
    """
    Builds ``Wwe``.

    Attributes:
        designator: Data card particle designator.
        bounds: Upper energy/time bound.
    """

    designator: str | types.Designator
    bounds: list[str] | list[float] | list[types.Real]

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
                if isinstance(item, types.Real):
                    bounds.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    bounds.append(types.Real(item))
                elif isinstance(item, str):
                    bounds.append(types.Real.from_mcnp(item))
            bounds = types.Tuple(bounds)
        else:
            bounds = None

        return Wwe(
            designator=designator,
            bounds=bounds,
        )

    @staticmethod
    def unbuild(ast: Wwe):
        """
        Unbuilds ``Wwe`` into ``WweBuilder``

        Returns:
            ``WweBuilder`` for ``Wwe``.
        """

        return WweBuilder(
            designator=copy.deepcopy(ast.designator),
            bounds=copy.deepcopy(ast.bounds),
        )
