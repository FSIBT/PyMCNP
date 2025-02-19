from __future__ import annotations
import re
import typing

from ..utils import types
from ..utils import errors
from ..utils import _parser
from ..utils import _object


class Header(_object.McnpElement_):
    """
    Represents PTRAC header blocks.

    Attributes:
        code: Simulation name.
        code_date: Simulation compilation date.
        version: Simulation version.
        run_date: Simulation run date.
        run_time: Simulation run time.
        title: Simulation title.
        settings: PTRAC input format.
        numbers: PTRAC event variable counts by type.
        ids: PTRAC event variable identifiers by type.
    """

    _REGEX = re.compile(
        r'   -1\n(.{8})(.{25})(.{8})(.{19})\n(.{80})\n((?:\s).{12}.{12}.{12}.{12}.{12}.{12}.{12}.{12}.{12}.{12}(?:\n))+((?:\s).{5}.{5}.{5}.{5}.{5}.{5}.{5}.{5}.{5}.{5}.{5}.{5}.{5}.{5}.{5}.{5}.{5}.{5}.{5}.{5}(?:\n))((?:\s)(.{4})+(?:\n))+([\S\s]+)'
    )

    def __init__(
        self,
        code: types.String,
        code_date: types.String,
        version: types.String,
        run_date: types.String,
        run_time: types.String,
        title: types.String,
        v_line: tuple[types.Real],
        n_line: tuple[types.Integer],
        l_line: tuple[types.Integer],
    ):
        """
        Initializes ``Header``.

        Parameters:
            code: Simulation name.
            code_date: Simulation compilation date.
            version: Simulation version.
            run_date: Simulation run date.
            run_time: Simulation run time.
            title: Simulation title.
            v_line: PTRAC v-line.
            n_line: PTRAC n-line.
            l_line: PTRAC l-line.

        Raises:
            PtracError: SEMANTICS_BLOCK_VALUE.
        """

        if code is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK_VALUE, code)

        if code_date is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK_VALUE, code_date)

        if version is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK_VALUE, version)

        if run_date is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK_VALUE, run_date)

        if run_time is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK_VALUE, run_time)

        if title is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK_VALUE, title)

        if v_line is None or None in v_line:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK_VALUE, v_line)

        if n_line is None or None in n_line:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK_VALUE, n_line)

        if l_line is None or None in l_line:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK_VALUE, l_line)

        self.code: typing.Final[types.String] = code
        self.code_date: typing.Final[types.String] = code_date
        self.version: typing.Final[types.String] = version
        self.run_date: typing.Final[types.String] = run_date
        self.run_time: typing.Final[types.String] = run_time
        self.title: typing.Final[types.String] = title
        self.v_line: typing.Final[tuple[types.Real]] = v_line
        self.n_line: typing.Final[tuple[types.Integer]] = n_line
        self.l_line: typing.Final[tuple[types.Integer]] = l_line

    @staticmethod
    def from_mcnp(source: str) -> tuple[Header, str]:
        """
        Generates ``Header`` from PTRAC.

        Parameters:
            source: PTRAC for ``Header``.

        Returns:
            ``Header``.

        Raises:
            PtracError: SYNTAX_HEADER.
        """

        source = _parser.preprocess_ptrac(source)
        tokens = Header._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_HEADER, source)

        code = types.String.from_mcnp(tokens[1])
        version = types.String.from_mcnp(tokens[2])
        code_date = types.String.from_mcnp(tokens[3])
        run_date = types.String.from_mcnp(tokens[4])
        run_time = types.String.from_mcnp(tokens[5])
        title = types.String.from_mcnp(tokens[6])
        v_line = types._Tuple(
            types.Real.from_mcnp(token) for token in re.split(r'\s+', tokens[7].strip())
        )
        n_line = types._Tuple(
            types.Integer.from_mcnp(token) for token in re.split(r'\s+', tokens[8].strip())
        )
        l_line = types._Tuple(
            types.Integer.from_mcnp(token) for token in re.split(r'\s+', tokens[9].strip())
        )

        return (
            Header(code, code_date, version, run_date, run_time, title, v_line, n_line, l_line),
            tokens[10],
        )

    def to_mcnp(self):
        """
        Generates PTRAC from ``Header``.

        Returns:
            INP for ``Header``.
        """

        assert False, "I'm working on it!"
