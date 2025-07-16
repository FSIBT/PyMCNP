import re
import typing

from . import _type
from .. import errors


class Tuple(tuple, _type.Type):
    """
    Represents generic MCNP collections.

    Attributes:
        value: Tuple value.
    """

    def __init__(self, value: tuple):
        """
        Initializes ``Tuple``.

        Parameters:
            value: Tuple value.

        Returns:
            ``Tuple``.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if value is None or not (value != tuple()):
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, value)

        self.value: typing.Final[tuple] = value

    @classmethod
    def from_mcnp(cls, source: str, T: typing.Type):
        """
        Generates ``Tuple`` from MCNP.

        Parameters:
            source: MCNP tuple.
            T: Inner type.

        Returns:
            ``Tuple``.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = re.finditer(T._REGEX.pattern[2:-2], source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        return Tuple([T.from_mcnp(token[0]) for token in tokens])

    def to_mcnp(self):
        """
        Generates MCNP from ``Tuple``.

        Returns:
            MCNP for ``Tuple``.
        """

        return ' '.join(val.to_mcnp() if val is not None else '' for val in self.value)
