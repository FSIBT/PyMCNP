import re
import typing
import dataclasses


from ._option import EmbedOption
from ....utils import types
from ....utils import errors


class Gmvfile(EmbedOption, keyword='gmvfile'):
    """
    Represents INP gmvfile elements.

    Attributes:
        filename: Name of the GMV output file.
    """

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'\Agmvfile( {types.String._REGEX.pattern})\Z')

    def __init__(self, filename: types.String):
        """
        Initializes ``Gmvfile``.

        Parameters:
            filename: Name of the GMV output file.

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
class GmvfileBuilder:
    """
    Builds ``Gmvfile``.

    Attributes:
        filename: Name of the GMV output file.
    """

    filename: str | types.String

    def build(self):
        """
        Builds ``GmvfileBuilder`` into ``Gmvfile``.

        Returns:
            ``Gmvfile`` for ``GmvfileBuilder``.
        """

        if isinstance(self.filename, types.String):
            filename = self.filename
        elif isinstance(self.filename, str):
            filename = types.String.from_mcnp(self.filename)

        return Gmvfile(
            filename=filename,
        )
