import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Eints(_option.FmeshOption):
    """
    Represents INP eints elements.

    Attributes:
        count: Number of mesh points for each mesh energy.
    """

    _KEYWORD = 'eints'

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'\Aeints( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``Eints``.

        Parameters:
            count: Number of mesh points for each mesh energy.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if count is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, count)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                count,
            ]
        )

        self.count: typing.Final[types.Integer] = count


@dataclasses.dataclass
class EintsBuilder(_option.FmeshOptionBuilder):
    """
    Builds ``Eints``.

    Attributes:
        count: Number of mesh points for each mesh energy.
    """

    count: str | int | types.Integer

    def build(self):
        """
        Builds ``EintsBuilder`` into ``Eints``.

        Returns:
            ``Eints`` for ``EintsBuilder``.
        """

        count = self.count
        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.Integer(self.count)
        elif isinstance(self.count, str):
            count = types.Integer.from_mcnp(self.count)

        return Eints(
            count=count,
        )

    @staticmethod
    def unbuild(ast: Eints):
        """
        Unbuilds ``Eints`` into ``EintsBuilder``

        Returns:
            ``EintsBuilder`` for ``Eints``.
        """

        return EintsBuilder(
            count=copy.deepcopy(ast.count),
        )
