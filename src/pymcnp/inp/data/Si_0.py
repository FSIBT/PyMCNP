import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Si_0(DataOption_, keyword='si'):
    """
    Represents INP si_0 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'option': types.String,
        'information': types.Tuple[types.DistributionNumber],
    }

    _REGEX = re.compile(
        rf'\Asi(\d+)( {types.String._REGEX.pattern})((?: {types.DistributionNumber._REGEX.pattern})+?)\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        option: types.String,
        information: types.Tuple[types.DistributionNumber],
    ):
        """
        Initializes ``Si_0``.

        Parameters:
            suffix: Data card option suffix.
            option: Information kind setting.
            information: Particle source information.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if option is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, option)
        if information is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, information)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                option,
                information,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.option: typing.Final[types.String] = option
        self.information: typing.Final[types.Tuple[types.DistributionNumber]] = information
