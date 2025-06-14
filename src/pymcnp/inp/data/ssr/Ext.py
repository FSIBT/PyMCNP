import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Ext(_option.SsrOption):
    """
    Represents INP ext elements.

    Attributes:
        number: Distribution number for baising sampling.
    """

    _KEYWORD = 'ext'

    _ATTRS = {
        'number': types.DistributionNumber,
    }

    _REGEX = re.compile(rf'\Aext( {types.DistributionNumber._REGEX.pattern[2:-2]})\Z')

    def __init__(self, number: types.DistributionNumber):
        """
        Initializes ``Ext``.

        Parameters:
            number: Distribution number for baising sampling.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if number is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.DistributionNumber] = number


@dataclasses.dataclass
class ExtBuilder(_option.SsrOptionBuilder):
    """
    Builds ``Ext``.

    Attributes:
        number: Distribution number for baising sampling.
    """

    number: str | types.DistributionNumber

    def build(self):
        """
        Builds ``ExtBuilder`` into ``Ext``.

        Returns:
            ``Ext`` for ``ExtBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.DistributionNumber):
            number = self.number
        elif isinstance(self.number, str):
            number = types.DistributionNumber.from_mcnp(self.number)

        return Ext(
            number=number,
        )

    @staticmethod
    def unbuild(ast: Ext):
        """
        Unbuilds ``Ext`` into ``ExtBuilder``

        Returns:
            ``ExtBuilder`` for ``Ext``.
        """

        return ExtBuilder(
            number=copy.deepcopy(ast.number),
        )
