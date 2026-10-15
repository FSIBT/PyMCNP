import re
import typing

from . import _type
from .. import errors


def Tuple(element: type) -> object:
    """
    Curries tuples and inner type.

    Parametres:
        element: Inner type.

    Returns:
        `_Tuple` with inner type.
    """

    class _Tuple(_type.Type):
        """
        Represents generic MCNP collections.

        Attributes:
            value: Tuple value.
        """

        def __init__(self, value: tuple[element]):
            """
            Initializes `Tuple`.

            Parameters:
                value: Tuple object.

            Returns:
                `Tuple`.

            Raises:
                TypesError: SEMANTICS_TYPE.
            """

            if value is None or value == tuple() or None in value:
                raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, value)

            self.value: typing.Final[tuple[element]] = value

        @classmethod
        def from_mcnp(cls, source: str):
            """
            Generates `Tuple` from MCNP.

            Parameters:
                source: MCNP tuple.
                T: Inner type.

            Returns:
                `Tuple`.

            Raises:
                TypesError: SYNTAX_TYPE.
            """

            pattern = element._REGEX.pattern[2:-2]
            tokens = list(re.finditer(rf'(?:{pattern})(?=(?:\s+(?:{pattern}))*\s*\Z)', source, re.IGNORECASE))
            leftover = source
            for token in reversed(tokens):
                leftover = leftover[: token.start()] + leftover[token.end() :]
            if leftover.strip():
                raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

            return _Tuple([element.from_mcnp(token[0]) for token in tokens])

        def to_mcnp(self):
            """
            Generates MCNP from `Tuple`.

            Returns:
                MCNP for `Tuple`.
            """

            return ' '.join(val.to_mcnp() if val is not None else '' for val in self.value)

        def __iter__(self):
            return self.value.__iter__()

        def __getitem__(self, index):
            return self.value.__getitem__(index)

        def __contains__(self, item):
            return self.value.__contains__(item)

    return _Tuple
