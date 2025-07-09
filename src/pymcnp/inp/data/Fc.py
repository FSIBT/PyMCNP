import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Fc(_option.DataOption):
    """
    Represents INP fc elements.

    Attributes:
        suffix: Data card option suffix.
        info: Title for tally in output and MCTAL file.
    """

    _KEYWORD = 'fc'

    _ATTRS = {
        'suffix': types.Integer,
        'info': types.String,
    }

    _REGEX = re.compile(r'\Afc(\d+)( [\S\s]+)\Z')

    def __init__(self, suffix: types.Integer, info: types.String):
        """
        Initializes ``Fc``.

        Parameters:
            suffix: Data card option suffix.
            info: Title for tally in output and MCTAL file.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if info is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, info)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                info,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.info: typing.Final[types.String] = info


@dataclasses.dataclass
class FcBuilder(_option.DataOptionBuilder):
    """
    Builds ``Fc``.

    Attributes:
        suffix: Data card option suffix.
        info: Title for tally in output and MCTAL file.
    """

    suffix: str | int | types.Integer
    info: str | types.String

    def build(self):
        """
        Builds ``FcBuilder`` into ``Fc``.

        Returns:
            ``Fc`` for ``FcBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        info = self.info
        if isinstance(self.info, types.String):
            info = self.info
        elif isinstance(self.info, str):
            info = types.String.from_mcnp(self.info)

        return Fc(
            suffix=suffix,
            info=info,
        )

    @staticmethod
    def unbuild(ast: Fc):
        """
        Unbuilds ``Fc`` into ``FcBuilder``

        Returns:
            ``FcBuilder`` for ``Fc``.
        """

        return FcBuilder(
            suffix=copy.deepcopy(ast.suffix),
            info=copy.deepcopy(ast.info),
        )
