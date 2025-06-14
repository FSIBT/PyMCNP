import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Mgeoin(_option.EmbedOption):
    """
    Represents INP mgeoin elements.

    Attributes:
        filename: Name of the input file containing the mesh description.
    """

    _KEYWORD = 'mgeoin'

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'\Amgeoin( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, filename: types.String):
        """
        Initializes ``Mgeoin``.

        Parameters:
            filename: Name of the input file containing the mesh description.

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
class MgeoinBuilder(_option.EmbedOptionBuilder):
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

        filename = self.filename
        if isinstance(self.filename, types.String):
            filename = self.filename
        elif isinstance(self.filename, str):
            filename = types.String.from_mcnp(self.filename)

        return Mgeoin(
            filename=filename,
        )

    @staticmethod
    def unbuild(ast: Mgeoin):
        """
        Unbuilds ``Mgeoin`` into ``MgeoinBuilder``

        Returns:
            ``MgeoinBuilder`` for ``Mgeoin``.
        """

        return MgeoinBuilder(
            filename=copy.deepcopy(ast.filename),
        )
