import re
import typing

from . import _type
from .Real import Real
from .. import errors


class Zaid(_type.Type):
    """
    Represents MCNP nuclide information numbers.

    Attributes:
        z: Atomic number.
        a: Mass number.
        abx: Cross-section evaluation & class information.
    """

    _REGEX = re.compile(r'\A(\d{1,3})(\d\d\d)(?:[.](\S+))?\Z')

    def __init__(self, z: int, a: int, abx: str = None):
        """
        Initializes ``Zaid``.

        Parameters:
            z: ZAID atomic number.
            a: ZAID mass number.
            abx: ZAID cross-section evaluation & class information.

        Returns:
            ``Zaid``.

        Raises:
            TypesError: SEMANTICS_TYPE.
            TypesError: SEMANTICS_TYPE.
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
        Generates ``Zaid`` from MCNP.

        Parameters:
            source: MCNP for ``Zaid``.

        Returns:
            ``Zaid`` object.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = Zaid._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        return Zaid(int(tokens[1]), int(tokens[2]), tokens[3])

    def to_mcnp(self) -> str:
        """
        Generates MCNP from ``Zaid``.

        Returns:
            MCNP Zaid.
        """

        if self.abx:
            return f'{self.z:03}{self.a:03}.{self.abx}'
        else:
            return f'{self.z:03}{self.a:03}'


class Substance(_type.Type):
    """
    Represents MCNP substances.

    Attributes:
        zaid: Zaid alias for nuclide.
        weight_ratio: Atomic weight ratios.
    """

    _REGEX = re.compile(r'\A(\S+) (\S+)\Z')

    def __init__(self, zaid: Zaid, weight_ratio: Real):
        """
        Initializes ``Substance``.

        Parameters:
            zaid: Zaid alias for nuclide.
            weight_ratio: Atomic weight ratios.

        Returns:
            ``Substance``.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if zaid is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, zaid)
        if weight_ratio is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, weight_ratio)

        self.zaid: typing.Final[Zaid] = zaid
        self.weight_ratio: typing.Final[Real] = weight_ratio

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Substance`` from MCNP.

        Parameters:
            MCNP for ``Substance``.

        Returns:
            ``Substance``.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = Substance._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, tokens)

        zaid = Zaid.from_mcnp(tokens[1])
        weight_ratio = Real.from_mcnp(tokens[2])

        return Substance(zaid, weight_ratio)

    def to_mcnp(self):
        """
        Generates INP from ``Substance``.

        Returns:
            INP for ``Substance``.
        """

        return f'{self.zaid} {self.weight_ratio}'
