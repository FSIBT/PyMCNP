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
        bounds: Upper time bound for weight-window group to be generated.
    """

    _KEYWORD = 'wwgt'

    _ATTRS = {
        'bounds': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Awwgt((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, bounds: types.Tuple[types.Real]):
        """
        Initializes ``Wwgt``.

        Parameters:
            bounds: Upper time bound for weight-window group to be generated.

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

        self.bounds: typing.Final[types.Tuple[types.Real]] = bounds


@dataclasses.dataclass
class WwgtBuilder:
    """
    Builds ``Wwgt``.

    Attributes:
        bounds: Upper time bound for weight-window group to be generated.
    """

    bounds: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``WwgtBuilder`` into ``Wwgt``.

        Returns:
            ``Wwgt`` for ``WwgtBuilder``.
        """

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
            bounds=copy.deepcopy(ast.bounds),
        )
