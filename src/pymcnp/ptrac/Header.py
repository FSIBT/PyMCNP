# noqa: E741

import re

from . import header
from .. import types
from .. import errors
from .. import _symbol
from .. import _fields


class Header(_fields.Fields, _symbol.Nonterminal):
    """
    Represents PTRAC header blocks.

    Attributes:
        code: Simulation name.
        version: Simulation version.
        code_date: Simulation compilation date.
        run_datetime: Simulation run datetime.
        title: Simulation title.
        settings: PTRAC input format.
        numbers: PTRAC event variable counts by type.
        ids: PTRAC event variable identifiers by type.
    """

    _REGEX = re.compile(r'\A   -1\n' r'(.{8})(.{25})(.{9})(.{18})\n' r'(.{80})\n((?:\s.{120}\n)+)(\s.{100}\n)((?:\s(?:.{4})+\n)+)\Z', re.IGNORECASE)

    _ERROR = errors.PtracError
    _CODE = errors.PtracCode.SEMANTICS_BLOCK

    code = _fields.Field(types.String, 'Simulation name')
    version = _fields.Field(types.String, 'Simulation version')
    code_date = _fields.Field(types.String, 'Simulation compilation date')
    run_datetime = _fields.Field(types.String, 'Simulation run datetime')
    title = _fields.Field(types.String, 'Simulation title')
    v_line = _fields.Field(header.V, 'PTRAC v-line')
    n_line = _fields.Field(header.N, 'PTRAC n-line')
    l_line = _fields.Field(header.L, 'PTRAC l-line')

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Header` from PTRAC.

        Parameters:
            source: PTRAC for `Header`.

        Returns:
            `Header`.

        Raises:
            PtracError: SYNTAX_BLOCK.
        """

        tokens = Header._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_BLOCK, source)

        code = types.String.from_mcnp(tokens[1])
        version = types.String.from_mcnp(tokens[2])
        code_date = types.String.from_mcnp(tokens[3])
        run_datetime = types.String.from_mcnp(tokens[4])
        title = types.String.from_mcnp(tokens[5])
        v_line = header.V.from_mcnp(tokens[6])
        n_line = header.N.from_mcnp(tokens[7])
        l_line = header.L.from_mcnp(tokens[8])

        return Header(code, version, code_date, run_datetime, title, v_line, n_line, l_line)

    def to_mcnp(self):
        """
        Generates PTRAC from `Header`.

        Returns:
            PTRAC for `Header`.
        """

        return f'   -1\n{self.code:<8}{self.version:<25}{self.code_date:<9}{self.run_datetime:<18}\n{self.title:<80}\n{self.v_line}{self.n_line}{self.l_line}'
