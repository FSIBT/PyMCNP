import re
import typing
import dataclasses


from .option_ import EmbedOption_
from ....utils import types
from ....utils import errors


class Meein(EmbedOption_, keyword='meein'):
    """
    Represents INP meein elements.

    Attributes:
        filename: Name of the EEOUT results file to read.
    """

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'\Ameein( {types.String._REGEX.pattern})\Z')

    def __init__(self, filename: types.String):
        """
        Initializes ``Meein``.

        Parameters:
            filename: Name of the EEOUT results file to read.

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
class MeeinBuilder:
    """
    Builds ``Meein``.

    Attributes:
        filename: Name of the EEOUT results file to read.
    """

    filename: str | types.String

    def build(self):
        """
        Builds ``MeeinBuilder`` into ``Meein``.

        Returns:
            ``Meein`` for ``MeeinBuilder``.
        """

        if isinstance(self.filename, types.String):
            filename = self.filename
        elif isinstance(self.filename, str):
            filename = types.String.from_mcnp(self.filename)

        return Meein(
            filename=filename,
        )
