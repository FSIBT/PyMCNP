import re
import typing

from . import _type
from .. import types
from .. import errors


class Substance(_type.Type):
    """
    Represents MCNP substances.

    Attributes:
        zaid: Zaid alias for nuclide.
        weight_ratio: Atomic weight ratios.
    """

    _REGEX = re.compile(r'\A(\S+) (\S+)\Z', re.IGNORECASE)

    def __init__(self, zaid: types.Zaid, weight_ratio: types.Real):
        """
        Initializes `Substance`.

        Parameters:
            zaid: Zaid alias for nuclide.
            weight_ratio: Atomic weight ratios.

        Returns:
            `Substance`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if zaid is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, zaid)
        if weight_ratio is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, weight_ratio)

        self.zaid: typing.Final[types.Zaid] = zaid
        self.weight_ratio: typing.Final[types.Real] = weight_ratio

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Substance` from MCNP.

        Parameters:
            MCNP for `Substance`.

        Returns:
            `Substance`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = Substance._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, tokens)

        zaid = types.Zaid.from_mcnp(tokens[1])
        weight_ratio = types.Real.from_mcnp(tokens[2])

        return Substance(zaid, weight_ratio)

    def to_mcnp(self):
        """
        Generates INP from `Substance`.

        Returns:
            INP for `Substance`.
        """

        return f'{self.zaid} {self.weight_ratio}'
