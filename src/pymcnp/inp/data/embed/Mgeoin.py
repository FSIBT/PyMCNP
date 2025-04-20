import re
import typing
import dataclasses


from .option_ import EmbedOption_
from ....utils import types
from ....utils import errors


class Mgeoin(EmbedOption_, keyword='mgeoin'):
    """
    Represents INP mgeoin elements.

    Attributes:
        filename: Name of the input file containing the mesh description.
    """

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'\Amgeoin( {types.String._REGEX.pattern})\Z')

    def __init__(self, filename: types.String):
        """
        Initializes ``Mgeoin``.

        Parameters:
            filename: Name of the input file containing the mesh description.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if filename is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, filename)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                filename,
            ]
        )

        self.filename: typing.Final[types.String] = filename


@dataclasses.dataclass
class MgeoinBuilder:
    """
    Builds ``Mgeoin``.

    Attributes:
        filename: Name of the input file containing the mesh description.
    """

    filename: str | types.String

    def build(self):
        """
        Builds ``MgeoinBuilder`` into ``Mgeoin``.

        Returns:
            ``Mgeoin`` for ``MgeoinBuilder``.
        """

        if isinstance(self.filename, types.String):
            filename = self.filename
        elif isinstance(self.filename, str):
            filename = types.String.from_mcnp(self.filename)

        return Mgeoin(
            filename=filename,
        )
