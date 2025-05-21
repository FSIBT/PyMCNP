import re
import copy
import typing
import dataclasses


from ._option import EmbedOption
from ....utils import types
from ....utils import errors


class Meshgeo(EmbedOption):
    """
    Represents INP meshgeo elements.

    Attributes:
        form: Format specification of the embedded mesh input file.
    """

    _KEYWORD = 'meshgeo'

    _ATTRS = {
        'form': types.String,
    }

    _REGEX = re.compile(rf'\Ameshgeo( {types.String._REGEX.pattern})\Z')

    def __init__(self, form: types.String):
        """
        Initializes ``Meshgeo``.

        Parameters:
            form: Format specification of the embedded mesh input file.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if form is None or form not in {'lnk3dnt', 'abaqu', 'mcnpum'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, form)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                form,
            ]
        )

        self.form: typing.Final[types.String] = form


@dataclasses.dataclass
class MeshgeoBuilder:
    """
    Builds ``Meshgeo``.

    Attributes:
        form: Format specification of the embedded mesh input file.
    """

    form: str | types.String

    def build(self):
        """
        Builds ``MeshgeoBuilder`` into ``Meshgeo``.

        Returns:
            ``Meshgeo`` for ``MeshgeoBuilder``.
        """

        form = self.form
        if isinstance(self.form, types.String):
            form = self.form
        elif isinstance(self.form, str):
            form = types.String.from_mcnp(self.form)

        return Meshgeo(
            form=form,
        )

    @staticmethod
    def unbuild(ast: Meshgeo):
        """
        Unbuilds ``Meshgeo`` into ``MeshgeoBuilder``

        Returns:
            ``MeshgeoBuilder`` for ``Meshgeo``.
        """

        return Meshgeo(
            form=copy.deepcopy(ast.form),
        )
