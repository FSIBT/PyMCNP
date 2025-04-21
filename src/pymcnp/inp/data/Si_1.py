import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Si_1(DataOption, keyword='si'):
    """
    Represents INP si variation #1 elements.

    Attributes:
        suffix: Data card option suffix.
        option: Information kind setting.
        information: Particle source information.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'option': types.String,
        'information': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(
        rf'\Asi(\d+)( {types.String._REGEX.pattern})((?: {types.RealOrJump._REGEX.pattern})+?)\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        option: types.String,
        information: types.Tuple[types.RealOrJump],
    ):
        """
        Initializes ``Si_1``.

        Parameters:
            suffix: Data card option suffix.
            option: Information kind setting.
            information: Particle source information.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if option is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, option)
        if information is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, information)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                option,
                information,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.option: typing.Final[types.String] = option
        self.information: typing.Final[types.Tuple[types.RealOrJump]] = information


@dataclasses.dataclass
class SiBuilder_1:
    """
    Builds ``Si_1``.

    Attributes:
        suffix: Data card option suffix.
        option: Information kind setting.
        information: Particle source information.
    """

    suffix: str | int | types.Integer
    option: str | types.String
    information: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``SiBuilder_1`` into ``Si_1``.

        Returns:
            ``Si_1`` for ``SiBuilder_1``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if isinstance(self.option, types.String):
            option = self.option
        elif isinstance(self.option, str):
            option = types.String.from_mcnp(self.option)

        information = []
        for item in self.information:
            if isinstance(item, types.RealOrJump):
                information.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                information.append(types.RealOrJump(item))
            elif isinstance(item, str):
                information.append(types.RealOrJump.from_mcnp(item))
        information = types.Tuple(information)

        return Si_1(
            suffix=suffix,
            option=option,
            information=information,
        )
