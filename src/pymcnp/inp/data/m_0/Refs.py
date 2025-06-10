import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Refs(_option.MOption_0):
    """
    Represents INP refs elements.

    Attributes:
        coefficents: Sellmeier coefficents.
    """

    _KEYWORD = 'refs'

    _ATTRS = {
        'coefficents': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Arefs((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, coefficents: types.Tuple[types.Real]):
        """
        Initializes ``Refs``.

        Parameters:
            coefficents: Sellmeier coefficents.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if coefficents is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, coefficents)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                coefficents,
            ]
        )

        self.coefficents: typing.Final[types.Tuple[types.Real]] = coefficents


@dataclasses.dataclass
class RefsBuilder(_option.MOptionBuilder_0):
    """
    Builds ``Refs``.

    Attributes:
        coefficents: Sellmeier coefficents.
    """

    coefficents: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``RefsBuilder`` into ``Refs``.

        Returns:
            ``Refs`` for ``RefsBuilder``.
        """

        if self.coefficents:
            coefficents = []
            for item in self.coefficents:
                if isinstance(item, types.Real):
                    coefficents.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    coefficents.append(types.Real(item))
                elif isinstance(item, str):
                    coefficents.append(types.Real.from_mcnp(item))
            coefficents = types.Tuple(coefficents)
        else:
            coefficents = None

        return Refs(
            coefficents=coefficents,
        )

    @staticmethod
    def unbuild(ast: Refs):
        """
        Unbuilds ``Refs`` into ``RefsBuilder``

        Returns:
            ``RefsBuilder`` for ``Refs``.
        """

        return RefsBuilder(
            coefficents=copy.deepcopy(ast.coefficents),
        )
