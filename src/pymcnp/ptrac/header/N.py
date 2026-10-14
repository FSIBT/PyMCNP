import re

from . import _line
from ... import types
from ... import errors
from ... import _fields


class N(_fields.Fields, _line.HeaderLine):
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

    _ERROR = errors.PtracError
    _CODE = errors.PtracCode.SEMANTICS_LINE

    n1 = _fields.Field(types.Integer, 'Number of variables on the I line')
    n2 = _fields.Field(types.Integer, 'Number of variables on 1st event line for an "src" event')
    n3 = _fields.Field(types.Integer, 'Number of variables on 2nd event line for an "src" event')
    n4 = _fields.Field(types.Integer, 'Number of variables on 1st event line for a "bnk" event')
    n5 = _fields.Field(types.Integer, 'Number of variables on 2nd event line for a "bnk" event')
    n6 = _fields.Field(types.Integer, 'Number of variables on 1st event line for a "sur" event')
    n7 = _fields.Field(types.Integer, 'Number of variables on 2nd event line for a "sur" event')
    n8 = _fields.Field(types.Integer, 'Number of variables on 1st event line for a "col" event')
    n9 = _fields.Field(types.Integer, 'Number of variables on 2nd event line for a "col" event')
    n10 = _fields.Field(types.Integer, 'Number of variables on 1st event line for a "ter" event')
    n11 = _fields.Field(types.Integer, 'Number of variables on 2nd event line for a "ter" event')
    n12 = _fields.Field(types.Integer, 'IPT for single particle transport, otherwise 0')
    n13 = _fields.Field(types.Integer, '4/8 for real * 4/8 output')
    n14 = _fields.Field(types.Integer, 'not used')
    n15 = _fields.Field(types.Integer, 'not used')
    n16 = _fields.Field(types.Integer, 'not used')
    n17 = _fields.Field(types.Integer, 'not used')
    n18 = _fields.Field(types.Integer, 'not used')
    n19 = _fields.Field(types.Integer, 'not used')
    n20 = _fields.Field(types.Integer, 'not used')

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
