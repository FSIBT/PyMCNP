import re
import typing
import dataclasses


from ._option import StopOption
from ....utils import types
from ....utils import errors


class Ctme(StopOption):
    """
    Represents INP ctme elements.

    Attributes:
        tme: Computer time before stop.
    """

    _ATTRS = {
        'tme': types.Real,
    }

    _REGEX = re.compile(rf'\Actme( {types.Real._REGEX.pattern})\Z')

    def __init__(self, tme: types.Real):
        """
        Initializes ``Ctme``.

        Parameters:
            tme: Computer time before stop.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if tme is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, tme)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                tme,
            ]
        )

        self.tme: typing.Final[types.Real] = tme


@dataclasses.dataclass
class CtmeBuilder:
    """
    Builds ``Ctme``.

    Attributes:
        tme: Computer time before stop.
    """

    tme: str | float | types.Real

    def build(self):
        """
        Builds ``CtmeBuilder`` into ``Ctme``.

        Returns:
            ``Ctme`` for ``CtmeBuilder``.
        """

        tme = self.tme
        if isinstance(self.tme, types.Real):
            tme = self.tme
        elif isinstance(self.tme, float) or isinstance(self.tme, int):
            tme = types.Real(self.tme)
        elif isinstance(self.tme, str):
            tme = types.Real.from_mcnp(self.tme)

        return Ctme(
            tme=tme,
        )
