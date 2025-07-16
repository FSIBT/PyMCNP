import re
import typing

from . import _type
from .Tuple import Tuple
from .. import errors


class Distribution(_type.Type):
    """
    Represents MCNP distribution numbers.

    Attributes:
        n: Distribution identifier.
    """

    _REGEX = re.compile(r'\A[dD]\d+\Z')

    def __init__(self, n: int):
        """
        Initializes ``Distribution``.

        Parameters:
            n: Distribution identifier.

        Returns:
            ``Distribution``.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if n is None or not (1 <= n <= 999):
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, n)

        self.n: typing.Final[int] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Distribution`` from MCNP.

        Parameters:
            source: MCNP for ``Distribution``.

        Returns:
            ``Distribution``.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = re.match(r'\A[dD](\d|\d\d|\d\d\d)\Z', source)

        if tokens is None:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        return Distribution(int(tokens[1]))

    def to_mcnp(self):
        """
        Generates MCNP from ``Distribution``.

        Returns:
            MCNP for ``Distribution``.
        """

        return f'd{self.n}'


class EmbeddedDistribution(_type.Type):
    """
    Represents MCNP embedded distribution numbers.

    Attributes:
        numbers: Distribution numbers.
    """

    _REGEX = re.compile(r'\A[dD0-1<]+\Z')

    def __init__(self, numbers: tuple[Distribution]):
        """
        Initializes ``EmbeddedDistribution``.

        Parameters:
            numbers: Distribution numbers.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if numbers is None or None in numbers:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, numbers)

        self.numbers: typing.Final[tuple[Distribution]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbeddedDistribution`` from MCNP.

        Parameters:
            source: MCNP for ``EmbeddedDistribution``.

        Returns:
            ``EmbeddedDistribution`` object.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        try:
            return EmbeddedDistribution(Tuple([Distribution.from_mcnp(token) for token in source.split('>')]))
        except Exception:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

    def to_mcnp(self):
        """
        Generates MCNP from ``EmbeddedDistribution``.

        Returns:
            MCNP for ``EmbeddedDistribution``.
        """

        return '>'.join(number.to_mcnp() for number in self.numbers)
