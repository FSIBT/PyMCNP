# noqa: E741

import re
import typing

from . import header
from .. import types
from .. import errors
from .. import _symbol


class Header(_symbol.Nonterminal):
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

    def __init__(
        self,
        code: types.String,
        version: types.String,
        code_date: types.String,
        run_datetime: types.String,
        title: types.String,
        v_line: header.V,
        n_line: header.N,
        l_line: header.L,
    ):
        """
        Initializes `Header`.

        Parameters:
            code: Simulation name.
            version: Simulation version.
            code_date: Simulation compilation date.
            run_datetime: Simulation run datetime.
            title: Simulation title.
            v_line: PTRAC v-line.
            n_line: PTRAC n-line.
            l_line: PTRAC l-line.

        Raises:
            PtracError: SEMANTICS_BLOCK.
        """

        if code is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK, code)

        if version is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK, version)

        if code_date is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK, code_date)

        if run_datetime is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK, run_datetime)

        if title is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK, title)

        if v_line is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK, v_line)

        if n_line is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK, n_line)

        if l_line is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK, l_line)

        self.code: typing.Final[types.String] = code
        self.version: typing.Final[types.String] = version
        self.code_date: typing.Final[types.String] = code_date
        self.run_datetime: typing.Final[types.String] = run_datetime
        self.title: typing.Final[types.String] = title
        self.v_line: typing.Final[header.V] = v_line
        self.n_line: typing.Final[header.N] = n_line
        self.l_line: typing.Final[header.L] = l_line

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
