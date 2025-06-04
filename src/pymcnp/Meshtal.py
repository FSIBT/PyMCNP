import re
import typing

from . import meshtal
from .utils import errors
from .utils import _object


class Meshtal(_object.McnpFile):
    """
    Represents MESTHAL files.

    Attributes:
        header: MESHTAL header.
        tallies: MESTHAL tallies.
    """

    _REGEX = re.compile(
        rf'\A({meshtal.Header._REGEX.pattern[2:-2]})((?:{meshtal.Tally._REGEX.pattern[2:-2]})+)\Z'
    )

    def __init__(
        self, header: meshtal.Header, tallies: typing.Generator[meshtal.Tally, None, None]
    ):
        """
        Initializes ``Meshtal``.

        Parameters:
            header: MESHTAL header.
            tallies: MESTHAL tallies.

        Returns:
            ``Meshtal``.

        Raises:
            MeshtalError: SEMANTICS_MESHTAL_HEADER.
            MeshtalError: SEMANTICS_MESHTAL_TALLIES.
        """

        if header is None:
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_MESHTAL)

        if tallies is None:
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_MESHTAL)

        self.header: typing.Final[meshtal.Header] = header
        self.tallies: typing.Final[
            typing.Generator[typing.Generator[meshtal.Tally, None, None]]
        ] = tallies

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Meshtal`` from MESHTAL.

        Parameters:
            source: MESHTAL for ``Meshtal``.

        Returns:
            ``Meshtal``.
        """

        tokens = Meshtal._REGEX.match(source)

        if not tokens:
            raise errors.MeshtalError(errors.MeshtalCode.SYNTAX_MESHTAL, source)

        header = meshtal.Header.from_mcnp(tokens[1])
        tallies = (
            meshtal.Tally.from_mcnp(match[0], header)
            for match in meshtal.Tally._REGEX.finditer(tokens[12])
        )

        return Meshtal(header, tallies)

    def to_mcnp(self):
        """
        Generates MESHTAL from ``Meshtal``.

        Returns:
            INP for ``Meshtal``.
        """

        return self.header.to_mcnp() + ' ' + '\n '.join(tally.to_mcnp() for tally in self.tallies)
