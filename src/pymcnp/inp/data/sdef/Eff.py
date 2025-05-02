import re
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Eff(SdefOption):
    """
    Represents INP eff elements.

    Attributes:
        criterion: Rejection efficiency criterion for position sampling.
    """

    _ATTRS = {
        'criterion': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Aeff( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, criterion: types.RealOrJump):
        """
        Initializes ``Eff``.

        Parameters:
            criterion: Rejection efficiency criterion for position sampling.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if criterion is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, criterion)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                criterion,
            ]
        )

        self.criterion: typing.Final[types.RealOrJump] = criterion


@dataclasses.dataclass
class EffBuilder:
    """
    Builds ``Eff``.

    Attributes:
        criterion: Rejection efficiency criterion for position sampling.
    """

    criterion: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``EffBuilder`` into ``Eff``.

        Returns:
            ``Eff`` for ``EffBuilder``.
        """

        if isinstance(self.criterion, types.Real):
            criterion = self.criterion
        elif isinstance(self.criterion, float) or isinstance(self.criterion, int):
            criterion = types.RealOrJump(self.criterion)
        elif isinstance(self.criterion, str):
            criterion = types.RealOrJump.from_mcnp(self.criterion)

        return Eff(
            criterion=criterion,
        )
