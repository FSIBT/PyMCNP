import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Wwgt(DataOption):
    """
    Represents INP wwgt elements.

    Attributes:
        designator: Data card particle designator.
        bounds: Upper time bound for weight-window group to be generated.
    """

    _KEYWORD = 'wwgt'

    _ATTRS = {
        'designator': types.Designator,
        'bounds': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Awwgt:(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, designator: types.Designator, bounds: types.Tuple[types.Real]):
        """
        Initializes ``Wwgt``.

        Parameters:
            designator: Data card particle designator.
            bounds: Upper time bound for weight-window group to be generated.

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
class WwgtBuilder:
    """
    Builds ``Wwgt``.

    Attributes:
        designator: Data card particle designator.
        bounds: Upper time bound for weight-window group to be generated.
    """

    designator: str | types.Designator
    bounds: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``WwgtBuilder`` into ``Wwgt``.

        Returns:
            ``Wwgt`` for ``WwgtBuilder``.
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

        return Wwgt(
            designator=designator,
            bounds=bounds,
        )

    @staticmethod
    def unbuild(ast: Wwgt):
        """
        Unbuilds ``Wwgt`` into ``WwgtBuilder``

        Returns:
            ``WwgtBuilder`` for ``Wwgt``.
        """

        return Wwgt(
            designator=copy.deepcopy(ast.designator),
            bounds=copy.deepcopy(ast.bounds),
        )
