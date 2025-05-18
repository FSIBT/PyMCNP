import re
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Elpt(CellOption):
    """
    Represents INP elpt elements.

    Attributes:
        designator: Cell particle designator.
        cutoff: Cell energy cutoff.
    """

    _ATTRS = {
        'designator': types.Designator,
        'cutoff': types.Real,
    }

    _REGEX = re.compile(rf'\Aelpt:(\S+)( {types.Real._REGEX.pattern})\Z')

    def __init__(self, designator: types.Designator, cutoff: types.Real):
        """
        Initializes ``Elpt``.

        Parameters:
            designator: Cell particle designator.
            cutoff: Cell energy cutoff.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if cutoff is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cutoff)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cutoff,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.cutoff: typing.Final[types.Real] = cutoff


@dataclasses.dataclass
class ElptBuilder:
    """
    Builds ``Elpt``.

    Attributes:
        designator: Cell particle designator.
        cutoff: Cell energy cutoff.
    """

    designator: str | types.Designator
    cutoff: str | float | types.Real

    def build(self):
        """
        Builds ``ElptBuilder`` into ``Elpt``.

        Returns:
            ``Elpt`` for ``ElptBuilder``.
        """

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        cutoff = self.cutoff
        if isinstance(self.cutoff, types.Real):
            cutoff = self.cutoff
        elif isinstance(self.cutoff, float) or isinstance(self.cutoff, int):
            cutoff = types.Real(self.cutoff)
        elif isinstance(self.cutoff, str):
            cutoff = types.Real.from_mcnp(self.cutoff)

        return Elpt(
            designator=designator,
            cutoff=cutoff,
        )
