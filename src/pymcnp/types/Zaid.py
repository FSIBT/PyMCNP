import re
import typing

from . import _type
from .. import errors


class Zaid(_type.Type):
    """
    Represents MCNP nuclide information numbers.

    Attributes:
        z: Atomic number.
        a: Mass number.
        abx: Cross-section evaluation & class information.
    """

    _REGEX = re.compile(r'\A(\d{1,3})(\d\d\d)(?:[.](\S+))?\Z', re.IGNORECASE)

    def __init__(self, z: int, a: int, abx: str = None):
        """
        Initializes `Zaid`.

        Parameters:
            z: ZAID atomic number.
            a: ZAID mass number.
            abx: ZAID cross-section evaluation & class information.

        Returns:
            `Zaid`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if z is None or not (000 <= z <= 999):
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, z)

        if a is None or not (000 <= a <= 999):
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, a)

        self.z: typing.Final[int] = z
        self.a: typing.Final[int] = a
        self.abx: typing.Final[str] = abx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Zaid` from MCNP.

        Parameters:
            source: MCNP for `Zaid`.

        Returns:
            `Zaid` object.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = Zaid._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        return Zaid(int(tokens[1]), int(tokens[2]), tokens[3])

    def to_mcnp(self) -> str:
        """
        Generates MCNP from `Zaid`.

        Returns:
            MCNP Zaid.
        """

        if self.abx:
            return f'{self.z:03}{self.a:03}.{self.abx}'
        else:
            return f'{self.z:03}{self.a:03}'
