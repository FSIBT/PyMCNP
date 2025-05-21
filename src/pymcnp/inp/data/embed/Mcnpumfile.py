import re
import copy
import typing
import dataclasses


from ._option import EmbedOption
from ....utils import types
from ....utils import errors


class Mcnpumfile(EmbedOption):
    """
    Represents INP mcnpumfile elements.

    Attributes:
        filename: Name of the MCNPUM output file.
    """

    _KEYWORD = 'mcnpumfile'

    _ATTRS = {
        'filename': types.String,
    }

    _REGEX = re.compile(rf'\Amcnpumfile( {types.String._REGEX.pattern})\Z')

    def __init__(self, filename: types.String):
        """
        Initializes ``Mcnpumfile``.

        Parameters:
            filename: Name of the MCNPUM output file.

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
class McnpumfileBuilder:
    """
    Builds ``Mcnpumfile``.

    Attributes:
        filename: Name of the MCNPUM output file.
    """

    filename: str | types.String

    def build(self):
        """
        Builds ``McnpumfileBuilder`` into ``Mcnpumfile``.

        Returns:
            ``Mcnpumfile`` for ``McnpumfileBuilder``.
        """

        filename = self.filename
        if isinstance(self.filename, types.String):
            filename = self.filename
        elif isinstance(self.filename, str):
            filename = types.String.from_mcnp(self.filename)

        return Mcnpumfile(
            filename=filename,
        )

    @staticmethod
    def unbuild(ast: Mcnpumfile):
        """
        Unbuilds ``Mcnpumfile`` into ``McnpumfileBuilder``

        Returns:
            ``McnpumfileBuilder`` for ``Mcnpumfile``.
        """

        return Mcnpumfile(
            filename=copy.deepcopy(ast.filename),
        )
