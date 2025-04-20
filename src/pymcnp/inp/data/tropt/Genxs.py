import re
import typing
import dataclasses


from .option_ import TroptOption_
from ....utils import types
from ....utils import errors


class Genxs(TroptOption_, keyword='genxs'):
    """
    Represents INP genxs elements.

    Attributes:
        filename: Cross section generation setting.
    """

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'\Agenxs( {types.String._REGEX.pattern})\Z')

    def __init__(self, filename: types.String):
        """
        Initializes ``Genxs``.

        Parameters:
            filename: Cross section generation setting.

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
class GenxsBuilder:
    """
    Builds ``Genxs``.

    Attributes:
        filename: Cross section generation setting.
    """

    filename: str | types.String

    def build(self):
        """
        Builds ``GenxsBuilder`` into ``Genxs``.

        Returns:
            ``Genxs`` for ``GenxsBuilder``.
        """

        if isinstance(self.filename, types.String):
            filename = self.filename
        elif isinstance(self.filename, str):
            filename = types.String.from_mcnp(self.filename)

        return Genxs(
            filename=filename,
        )
