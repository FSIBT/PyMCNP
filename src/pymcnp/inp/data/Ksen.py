import re
import typing
import dataclasses


from . import ksen
from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Ksen(DataOption_, keyword='ksen'):
    """
    Represents INP ksen elements.

    Attributes:
        suffix: Data card option suffix.
        sen: Type of sensitivity.
        options: Dictionary of options.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'sen': types.String,
        'options': types.Tuple[ksen.KsenOption_],
    }

    _REGEX = re.compile(
        rf'\Aksen(\d+)( {types.String._REGEX.pattern})((?: (?:{ksen.KsenOption_._REGEX.pattern}))+?)?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        sen: types.String,
        options: types.Tuple[ksen.KsenOption_] = None,
    ):
        """
        Initializes ``Ksen``.

        Parameters:
            suffix: Data card option suffix.
            sen: Type of sensitivity.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (0 < suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if sen is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, sen)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                sen,
                options,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.sen: typing.Final[types.String] = sen
        self.options: typing.Final[types.Tuple[ksen.KsenOption_]] = options


@dataclasses.dataclass
class KsenBuilder:
    """
    Builds ``Ksen``.

    Attributes:
        suffix: Data card option suffix.
        sen: Type of sensitivity.
        options: Dictionary of options.
    """

    suffix: str | int | types.Integer
    sen: str | types.String
    options: list[str] | list[ksen.KsenOption_] = None

    def build(self):
        """
        Builds ``KsenBuilder`` into ``Ksen``.

        Returns:
            ``Ksen`` for ``KsenBuilder``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if isinstance(self.sen, types.String):
            sen = self.sen
        elif isinstance(self.sen, str):
            sen = types.String.from_mcnp(self.sen)

        options = []
        for item in self.options:
            if isinstance(item, ksen.KsenOption_):
                options.append(item)
            elif isinstance(item, str):
                options.append(ksen.KsenOption_.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Ksen(
            suffix=suffix,
            sen=sen,
            options=options,
        )
