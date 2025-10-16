import re
import typing

from . import _type
from .Integer import Integer
from .. import errors


class Distribution(_type.Type):
    """
    Represents MCNP distribution numbers.

    Attributes:
        n: Distribution identifier.
    """

    _REGEX = re.compile(r'\A(?:(?:[dD](\d+))|0)\Z', re.IGNORECASE)

    def __init__(self, n: Integer):
        """
        Initializes `Distribution`.

        Parameters:
            n: Distribution identifier.

        Returns:
            `Distribution`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if n is None or not (0 <= n <= 999):
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, n)

        self.n: typing.Final[Integer] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Distribution` from MCNP.

        Parameters:
            source: MCNP for `Distribution`.

        Returns:
            `Distribution`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = re.match(r'\A(?:[dD](\d|\d\d|\d\d\d))|(?:0)\Z', source)

        if tokens is None:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        n = Integer.from_mcnp(tokens[1]) if tokens[1] else Integer(0)

        return Distribution(n)

    def to_mcnp(self):
        """
        Generates MCNP from `Distribution`.

        Returns:
            MCNP for `Distribution`.
        """

        return f'd{self.n}'
