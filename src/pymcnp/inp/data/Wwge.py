import re
import copy
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

    _KEYWORD = 'wwge'

    _ATTRS = {
        'bounds': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Awwge((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, bounds: types.Tuple[types.Real]):
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

        self.bounds: typing.Final[types.Tuple[types.Real]] = bounds


@dataclasses.dataclass
class WwgeBuilder:
    """
    Builds ``Wwge``.

    Attributes:
        bounds: Upper energy bound for weight-window group to be generated.
    """

    bounds: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``WwgeBuilder`` into ``Wwge``.

        Returns:
            ``Wwge`` for ``WwgeBuilder``.
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

        return Wwge(
            bounds=bounds,
        )

    @staticmethod
    def unbuild(ast: Wwge):
        """
        Unbuilds ``Wwge`` into ``WwgeBuilder``

        Returns:
            ``WwgeBuilder`` for ``Wwge``.
        """

        return Wwge(
            bounds=copy.deepcopy(ast.bounds),
        )
