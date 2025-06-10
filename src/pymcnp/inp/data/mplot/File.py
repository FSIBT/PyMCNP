import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class File(_option.MplotOption):
    """
    Represents INP file elements.

    Attributes:
        aa: Graphics metafile on/off.
    """

    _KEYWORD = 'file'

    _ATTRS = {
        'aa': types.String,
    }

    _REGEX = re.compile(r'\Afile(?: (all|none))?\Z')

    def __init__(self, aa: types.String = None):
        """
        Initializes ``File``.

        Parameters:
            aa: Graphics metafile on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if aa is not None and aa not in {'all', 'none'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, aa)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                aa,
            ]
        )

        self.aa: typing.Final[types.String] = aa


@dataclasses.dataclass
class FileBuilder(_option.MplotOptionBuilder):
    """
    Builds ``File``.

    Attributes:
        aa: Graphics metafile on/off.
    """

    aa: str | types.String = None

    def build(self):
        """
        Builds ``FileBuilder`` into ``File``.

        Returns:
            ``File`` for ``FileBuilder``.
        """

        aa = self.aa
        if isinstance(self.aa, types.String):
            aa = self.aa
        elif isinstance(self.aa, str):
            aa = types.String.from_mcnp(self.aa)

        return File(
            aa=aa,
        )

    @staticmethod
    def unbuild(ast: File):
        """
        Unbuilds ``File`` into ``FileBuilder``

        Returns:
            ``FileBuilder`` for ``File``.
        """

        return FileBuilder(
            aa=copy.deepcopy(ast.aa),
        )
