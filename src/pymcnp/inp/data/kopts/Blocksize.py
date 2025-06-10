import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Blocksize(_option.KoptsOption):
    """
    Represents INP blocksize elements.

    Attributes:
        ncy: Number of cycles in every outer iteration.
    """

    _KEYWORD = 'blocksize'

    _ATTRS = {
        'ncy': types.Integer,
    }

    _REGEX = re.compile(rf'\Ablocksize( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, ncy: types.Integer):
        """
        Initializes ``Blocksize``.

        Parameters:
            ncy: Number of cycles in every outer iteration.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if ncy is None or not (ncy.value >= 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ncy)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                ncy,
            ]
        )

        self.ncy: typing.Final[types.Integer] = ncy


@dataclasses.dataclass
class BlocksizeBuilder(_option.KoptsOptionBuilder):
    """
    Builds ``Blocksize``.

    Attributes:
        ncy: Number of cycles in every outer iteration.
    """

    ncy: str | int | types.Integer

    def build(self):
        """
        Builds ``BlocksizeBuilder`` into ``Blocksize``.

        Returns:
            ``Blocksize`` for ``BlocksizeBuilder``.
        """

        ncy = self.ncy
        if isinstance(self.ncy, types.Integer):
            ncy = self.ncy
        elif isinstance(self.ncy, int):
            ncy = types.Integer(self.ncy)
        elif isinstance(self.ncy, str):
            ncy = types.Integer.from_mcnp(self.ncy)

        return Blocksize(
            ncy=ncy,
        )

    @staticmethod
    def unbuild(ast: Blocksize):
        """
        Unbuilds ``Blocksize`` into ``BlocksizeBuilder``

        Returns:
            ``BlocksizeBuilder`` for ``Blocksize``.
        """

        return BlocksizeBuilder(
            ncy=copy.deepcopy(ast.ncy),
        )
