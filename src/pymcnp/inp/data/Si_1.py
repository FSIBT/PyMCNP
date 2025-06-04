import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Si_1(DataOption):
    """
    Represents INP si variation #1 elements.

    Attributes:
        suffix: Data card option suffix.
        option: Information kind setting.
        information: Particle source information.
    """

    _KEYWORD = 'si'

    _ATTRS = {
        'suffix': types.Integer,
        'option': types.String,
        'information': types.Tuple[types.Real],
    }

    _REGEX = re.compile(
        rf'\Asi(\d+)( {types.String._REGEX.pattern[2:-2]})?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        information: types.Tuple[types.Real],
        option: types.String = None,
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
        self.information: typing.Final[types.Tuple[types.Real]] = information


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
    information: list[str] | list[float] | list[types.Real]
    option: str | types.String = None

    def build(self):
        """
        Builds ``SiBuilder_1`` into ``Si_1``.

        Returns:
            ``Si_1`` for ``SiBuilder_1``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        option = self.option
        if isinstance(self.option, types.String):
            option = self.option
        elif isinstance(self.option, str):
            option = types.String.from_mcnp(self.option)

        if self.information:
            information = []
            for item in self.information:
                if isinstance(item, types.Real):
                    information.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    information.append(types.Real(item))
                elif isinstance(item, str):
                    information.append(types.Real.from_mcnp(item))
            information = types.Tuple(information)
        else:
            information = None

        return Si_1(
            suffix=suffix,
            option=option,
            information=information,
        )

    @staticmethod
    def unbuild(ast: Si_1):
        """
        Unbuilds ``Si_1`` into ``SiBuilder_1``

        Returns:
            ``SiBuilder_1`` for ``Si_1``.
        """

        return Si_1(
            suffix=copy.deepcopy(ast.suffix),
            option=copy.deepcopy(ast.option),
            information=copy.deepcopy(ast.information),
        )
