import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Tf_1(DataOption):
    """
    Represents INP tf variation #1 elements.

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
        if2: Cell, surface, or detector bin number.
        id2: Total, flagged, or un-collided bin number.
        iu2: User bin number.
        is2: Segment bin number.
        im2: Multiplier bin number.
        ic2: Cosine bin number.
        ie2: Energy bin number.
        it2: Time bin number.
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
        'if2': types.Integer,
        'id2': types.Integer,
        'iu2': types.Integer,
        'is2': types.Integer,
        'im2': types.Integer,
        'ic2': types.Integer,
        'ie2': types.Integer,
        'it2': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Atf(\d+)( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z'
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
        if2: types.Integer = None,
        id2: types.Integer = None,
        iu2: types.Integer = None,
        is2: types.Integer = None,
        im2: types.Integer = None,
        ic2: types.Integer = None,
        ie2: types.Integer = None,
        it2: types.Integer = None,
    ):
        """
        Initializes ``Tf_1``.

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
            if2: Cell, surface, or detector bin number.
            id2: Total, flagged, or un-collided bin number.
            iu2: User bin number.
            is2: Segment bin number.
            im2: Multiplier bin number.
            ic2: Cosine bin number.
            ie2: Energy bin number.
            it2: Time bin number.

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
                if2,
                id2,
                iu2,
                is2,
                im2,
                ic2,
                ie2,
                it2,
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
        self.if2: typing.Final[types.Integer] = if2
        self.id2: typing.Final[types.Integer] = id2
        self.iu2: typing.Final[types.Integer] = iu2
        self.is2: typing.Final[types.Integer] = is2
        self.im2: typing.Final[types.Integer] = im2
        self.ic2: typing.Final[types.Integer] = ic2
        self.ie2: typing.Final[types.Integer] = ie2
        self.it2: typing.Final[types.Integer] = it2


@dataclasses.dataclass
class TfBuilder_1:
    """
    Builds ``Tf_1``.

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
        if2: Cell, surface, or detector bin number.
        id2: Total, flagged, or un-collided bin number.
        iu2: User bin number.
        is2: Segment bin number.
        im2: Multiplier bin number.
        ic2: Cosine bin number.
        ie2: Energy bin number.
        it2: Time bin number.
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
    if2: str | int | types.Integer = None
    id2: str | int | types.Integer = None
    iu2: str | int | types.Integer = None
    is2: str | int | types.Integer = None
    im2: str | int | types.Integer = None
    ic2: str | int | types.Integer = None
    ie2: str | int | types.Integer = None
    it2: str | int | types.Integer = None

    def build(self):
        """
        Builds ``TfBuilder_1`` into ``Tf_1``.

        Returns:
            ``Tf_1`` for ``TfBuilder_1``.
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

        if2 = self.if2
        if isinstance(self.if2, types.Integer):
            if2 = self.if2
        elif isinstance(self.if2, int):
            if2 = types.Integer(self.if2)
        elif isinstance(self.if2, str):
            if2 = types.Integer.from_mcnp(self.if2)

        id2 = self.id2
        if isinstance(self.id2, types.Integer):
            id2 = self.id2
        elif isinstance(self.id2, int):
            id2 = types.Integer(self.id2)
        elif isinstance(self.id2, str):
            id2 = types.Integer.from_mcnp(self.id2)

        iu2 = self.iu2
        if isinstance(self.iu2, types.Integer):
            iu2 = self.iu2
        elif isinstance(self.iu2, int):
            iu2 = types.Integer(self.iu2)
        elif isinstance(self.iu2, str):
            iu2 = types.Integer.from_mcnp(self.iu2)

        is2 = self.is2
        if isinstance(self.is2, types.Integer):
            is2 = self.is2
        elif isinstance(self.is2, int):
            is2 = types.Integer(self.is2)
        elif isinstance(self.is2, str):
            is2 = types.Integer.from_mcnp(self.is2)

        im2 = self.im2
        if isinstance(self.im2, types.Integer):
            im2 = self.im2
        elif isinstance(self.im2, int):
            im2 = types.Integer(self.im2)
        elif isinstance(self.im2, str):
            im2 = types.Integer.from_mcnp(self.im2)

        ic2 = self.ic2
        if isinstance(self.ic2, types.Integer):
            ic2 = self.ic2
        elif isinstance(self.ic2, int):
            ic2 = types.Integer(self.ic2)
        elif isinstance(self.ic2, str):
            ic2 = types.Integer.from_mcnp(self.ic2)

        ie2 = self.ie2
        if isinstance(self.ie2, types.Integer):
            ie2 = self.ie2
        elif isinstance(self.ie2, int):
            ie2 = types.Integer(self.ie2)
        elif isinstance(self.ie2, str):
            ie2 = types.Integer.from_mcnp(self.ie2)

        it2 = self.it2
        if isinstance(self.it2, types.Integer):
            it2 = self.it2
        elif isinstance(self.it2, int):
            it2 = types.Integer(self.it2)
        elif isinstance(self.it2, str):
            it2 = types.Integer.from_mcnp(self.it2)

        return Tf_1(
            suffix=suffix,
            if1=if1,
            id1=id1,
            iu1=iu1,
            is1=is1,
            im1=im1,
            ic1=ic1,
            ie1=ie1,
            it1=it1,
            if2=if2,
            id2=id2,
            iu2=iu2,
            is2=is2,
            im2=im2,
            ic2=ic2,
            ie2=ie2,
            it2=it2,
        )

    @staticmethod
    def unbuild(ast: Tf_1):
        """
        Unbuilds ``Tf_1`` into ``TfBuilder_1``

        Returns:
            ``TfBuilder_1`` for ``Tf_1``.
        """

        return Tf_1(
            suffix=copy.deepcopy(ast.suffix),
            if1=copy.deepcopy(ast.if1),
            id1=copy.deepcopy(ast.id1),
            iu1=copy.deepcopy(ast.iu1),
            is1=copy.deepcopy(ast.is1),
            im1=copy.deepcopy(ast.im1),
            ic1=copy.deepcopy(ast.ic1),
            ie1=copy.deepcopy(ast.ie1),
            it1=copy.deepcopy(ast.it1),
            if2=copy.deepcopy(ast.if2),
            id2=copy.deepcopy(ast.id2),
            iu2=copy.deepcopy(ast.iu2),
            is2=copy.deepcopy(ast.is2),
            im2=copy.deepcopy(ast.im2),
            ic2=copy.deepcopy(ast.ic2),
            ie2=copy.deepcopy(ast.ie2),
            it2=copy.deepcopy(ast.it2),
        )
