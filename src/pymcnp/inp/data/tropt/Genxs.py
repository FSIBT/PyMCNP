import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types


class Genxs(_option.TroptOption):
    """
    Represents INP genxs elements.

    Attributes:
        filename: Cross section generation setting.
    """

    _KEYWORD = 'genxs'

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'\Agenxs( {types.String._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, filename: types.String = None):
        """
        Initializes ``Genxs``.

        Parameters:
            filename: Cross section generation setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                filename,
            ]
        )

        self.filename: typing.Final[types.String] = filename


@dataclasses.dataclass
class GenxsBuilder(_option.TroptOptionBuilder):
    """
    Builds ``Genxs``.

    Attributes:
        filename: Cross section generation setting.
    """

    filename: str | types.String = None

    def build(self):
        """
        Builds ``GenxsBuilder`` into ``Genxs``.

        Returns:
            ``Genxs`` for ``GenxsBuilder``.
        """

        filename = self.filename
        if isinstance(self.filename, types.String):
            filename = self.filename
        elif isinstance(self.filename, str):
            filename = types.String.from_mcnp(self.filename)

        return Genxs(
            filename=filename,
        )

    @staticmethod
    def unbuild(ast: Genxs):
        """
        Unbuilds ``Genxs`` into ``GenxsBuilder``

        Returns:
            ``GenxsBuilder`` for ``Genxs``.
        """

        return GenxsBuilder(
            filename=copy.deepcopy(ast.filename),
        )
