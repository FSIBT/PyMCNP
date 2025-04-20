import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Ds_0(DataOption_, keyword='ds'):
    """
    Represents INP ds variation #0 elements.

    Attributes:
        suffix: Data card option suffix.
        option: Dependent variable setting.
        js: Depdented source dependent variables.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'option': types.String,
        'js': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(
        rf'\Ads(\d+)( [hls])?((?: {types.RealOrJump._REGEX.pattern})+?)\Z'
    )

    def __init__(
        self, suffix: types.Integer, js: types.Tuple[types.RealOrJump], option: types.String = None
    ):
        """
        Initializes ``Ds_0``.

        Parameters:
            suffix: Data card option suffix.
            option: Dependent variable setting.
            js: Depdented source dependent variables.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if option is not None and option not in {'h', 'l', 's'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, option)
        if js is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, js)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                option,
                js,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.option: typing.Final[types.String] = option
        self.js: typing.Final[types.Tuple[types.RealOrJump]] = js


@dataclasses.dataclass
class DsBuilder_0:
    """
    Builds ``Ds_0``.

    Attributes:
        suffix: Data card option suffix.
        option: Dependent variable setting.
        js: Depdented source dependent variables.
    """

    suffix: str | int | types.Integer
    js: list[str] | list[float] | list[types.RealOrJump]
    option: str | types.String = None

    def build(self):
        """
        Builds ``DsBuilder_0`` into ``Ds_0``.

        Returns:
            ``Ds_0`` for ``DsBuilder_0``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        option = None
        if isinstance(self.option, types.String):
            option = self.option
        elif isinstance(self.option, str):
            option = types.String.from_mcnp(self.option)

        js = []
        for item in self.js:
            if isinstance(item, types.RealOrJump):
                js.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                js.append(types.RealOrJump(item))
            elif isinstance(item, str):
                js.append(types.RealOrJump.from_mcnp(item))
        js = types.Tuple(js)

        return Ds_0(
            suffix=suffix,
            option=option,
            js=js,
        )
