import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Si_2(_option.DataOption):
    """
    Represents INP si variation #2 elements.

    Attributes:
        suffix: Data card option suffix.
        option: Information kind setting.
        information: Particle source information.
    """

    _KEYWORD = 'si'

    _ATTRS = {
        'suffix': types.Integer,
        'option': types.String,
        'information': types.Tuple[types.Designator],
    }

    _REGEX = re.compile(rf'\Asi(\d+)( {types.String._REGEX.pattern[2:-2]})?((?: {types.Designator._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: types.Integer, information: types.Tuple[types.Designator], option: types.String = None):
        """
        Initializes ``Si_2``.

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
        self.information: typing.Final[types.Tuple[types.Designator]] = information


@dataclasses.dataclass
class SiBuilder_2(_option.DataOptionBuilder):
    """
    Builds ``Si_2``.

    Attributes:
        suffix: Data card option suffix.
        option: Information kind setting.
        information: Particle source information.
    """

    suffix: str | int | types.Integer
    information: list[str] | list[types.Designator]
    option: str | types.String = None

    def build(self):
        """
        Builds ``SiBuilder_2`` into ``Si_2``.

        Returns:
            ``Si_2`` for ``SiBuilder_2``.
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
                if isinstance(item, types.Designator):
                    information.append(item)
                elif isinstance(item, str):
                    information.append(types.Designator.from_mcnp(item))
            information = types.Tuple(information)
        else:
            information = None

        return Si_2(
            suffix=suffix,
            option=option,
            information=information,
        )

    @staticmethod
    def unbuild(ast: Si_2):
        """
        Unbuilds ``Si_2`` into ``SiBuilder_2``

        Returns:
            ``SiBuilder_2`` for ``Si_2``.
        """

        return SiBuilder_2(
            suffix=copy.deepcopy(ast.suffix),
            option=copy.deepcopy(ast.option),
            information=copy.deepcopy(ast.information),
        )
