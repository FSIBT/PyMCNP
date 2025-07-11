import re

from . import _option
from ....utils import types
from ....utils import errors


class Meshgeo(_option.EmbedOption):
    """
    Represents INP meshgeo elements.

    Attributes:
        form: Format specification of the embedded mesh input file.
    """

    _KEYWORD = 'meshgeo'

    _ATTRS = {
        'form': types.String,
    }

    _REGEX = re.compile(rf'\Ameshgeo( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, form: str | types.String):
        """
        Initializes ``Meshgeo``.

        Parameters:
            form: Format specification of the embedded mesh input file.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.form: types.String = form

    @property
    def form(self) -> types.String:
        """
        Gets ``form``.

        Returns:
            ``form``.
        """

        return self._form

    @form.setter
    def form(self, form: str | types.String) -> None:
        """
        Sets ``form``.

        Parameters:
            form: Format specification of the embedded mesh input file.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if form is not None:
            if isinstance(form, types.String):
                form = form
            elif isinstance(form, str):
                form = types.String.from_mcnp(form)
            else:
                raise TypeError

        if form is None or form not in {'lnk3dnt', 'abaqus', 'mcnpum'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, form)

        self._form: types.String = form
