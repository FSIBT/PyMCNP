import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Wmctal(MplotOption):
    """
    Represents INP wmctal elements.

    Attributes:
        filename: MCTAL file to write.
    """

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'\Awmctal( {types.String._REGEX.pattern})\Z')

    def __init__(self, filename: types.String):
        """
        Initializes ``Wmctal``.

        Parameters:
            filename: MCTAL file to write.

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
class WmctalBuilder:
    """
    Builds ``Wmctal``.

    Attributes:
        filename: MCTAL file to write.
    """

    filename: str | types.String

    def build(self):
        """
        Builds ``WmctalBuilder`` into ``Wmctal``.

        Returns:
            ``Wmctal`` for ``WmctalBuilder``.
        """

        filename = self.filename
        if isinstance(self.filename, types.String):
            filename = self.filename
        elif isinstance(self.filename, str):
            filename = types.String.from_mcnp(self.filename)

        return Wmctal(
            filename=filename,
        )
