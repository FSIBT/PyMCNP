import re
import typing

from . import _line
from ... import types
from ... import errors


class N(_line.HeaderLine):
    """
    Represents PTRAC header block n lines.

    Attributes:
        n1: Number of variables on the I line.
        n2: Number of variables on 1st event line for an "src" event.
        n3: Number of variables on 2nd event line for an "src" event.
        n4: Number of variables on 1st event line for a "bnk" event.
        n5: Number of variables on 2nd event line for a "bnk" event.
        n6: Number of variables on 1st event line for a "sur" event.
        n7: Number of variables on 2nd event line for a "sur" event.
        n8: Number of variables on 1st event line for a "col" event.
        n9: Number of variables on 2nd event line for a "col" event.
        n10: Number of variables on 1st event line for a "ter" event.
        n11: Number of variables on 2nd event line for a "ter" event.
        n12: IPT for single particle transport, otherwise 0.
        n13: 4/8 for real * 4/8 output.
        n14: not used.
        n15: not used.
        n16: not used.
        n17: not used.
        n18: not used.
        n19: not used.
        n20: not used.
    """

    _REGEX = re.compile(r'\A\s(.{5})(.{5})(.{5})(.{5})(.{5})(.{5})(.{5})(.{5})(.{5})(.{5})(.{5})(.{5})(.{5})(.{5})(.{5})(.{5})(.{5})(.{5})(.{5})(.{5})\n\Z', re.IGNORECASE)

    def __init__(
        self,
        n1: types.Integer,
        n2: types.Integer,
        n3: types.Integer,
        n4: types.Integer,
        n5: types.Integer,
        n6: types.Integer,
        n7: types.Integer,
        n8: types.Integer,
        n9: types.Integer,
        n10: types.Integer,
        n11: types.Integer,
        n12: types.Integer,
        n13: types.Integer,
        n14: types.Integer,
        n15: types.Integer,
        n16: types.Integer,
        n17: types.Integer,
        n18: types.Integer,
        n19: types.Integer,
        n20: types.Integer,
    ):
        """
        Initializes `N`.

        Parameters:
            n1: Number of variables on the I line.
            n2: Number of variables on 1st event line for an "src" event.
            n3: Number of variables on 2nd event line for an "src" event.
            n4: Number of variables on 1st event line for a "bnk" event.
            n5: Number of variables on 2nd event line for a "bnk" event.
            n6: Number of variables on 1st event line for a "sur" event.
            n7: Number of variables on 2nd event line for a "sur" event.
            n8: Number of variables on 1st event line for a "col" event.
            n9: Number of variables on 2nd event line for a "col" event.
            n10: Number of variables on 1st event line for a "ter" event.
            n11: Number of variables on 2nd event line for a "ter" event.
            n12: IPT for single particle transport, otherwise 0.
            n13: 4/8 for real * 4/8 output.
            n14: not used.
            n15: not used.
            n16: not used.
            n17: not used.
            n18: not used.
            n19: not used.
            n20: not used.

        Raises:
            PtracError: SEMANTICS_LINE.
        """

        if n1 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n1)

        if n2 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n2)

        if n3 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n3)

        if n4 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n4)

        if n5 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n5)

        if n6 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n6)

        if n7 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n7)

        if n8 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n8)

        if n9 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n9)

        if n10 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n10)

        if n11 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n11)

        if n12 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n12)

        if n13 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n13)

        if n14 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n14)

        if n15 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n15)

        if n16 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n16)

        if n17 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n17)

        if n18 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n18)

        if n19 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n19)

        if n20 is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, n20)

        self.n1: typing.Final[types.Integer] = n1
        self.n2: typing.Final[types.Integer] = n2
        self.n3: typing.Final[types.Integer] = n3
        self.n4: typing.Final[types.Integer] = n4
        self.n5: typing.Final[types.Integer] = n5
        self.n6: typing.Final[types.Integer] = n6
        self.n7: typing.Final[types.Integer] = n7
        self.n8: typing.Final[types.Integer] = n8
        self.n9: typing.Final[types.Integer] = n9
        self.n10: typing.Final[types.Integer] = n10
        self.n11: typing.Final[types.Integer] = n11
        self.n12: typing.Final[types.Integer] = n12
        self.n13: typing.Final[types.Integer] = n13
        self.n14: typing.Final[types.Integer] = n14
        self.n15: typing.Final[types.Integer] = n15
        self.n16: typing.Final[types.Integer] = n16
        self.n17: typing.Final[types.Integer] = n17
        self.n18: typing.Final[types.Integer] = n18
        self.n19: typing.Final[types.Integer] = n19
        self.n20: typing.Final[types.Integer] = n20

    def from_mcnp(source: str):
        """
        Generates `N` from PTRAC.

        Parameters:
            source: PTRAC for `N`.

        Returns:
            `N`.

        Raises:
            PtracError: SYNTAX_LINE.
        """

        tokens = N._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_LINE, source)

        n1 = types.Integer.from_mcnp(tokens[1])
        n2 = types.Integer.from_mcnp(tokens[2])
        n3 = types.Integer.from_mcnp(tokens[3])
        n4 = types.Integer.from_mcnp(tokens[4])
        n5 = types.Integer.from_mcnp(tokens[5])
        n6 = types.Integer.from_mcnp(tokens[6])
        n7 = types.Integer.from_mcnp(tokens[7])
        n8 = types.Integer.from_mcnp(tokens[8])
        n9 = types.Integer.from_mcnp(tokens[9])
        n10 = types.Integer.from_mcnp(tokens[10])
        n11 = types.Integer.from_mcnp(tokens[11])
        n12 = types.Integer.from_mcnp(tokens[12])
        n13 = types.Integer.from_mcnp(tokens[13])
        n14 = types.Integer.from_mcnp(tokens[14])
        n15 = types.Integer.from_mcnp(tokens[15])
        n16 = types.Integer.from_mcnp(tokens[16])
        n17 = types.Integer.from_mcnp(tokens[17])
        n18 = types.Integer.from_mcnp(tokens[18])
        n19 = types.Integer.from_mcnp(tokens[19])
        n20 = types.Integer.from_mcnp(tokens[20])

        return N(
            n1,
            n2,
            n3,
            n4,
            n5,
            n6,
            n7,
            n8,
            n9,
            n10,
            n11,
            n12,
            n13,
            n14,
            n15,
            n16,
            n17,
            n18,
            n19,
            n20,
        )

    def to_mcnp(self):
        """
        Generates PTRAC from `N`.

        Returns:
            PTRAC for `N`.
        """

        n_line = ' '
        for n in [
            self.n1,
            self.n2,
            self.n3,
            self.n4,
            self.n5,
            self.n6,
            self.n7,
            self.n8,
            self.n9,
            self.n10,
            self.n11,
            self.n12,
            self.n13,
            self.n14,
            self.n15,
            self.n16,
            self.n17,
            self.n18,
            self.n19,
            self.n20,
        ]:
            n_line += f'{str(n):>5}'

        return n_line + '\n'
