import re

from . import _type
from .Integer import Integer
from .. import errors


class Index(_type.Type):
    """
    Represents INP lattice index entries.

    Attributes:
        lower: Lower index.
        upper: Upper index.
    """

    _REGEX = re.compile(r'\A(\S+):(\S+)\Z', re.IGNORECASE)

    def __init__(self, lower: Integer, upper: Integer):
        """
        Initializes `Index`.

        Parameters:
            lower: Lower index.
            upper: Upper index.

        Returns:
            `Index`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if lower is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, lower)

        if upper is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, upper)

        self.lower: Integer = lower
        self.upper: Integer = upper

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Index` from INP.

        Parameters:
            INP for `Index`.

        Returns:
            `Index`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = Index._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        lower = Integer.from_mcnp(tokens[1]).value
        upper = Integer.from_mcnp(tokens[2]).value

        return Index(lower, upper)

    def to_mcnp(self):
        """
        Generates INP from `Index`.

        Returns:
            INP for `Index`.
        """

        return f'{self.lower}:{self.upper}'
