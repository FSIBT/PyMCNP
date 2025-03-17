import typing

from . import meshtal
from .utils import errors
from .utils import _object


class Meshtal(_object.McnpFile_):
    """
    Represents MESTHAL files.

    Attributes:
        header: MESHTAL header.
        tallies: MESTHAL tallies.
    """

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
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_MESHTAL_HEADER)

        if tallies is None:
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_MESHTAL_TALLIES)

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

        header, lines = meshtal.Header.from_mcnp(source)

        def tallies(lines):
            while lines:
                tally, lines = meshtal.Tally.from_mcnp(lines, header)
                yield tally
            return

        tallies = tallies(lines)

        return Meshtal(header, tallies)

    def to_mcnp(self):
        """
        Generates MESHTAL from ``Meshtal``.

        Returns:
            INP for ``Meshtal``.
        """

        assert False, "I'm working on it!"
