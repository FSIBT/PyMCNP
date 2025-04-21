import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Fc(DataOption, keyword='fc'):
    """
    Represents INP fc elements.

    Attributes:
        suffix: Data card option suffix.
        info: Title for tally in output and MCTAL file.
    """

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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if info is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, info)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                info,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.info: typing.Final[types.String] = info


@dataclasses.dataclass
class FcBuilder:
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

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if isinstance(self.info, types.String):
            info = self.info
        elif isinstance(self.info, str):
            info = types.String.from_mcnp(self.info)

        return Fc(
            suffix=suffix,
            info=info,
        )
