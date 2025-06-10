import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Refc(_option.MOption_0):
    """
    Represents INP refc elements.

    Attributes:
        coefficents: Cauchy coefficents.
    """

    _KEYWORD = 'refc'

    _ATTRS = {
        'coefficents': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Arefc((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, coefficents: types.Tuple[types.Real]):
        """
        Initializes ``Refc``.

        Parameters:
            coefficents: Cauchy coefficents.

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
class RefcBuilder(_option.MOptionBuilder_0):
    """
    Builds ``Refc``.

    Attributes:
        coefficents: Cauchy coefficents.
    """

    coefficents: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``RefcBuilder`` into ``Refc``.

        Returns:
            ``Refc`` for ``RefcBuilder``.
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

        return Refc(
            coefficents=coefficents,
        )

    @staticmethod
    def unbuild(ast: Refc):
        """
        Unbuilds ``Refc`` into ``RefcBuilder``

        Returns:
            ``RefcBuilder`` for ``Refc``.
        """

        return RefcBuilder(
            coefficents=copy.deepcopy(ast.coefficents),
        )
