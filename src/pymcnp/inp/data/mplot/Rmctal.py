import re
import copy
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Rmctal(MplotOption):
    """
    Represents INP rmctal elements.

    Attributes:
        filename: MCTAL file to read.
    """

    _KEYWORD = 'rmctal'

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'\Armctal( {types.String._REGEX.pattern})\Z')

    def __init__(self, filename: types.String):
        """
        Initializes ``Rmctal``.

        Parameters:
            filename: MCTAL file to read.

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
class RmctalBuilder:
    """
    Builds ``Rmctal``.

    Attributes:
        filename: MCTAL file to read.
    """

    filename: str | types.String

    def build(self):
        """
        Builds ``RmctalBuilder`` into ``Rmctal``.

        Returns:
            ``Rmctal`` for ``RmctalBuilder``.
        """

        filename = self.filename
        if isinstance(self.filename, types.String):
            filename = self.filename
        elif isinstance(self.filename, str):
            filename = types.String.from_mcnp(self.filename)

        return Rmctal(
            filename=filename,
        )

    @staticmethod
    def unbuild(ast: Rmctal):
        """
        Unbuilds ``Rmctal`` into ``RmctalBuilder``

        Returns:
            ``RmctalBuilder`` for ``Rmctal``.
        """

        return Rmctal(
            filename=copy.deepcopy(ast.filename),
        )
