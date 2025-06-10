import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Runtpe(_option.MplotOption):
    """
    Represents INP runtpe elements.

    Attributes:
        filename: RUNTPE file to read dump.
        n: RUNTPE read dump number.
    """

    _KEYWORD = 'runtpe'

    _ATTRS = {
        'filename': types.String,
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Aruntpe( {types.String._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, filename: types.String, n: types.Integer = None):
        """
        Initializes ``Runtpe``.

        Parameters:
            filename: RUNTPE file to read dump.
            n: RUNTPE read dump number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if filename is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, filename)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                filename,
                n,
            ]
        )

        self.filename: typing.Final[types.String] = filename
        self.n: typing.Final[types.Integer] = n


@dataclasses.dataclass
class RuntpeBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Runtpe``.

    Attributes:
        filename: RUNTPE file to read dump.
        n: RUNTPE read dump number.
    """

    filename: str | types.String
    n: str | int | types.Integer = None

    def build(self):
        """
        Builds ``RuntpeBuilder`` into ``Runtpe``.

        Returns:
            ``Runtpe`` for ``RuntpeBuilder``.
        """

        filename = self.filename
        if isinstance(self.filename, types.String):
            filename = self.filename
        elif isinstance(self.filename, str):
            filename = types.String.from_mcnp(self.filename)

        n = self.n
        if isinstance(self.n, types.Integer):
            n = self.n
        elif isinstance(self.n, int):
            n = types.Integer(self.n)
        elif isinstance(self.n, str):
            n = types.Integer.from_mcnp(self.n)

        return Runtpe(
            filename=filename,
            n=n,
        )

    @staticmethod
    def unbuild(ast: Runtpe):
        """
        Unbuilds ``Runtpe`` into ``RuntpeBuilder``

        Returns:
            ``RuntpeBuilder`` for ``Runtpe``.
        """

        return RuntpeBuilder(
            filename=copy.deepcopy(ast.filename),
            n=copy.deepcopy(ast.n),
        )
