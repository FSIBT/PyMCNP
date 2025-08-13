import re
import typing
import itertools

from . import _type
from .. import errors


def Generator(element: typing.Type) -> object:
    """
    Curries generators and inner type.

    Parametres:
        element: Inner type.

    Returns:
        `_Generator` with inner type.
    """

    class _Generator(_type.Type):
        """
        Represents generic MCNP collections.

        Attributes:
            value: Generator value.
        """

        def __init__(self, value: typing.Generator[element, None, None]):
            """
            Initializes `Generator`.

            Parameters:
                value: Generator object.

            Returns:
                `Generator`.

            Raises:
                TypesError: SEMANTICS_TYPE.
            """

            if value is None:
                raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, value)

            self.value: typing.Final[typing.Generator[element, None, None]] = value

        @classmethod
        def from_mcnp(cls, source: str):
            """
            Generates `Generator` from MCNP.

            Parameters:
                source: MCNP tuple.
                T: Inner type.

            Returns:
                `Generator`.

            Raises:
                TypesError: SYNTAX_TYPE.
            """

            value = (element.from_mcnp(token[0]) for token in re.finditer(element._REGEX.pattern[2:-2], source, re.IGNORECASE))
            return _Generator(value)

        def to_mcnp(self):
            """
            Generates MCNP from `Generator`.

            Returns:
                MCNP for `Generator`.
            """

            return ' '.join(val.to_mcnp() for val in self.__iter__())

        def __iter__(self):
            value0, value1 = itertools.tee(self.value)
            self.value = value0
            return value1

    return _Generator
