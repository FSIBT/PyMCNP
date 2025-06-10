import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Tf_0(_option.DataOption):
    """
    Represents INP tf variation #0 elements.

    Attributes:
        suffix: Data card option suffix.
        if1: Cell, surface, or detector bin number.
        id1: Total, flagged, or un-collided bin number.
        iu1: User bin number.
        is1: Segment bin number.
        im1: Multiplier bin number.
        ic1: Cosine bin number.
        ie1: Energy bin number.
        it1: Time bin number.
    """

    _KEYWORD = 'tf'

    _ATTRS = {
        'suffix': types.Integer,
        'if1': types.Integer,
        'id1': types.Integer,
        'iu1': types.Integer,
        'is1': types.Integer,
        'im1': types.Integer,
        'ic1': types.Integer,
        'ie1': types.Integer,
        'it1': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Atf(\d+)( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        if1: types.Integer = None,
        id1: types.Integer = None,
        iu1: types.Integer = None,
        is1: types.Integer = None,
        im1: types.Integer = None,
        ic1: types.Integer = None,
        ie1: types.Integer = None,
        it1: types.Integer = None,
    ):
        """
        Initializes ``Tf_0``.

        Parameters:
            suffix: Data card option suffix.
            if1: Cell, surface, or detector bin number.
            id1: Total, flagged, or un-collided bin number.
            iu1: User bin number.
            is1: Segment bin number.
            im1: Multiplier bin number.
            ic1: Cosine bin number.
            ie1: Energy bin number.
            it1: Time bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                if1,
                id1,
                iu1,
                is1,
                im1,
                ic1,
                ie1,
                it1,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.if1: typing.Final[types.Integer] = if1
        self.id1: typing.Final[types.Integer] = id1
        self.iu1: typing.Final[types.Integer] = iu1
        self.is1: typing.Final[types.Integer] = is1
        self.im1: typing.Final[types.Integer] = im1
        self.ic1: typing.Final[types.Integer] = ic1
        self.ie1: typing.Final[types.Integer] = ie1
        self.it1: typing.Final[types.Integer] = it1


@dataclasses.dataclass
class TfBuilder_0(_option.DataOptionBuilder):
    """
    Builds ``Tf_0``.

    Attributes:
        suffix: Data card option suffix.
        if1: Cell, surface, or detector bin number.
        id1: Total, flagged, or un-collided bin number.
        iu1: User bin number.
        is1: Segment bin number.
        im1: Multiplier bin number.
        ic1: Cosine bin number.
        ie1: Energy bin number.
        it1: Time bin number.
    """

    suffix: str | int | types.Integer
    if1: str | int | types.Integer = None
    id1: str | int | types.Integer = None
    iu1: str | int | types.Integer = None
    is1: str | int | types.Integer = None
    im1: str | int | types.Integer = None
    ic1: str | int | types.Integer = None
    ie1: str | int | types.Integer = None
    it1: str | int | types.Integer = None

    def build(self):
        """
        Builds ``TfBuilder_0`` into ``Tf_0``.

        Returns:
            ``Tf_0`` for ``TfBuilder_0``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if1 = self.if1
        if isinstance(self.if1, types.Integer):
            if1 = self.if1
        elif isinstance(self.if1, int):
            if1 = types.Integer(self.if1)
        elif isinstance(self.if1, str):
            if1 = types.Integer.from_mcnp(self.if1)

        id1 = self.id1
        if isinstance(self.id1, types.Integer):
            id1 = self.id1
        elif isinstance(self.id1, int):
            id1 = types.Integer(self.id1)
        elif isinstance(self.id1, str):
            id1 = types.Integer.from_mcnp(self.id1)

        iu1 = self.iu1
        if isinstance(self.iu1, types.Integer):
            iu1 = self.iu1
        elif isinstance(self.iu1, int):
            iu1 = types.Integer(self.iu1)
        elif isinstance(self.iu1, str):
            iu1 = types.Integer.from_mcnp(self.iu1)

        is1 = self.is1
        if isinstance(self.is1, types.Integer):
            is1 = self.is1
        elif isinstance(self.is1, int):
            is1 = types.Integer(self.is1)
        elif isinstance(self.is1, str):
            is1 = types.Integer.from_mcnp(self.is1)

        im1 = self.im1
        if isinstance(self.im1, types.Integer):
            im1 = self.im1
        elif isinstance(self.im1, int):
            im1 = types.Integer(self.im1)
        elif isinstance(self.im1, str):
            im1 = types.Integer.from_mcnp(self.im1)

        ic1 = self.ic1
        if isinstance(self.ic1, types.Integer):
            ic1 = self.ic1
        elif isinstance(self.ic1, int):
            ic1 = types.Integer(self.ic1)
        elif isinstance(self.ic1, str):
            ic1 = types.Integer.from_mcnp(self.ic1)

        ie1 = self.ie1
        if isinstance(self.ie1, types.Integer):
            ie1 = self.ie1
        elif isinstance(self.ie1, int):
            ie1 = types.Integer(self.ie1)
        elif isinstance(self.ie1, str):
            ie1 = types.Integer.from_mcnp(self.ie1)

        it1 = self.it1
        if isinstance(self.it1, types.Integer):
            it1 = self.it1
        elif isinstance(self.it1, int):
            it1 = types.Integer(self.it1)
        elif isinstance(self.it1, str):
            it1 = types.Integer.from_mcnp(self.it1)

        return Tf_0(
            suffix=suffix,
            if1=if1,
            id1=id1,
            iu1=iu1,
            is1=is1,
            im1=im1,
            ic1=ic1,
            ie1=ie1,
            it1=it1,
        )

    @staticmethod
    def unbuild(ast: Tf_0):
        """
        Unbuilds ``Tf_0`` into ``TfBuilder_0``

        Returns:
            ``TfBuilder_0`` for ``Tf_0``.
        """

        return TfBuilder_0(
            suffix=copy.deepcopy(ast.suffix),
            if1=copy.deepcopy(ast.if1),
            id1=copy.deepcopy(ast.id1),
            iu1=copy.deepcopy(ast.iu1),
            is1=copy.deepcopy(ast.is1),
            im1=copy.deepcopy(ast.im1),
            ic1=copy.deepcopy(ast.ic1),
            ie1=copy.deepcopy(ast.ie1),
            it1=copy.deepcopy(ast.it1),
        )
