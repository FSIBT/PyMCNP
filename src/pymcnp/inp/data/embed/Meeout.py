import re
import typing
import dataclasses


from ._option import EmbedOption
from ....utils import types
from ....utils import errors


class Meeout(EmbedOption, keyword='meeout'):
    """
    Represents INP meeout elements.

    Attributes:
        filename: Name assigned to EEOUT, the elemental edit output file.
    """

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'\Ameeout( {types.String._REGEX.pattern})\Z')

    def __init__(self, filename: types.String):
        """
        Initializes ``Meeout``.

        Parameters:
            filename: Name assigned to EEOUT, the elemental edit output file.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if filename is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, filename)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                filename,
            ]
        )

        self.filename: typing.Final[types.String] = filename


@dataclasses.dataclass
class MeeoutBuilder:
    """
    Builds ``Meeout``.

    Attributes:
        filename: Name assigned to EEOUT, the elemental edit output file.
    """

    filename: str | types.String

    def build(self):
        """
        Builds ``MeeoutBuilder`` into ``Meeout``.

        Returns:
            ``Meeout`` for ``MeeoutBuilder``.
        """

        if isinstance(self.filename, types.String):
            filename = self.filename
        elif isinstance(self.filename, str):
            filename = types.String.from_mcnp(self.filename)

        return Meeout(
            filename=filename,
        )
