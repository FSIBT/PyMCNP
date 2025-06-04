# noqa: E741

import re
import typing

from ..utils import types
from ..utils import errors
from ..utils import _object


class Header(_object.McnpNonterminal):
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

    _REGEX = re.compile(
        r'\A   -1\n'
        r'(.{8})(.{25})(.{9})(.{18})\n'
        r'(.{80})\n'
        r'((?:\s.{120}\n)+)'
        r'\s(.{100})\n'
        r'((?:\s(?:.{4})+\n)+)\Z'
    )

    def __init__(
        self,
        code: types.String,
        version: types.String,
        code_date: types.String,
        run_datetime: types.String,
        title: types.String,
        v_line: types.Tuple[types.Real],
        n_line: types.Tuple[types.Integer],
        l_line: types.Tuple[types.Integer],
    ):
        """
        Initializes ``Header``.

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

        if v_line is None or None in v_line:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK, v_line)

        if n_line is None or None in n_line:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK, n_line)

        if l_line is None or None in l_line:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK, l_line)

        self.code: typing.Final[types.String] = code
        self.version: typing.Final[types.String] = version
        self.code_date: typing.Final[types.String] = code_date
        self.run_datetime: typing.Final[types.String] = run_datetime
        self.title: typing.Final[types.String] = title
        self.v_line: typing.Final[types.Tuple[types.Real]] = v_line
        self.n_line: typing.Final[types.Tuple[types.Integer]] = n_line
        self.l_line: typing.Final[types.Tuple[types.Integer]] = l_line

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Header`` from PTRAC.

        Parameters:
            source: PTRAC for ``Header``.

        Returns:
            ``Header``.

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
        v_line = types.Tuple(
            [types.Real.from_mcnp(v) for v in re.split(r'\s+|\n', tokens[6].strip())]
        )
        n_line = types.Tuple(
            [types.Integer.from_mcnp(n) for n in re.split(r'\s+|\n', tokens[7].strip())]
        )
        l_line = types.Tuple(
            [types.Integer.from_mcnp(l) for l in re.split(r'\s+|\n', tokens[8].strip())]
        )

        return Header(code, version, code_date, run_datetime, title, v_line, n_line, l_line)

    def to_mcnp(self):
        """
        Generates PTRAC from ``Header``.

        Returns:
            PTRAC for ``Header``.
        """

        v_line = ' '
        for i, v in enumerate(self.v_line):
            v_line += f'{v:>12.4E}'

            if (i + 1) % 10 == 0 and i != 0:
                v_line += '\n '
        v_line = v_line[:-1]

        n_line = ' '
        for i, n in enumerate(self.n_line):
            n_line += f'{n:>5}'

        l_line = ' '
        for i, l in enumerate(self.l_line):
            l_line += f'{l:>4}'

            if (i + 1) % 30 == 0 and i != 0:
                l_line += '\n '

        return f'   -1\n{self.code:<8}{self.version:<25}{self.code_date:<9}{self.run_datetime:<18}\n{self.title:<80}\n{v_line}{n_line}\n{l_line}\n'
