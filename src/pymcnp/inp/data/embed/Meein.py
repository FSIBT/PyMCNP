import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Meein(_option.EmbedOption):
    """
    Represents INP meein elements.

    Attributes:
        filename: Name of the EEOUT results file to read.
    """

    _KEYWORD = 'meein'

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'\Ameein( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, filename: types.String):
        """
        Initializes ``Meein``.

        Parameters:
            filename: Name of the EEOUT results file to read.

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
class MeeinBuilder(_option.EmbedOptionBuilder):
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

        filename = self.filename
        if isinstance(self.filename, types.String):
            filename = self.filename
        elif isinstance(self.filename, str):
            filename = types.String.from_mcnp(self.filename)

        return Meein(
            filename=filename,
        )

    @staticmethod
    def unbuild(ast: Meein):
        """
        Unbuilds ``Meein`` into ``MeeinBuilder``

        Returns:
            ``MeeinBuilder`` for ``Meein``.
        """

        return MeeinBuilder(
            filename=copy.deepcopy(ast.filename),
        )
