import re
import typing


from .option_ import EmbedOption_
from ....utils import types
from ....utils import errors


class Meshgeo(EmbedOption_, keyword='meshgeo'):
    """
    Represents INP meshgeo elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'form': types.String,
    }

    _REGEX = re.compile(r'meshgeo( \S+)')

    def __init__(self, form: types.String):
        """
        Initializes ``Meshgeo``.

        Parameters:
            form: Format specification of the embedded mesh input file.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if form is None or form not in {'lnk3dnt', 'abaqu', 'mcnpum'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, form)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                form,
            ]
        )

        self.form: typing.Final[types.String] = form
