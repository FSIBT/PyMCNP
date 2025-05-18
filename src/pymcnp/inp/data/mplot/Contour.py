import re
import typing
import dataclasses


from . import contour
from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Contour(MplotOption):
    """
    Represents INP contour elements.

    Attributes:
        cmin: Contour lower limit.
        cmax: Contour upper limit.
        cstep: Contour interval.
        options: Dictionary of options.
    """

    _ATTRS = {
        'cmin': types.Real,
        'cmax': types.Real,
        'cstep': types.Real,
        'options': types.Tuple[contour.ContourOption],
    }

    _REGEX = re.compile(
        rf'\Acontour( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})((?: (?:{contour.ContourOption._REGEX.pattern}))+?)?\Z'
    )

    def __init__(
        self,
        cmin: types.Real,
        cmax: types.Real,
        cstep: types.Real,
        options: types.Tuple[contour.ContourOption] = None,
    ):
        """
        Initializes ``Contour``.

        Parameters:
            cmin: Contour lower limit.
            cmax: Contour upper limit.
            cstep: Contour interval.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if cmin is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cmin)
        if cmax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cmax)
        if cstep is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cstep)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cmin,
                cmax,
                cstep,
                options,
            ]
        )

        self.cmin: typing.Final[types.Real] = cmin
        self.cmax: typing.Final[types.Real] = cmax
        self.cstep: typing.Final[types.Real] = cstep
        self.options: typing.Final[types.Tuple[contour.ContourOption]] = options


@dataclasses.dataclass
class ContourBuilder:
    """
    Builds ``Contour``.

    Attributes:
        cmin: Contour lower limit.
        cmax: Contour upper limit.
        cstep: Contour interval.
        options: Dictionary of options.
    """

    cmin: str | float | types.Real
    cmax: str | float | types.Real
    cstep: str | float | types.Real
    options: list[str] | list[contour.ContourOption] = None

    def build(self):
        """
        Builds ``ContourBuilder`` into ``Contour``.

        Returns:
            ``Contour`` for ``ContourBuilder``.
        """

        cmin = self.cmin
        if isinstance(self.cmin, types.Real):
            cmin = self.cmin
        elif isinstance(self.cmin, float) or isinstance(self.cmin, int):
            cmin = types.Real(self.cmin)
        elif isinstance(self.cmin, str):
            cmin = types.Real.from_mcnp(self.cmin)

        cmax = self.cmax
        if isinstance(self.cmax, types.Real):
            cmax = self.cmax
        elif isinstance(self.cmax, float) or isinstance(self.cmax, int):
            cmax = types.Real(self.cmax)
        elif isinstance(self.cmax, str):
            cmax = types.Real.from_mcnp(self.cmax)

        cstep = self.cstep
        if isinstance(self.cstep, types.Real):
            cstep = self.cstep
        elif isinstance(self.cstep, float) or isinstance(self.cstep, int):
            cstep = types.Real(self.cstep)
        elif isinstance(self.cstep, str):
            cstep = types.Real.from_mcnp(self.cstep)

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, contour.ContourOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(contour.ContourOption.from_mcnp(item))
                else:
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Contour(
            cmin=cmin,
            cmax=cmax,
            cstep=cstep,
            options=options,
        )
