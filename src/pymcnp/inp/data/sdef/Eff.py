import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Eff(_option.SdefOption):
    """
    Represents INP eff elements.

    Attributes:
        criterion: Rejection efficiency criterion for position sampling.
    """

    _KEYWORD = 'eff'

    _ATTRS = {
        'criterion': types.Real,
    }

    _REGEX = re.compile(rf'\Aeff( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, criterion: types.Real):
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

        self.criterion: typing.Final[types.Real] = criterion


@dataclasses.dataclass
class EffBuilder(_option.SdefOptionBuilder):
    """
    Builds ``Eff``.

    Attributes:
        criterion: Rejection efficiency criterion for position sampling.
    """

    criterion: str | float | types.Real

    def build(self):
        """
        Builds ``EffBuilder`` into ``Eff``.

        Returns:
            ``Eff`` for ``EffBuilder``.
        """

        criterion = self.criterion
        if isinstance(self.criterion, types.Real):
            criterion = self.criterion
        elif isinstance(self.criterion, float) or isinstance(self.criterion, int):
            criterion = types.Real(self.criterion)
        elif isinstance(self.criterion, str):
            criterion = types.Real.from_mcnp(self.criterion)

        return Eff(
            criterion=criterion,
        )

    @staticmethod
    def unbuild(ast: Eff):
        """
        Unbuilds ``Eff`` into ``EffBuilder``

        Returns:
            ``EffBuilder`` for ``Eff``.
        """

        return EffBuilder(
            criterion=copy.deepcopy(ast.criterion),
        )
