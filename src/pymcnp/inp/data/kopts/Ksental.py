import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Ksental(_option.KoptsOption):
    """
    Represents INP ksental elements.

    Attributes:
        fileopt: Format of sensity profiles output file.
    """

    _KEYWORD = 'ksental'

    _ATTRS = {
        'fileopt': types.String,
    }

    _REGEX = re.compile(rf'\Aksental( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, fileopt: types.String):
        """
        Initializes ``Ksental``.

        Parameters:
            fileopt: Format of sensity profiles output file.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if fileopt is None or fileopt not in {'mctal', 'tsunami-b'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fileopt)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fileopt,
            ]
        )

        self.fileopt: typing.Final[types.String] = fileopt


@dataclasses.dataclass
class KsentalBuilder(_option.KoptsOptionBuilder):
    """
    Builds ``Ksental``.

    Attributes:
        fileopt: Format of sensity profiles output file.
    """

    fileopt: str | types.String

    def build(self):
        """
        Builds ``KsentalBuilder`` into ``Ksental``.

        Returns:
            ``Ksental`` for ``KsentalBuilder``.
        """

        fileopt = self.fileopt
        if isinstance(self.fileopt, types.String):
            fileopt = self.fileopt
        elif isinstance(self.fileopt, str):
            fileopt = types.String.from_mcnp(self.fileopt)

        return Ksental(
            fileopt=fileopt,
        )

    @staticmethod
    def unbuild(ast: Ksental):
        """
        Unbuilds ``Ksental`` into ``KsentalBuilder``

        Returns:
            ``KsentalBuilder`` for ``Ksental``.
        """

        return KsentalBuilder(
            fileopt=copy.deepcopy(ast.fileopt),
        )
