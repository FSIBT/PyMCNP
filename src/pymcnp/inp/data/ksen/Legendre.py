import re
import copy
import typing
import dataclasses


from ._option import KsenOption
from ....utils import types
from ....utils import errors


class Legendre(KsenOption):
    """
    Represents INP legendre elements.

    Attributes:
        number: Order of Legendre moments to calculate sensitivities.
    """

    _KEYWORD = 'legendre'

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Alegendre( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Legendre``.

        Parameters:
            number: Order of Legendre moments to calculate sensitivities.

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

        self.number: typing.Final[types.Integer] = number


@dataclasses.dataclass
class LegendreBuilder:
    """
    Builds ``Legendre``.

    Attributes:
        number: Order of Legendre moments to calculate sensitivities.
    """

    number: str | int | types.Integer

    def build(self):
        """
        Builds ``LegendreBuilder`` into ``Legendre``.

        Returns:
            ``Legendre`` for ``LegendreBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        return Legendre(
            number=number,
        )

    @staticmethod
    def unbuild(ast: Legendre):
        """
        Unbuilds ``Legendre`` into ``LegendreBuilder``

        Returns:
            ``LegendreBuilder`` for ``Legendre``.
        """

        return Legendre(
            number=copy.deepcopy(ast.number),
        )
