import re
import copy
import typing
import dataclasses


from ._option import PtracOption
from ....utils import types
from ....utils import errors


class Value(PtracOption):
    """
    Represents INP value elements.

    Attributes:
        cutoff: Specifies tally cutoff above which history events will be written..
    """

    _KEYWORD = 'value'

    _ATTRS = {
        'cutoff': types.Real,
    }

    _REGEX = re.compile(rf'\Avalue( {types.Real._REGEX.pattern})\Z')

    def __init__(self, cutoff: types.Real):
        """
        Initializes ``Value``.

        Parameters:
            cutoff: Specifies tally cutoff above which history events will be written..

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if cutoff is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cutoff)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cutoff,
            ]
        )

        self.cutoff: typing.Final[types.Real] = cutoff


@dataclasses.dataclass
class ValueBuilder:
    """
    Builds ``Value``.

    Attributes:
        cutoff: Specifies tally cutoff above which history events will be written..
    """

    cutoff: str | float | types.Real

    def build(self):
        """
        Builds ``ValueBuilder`` into ``Value``.

        Returns:
            ``Value`` for ``ValueBuilder``.
        """

        cutoff = self.cutoff
        if isinstance(self.cutoff, types.Real):
            cutoff = self.cutoff
        elif isinstance(self.cutoff, float) or isinstance(self.cutoff, int):
            cutoff = types.Real(self.cutoff)
        elif isinstance(self.cutoff, str):
            cutoff = types.Real.from_mcnp(self.cutoff)

        return Value(
            cutoff=cutoff,
        )

    @staticmethod
    def unbuild(ast: Value):
        """
        Unbuilds ``Value`` into ``ValueBuilder``

        Returns:
            ``ValueBuilder`` for ``Value``.
        """

        return Value(
            cutoff=copy.deepcopy(ast.cutoff),
        )
