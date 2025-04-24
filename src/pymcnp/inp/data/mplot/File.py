import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class File(MplotOption, keyword='file'):
    """
    Represents INP file elements.

    Attributes:
        aa: Graphics metafile on/off.
    """

    _ATTRS = {
        'aa': types.String,
    }

    _REGEX = re.compile(r'\Afile( all|none)?\Z')

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
class FileBuilder:
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

        aa = None
        if isinstance(self.aa, types.String):
            aa = self.aa
        elif isinstance(self.aa, str):
            aa = types.String.from_mcnp(self.aa)

        return File(
            aa=aa,
        )
