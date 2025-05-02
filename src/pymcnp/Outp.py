import typing

from .utils import types
from .utils import errors
from .utils import _object


class Outp(_object.McnpFile):
    """
    Represents OUTP files.

    Attributes:
        lines: OUTP lines.
    """

    def __init__(self, lines: types.Tuple[types.String]):
        """
        Initializes ``Outp``.

        Parameters:
            lines: OUTP lines.

        Raises:
            OutpError: SEMANTICS_OUTP.
        """

        if lines is None or None in lines:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_OUTP, lines)

        self.lines: typing.Final[types.Tuple[types.String]] = lines

    @classmethod
    def from_mcnp(cls, source: str):
        """
        Generates ``Outp`` from OUTP.

        Parameters:
            source: OUTP for ``Outp``.

        Returns:
            ``Outp``.
        """

        lines = types.Tuple(map(lambda line: types.String(line), source.split('\n')))

        return cls(lines)

    def to_mcnp(self):
        """
        Generates OUTP from ``Outp``.

        Returns:
            OUTP for ``Outp``.
        """

        return '\n'.join(line for line in self.lines)
