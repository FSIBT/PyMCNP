import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Gmvfile(_option.EmbedOption):
    """
    Represents INP gmvfile elements.

    Attributes:
        filename: Name of the GMV output file.
    """

    _KEYWORD = 'gmvfile'

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'\Agmvfile( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, filename: types.String):
        """
        Initializes ``Gmvfile``.

        Parameters:
            filename: Name of the GMV output file.

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
class GmvfileBuilder(_option.EmbedOptionBuilder):
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

        filename = self.filename
        if isinstance(self.filename, types.String):
            filename = self.filename
        elif isinstance(self.filename, str):
            filename = types.String.from_mcnp(self.filename)

        return Gmvfile(
            filename=filename,
        )

    @staticmethod
    def unbuild(ast: Gmvfile):
        """
        Unbuilds ``Gmvfile`` into ``GmvfileBuilder``

        Returns:
            ``GmvfileBuilder`` for ``Gmvfile``.
        """

        return GmvfileBuilder(
            filename=copy.deepcopy(ast.filename),
        )
