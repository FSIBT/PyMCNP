import re
import typing

from . import _file
from . import types
from . import errors
from . import meshtal


class Meshtal(_file.File):
    """
    Represents MESTHAL files.

    Attributes:
        header: MESHTAL header.
        tallies: MESTHAL tallies.
    """

    _REGEX = re.compile(
        r'\A([^\n]{7}version [^\n]{6}ld=[^\n]{10}probid =[^\n]{20}\n\s[^\n]+\n\sNumber of histories used for normalizing tallies =[^\n]{17}\n\n\sMesh Tally Number[^\n]{10}\n\s[^\n]{8} mesh tally[.]\n\n Tally bin boundaries:\n(?:    .+\n)+\n[^\n]+\n)([\n\s\S]+)\Z',
        re.IGNORECASE,
    )

    def __init__(self, header: meshtal.Header, tallies: types.Generator(meshtal.Tally)):
        """
        Initializes `Meshtal`.

        Parameters:
            header: MESHTAL header.
            tallies: MESTHAL tallies.

        Returns:
            `Meshtal`.

        Raises:
            MeshtalError: SEMANTICS_FILE_HEADER.
            MeshtalError: SEMANTICS_FILE_TALLIES.
        """

        if header is None:
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_FILE, header)

        if tallies is None:
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_FILE, tallies)

        self.header: typing.Final[meshtal.Header] = header
        self.tallies: typing.Final[typing.Generator[typing.Generator[meshtal.Tally, None, None]]] = tallies

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Meshtal` from MESHTAL.

        Parameters:
            source: MESHTAL for `Meshtal`.

        Returns:
            `Meshtal`.
        """

        tokens = Meshtal._REGEX.match(source)

        if not tokens:
            raise errors.MeshtalError(errors.MeshtalCode.SYNTAX_FILE, source)

        header = meshtal.Header.from_mcnp(tokens[1])
        tallies = types.Generator(meshtal.Tally).from_mcnp(tokens[2])

        return Meshtal(header, tallies)

    def to_mcnp(self):
        """
        Generates MESHTAL from `Meshtal`.

        Returns:
            INP for `Meshtal`.
        """

        return self.header.to_mcnp() + '\n'.join(tally.to_mcnp() for tally in self.tallies)
