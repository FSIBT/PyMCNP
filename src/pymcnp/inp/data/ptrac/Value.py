import re
import typing
import dataclasses


from ._option import PtracOption
from ....utils import types
from ....utils import errors


class Value(PtracOption, keyword='value'):
    """
    Represents INP value elements.

    Attributes:
        cutoff: Specifies tally cutoff above which history events will be written..
    """

    _ATTRS = {
        'cutoff': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Avalue( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, cutoff: types.RealOrJump):
        """
        Initializes ``Value``.

        Parameters:
            cutoff: Specifies tally cutoff above which history events will be written..

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if cutoff is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cutoff)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cutoff,
            ]
        )

        self.cutoff: typing.Final[types.RealOrJump] = cutoff


@dataclasses.dataclass
class ValueBuilder:
    """
    Builds ``Value``.

    Attributes:
        cutoff: Specifies tally cutoff above which history events will be written..
    """

    cutoff: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``ValueBuilder`` into ``Value``.

        Returns:
            ``Value`` for ``ValueBuilder``.
        """

        if isinstance(self.cutoff, types.Real):
            cutoff = self.cutoff
        elif isinstance(self.cutoff, float) or isinstance(self.cutoff, int):
            cutoff = types.RealOrJump(self.cutoff)
        elif isinstance(self.cutoff, str):
            cutoff = types.RealOrJump.from_mcnp(self.cutoff)

        return Value(
            cutoff=cutoff,
        )
