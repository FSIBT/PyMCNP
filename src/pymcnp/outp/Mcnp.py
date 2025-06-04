import re
import typing

from . import _block
from ..utils import types
from ..utils import errors


class Mcnp(_block.Block):
    """
    Represents OUTP ``1mcnp`` tables.

    Attributes:
        version: Simulation version.
        code_date: Simulation compilation date.
        run_date: Simulation run date.
        run_time: Simulation run time.
        probid: Simulation problem ID.
        command: Simulation command.
        lines: Input lines.
        messages: Input messages.
    """

    _REGEX = re.compile(
        r'\A1mcnp     (.{14})(.{32})(.{9})(.{9})\n'
        r' \*{73}                 (.{28})\n'
        r'(.+)\n \n'
        r'((?:  [0-9 ]{8}-       .{80}\n)|(?:  warning[.]  .+\n)|(?:  comment[.]  .+\n))+((?:(?: \n)(?:(?:  warning[.]  .+\n)|(?:  comment[.]  .+\n)|(?:  fatal error[.]  .+\n))+)+)?\Z'
    )

    def __init__(
        self,
        version: types.String,
        code_date: types.String,
        run_date: types.String,
        run_time: types.String,
        probid: types.String,
        command: types.String,
        lines: types.Tuple[types.String],
        messages: types.Tuple[types.String],
    ):
        """
        Initializes ``Mcnp``.

        Parameters:
            version: Simulation version.
            code_date: Simulation compilation date.
            run_date: Simulation run date.
            run_time: Simulation run time.
            probid: Simulation problem ID.
            command: Simulation command.
            lines: Input lines.
            messages: Input messages.

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if version is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, version)

        if code_date is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, code_date)

        if run_date is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, run_date)

        if run_time is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, run_time)

        if probid is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, probid)

        if command is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, command)

        if lines is None or None in lines:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, lines)

        if messages is None or None in messages:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, messages)

        self.version: typing.Final[types.String] = version
        self.code_date: typing.Final[types.String] = code_date
        self.run_date: typing.Final[types.String] = run_date
        self.run_time: typing.Final[types.String] = run_time
        self.probid: typing.Final[types.String] = probid
        self.command: typing.Final[types.Tuple[types.String]] = command
        self.lines: typing.Final[types.Tuple[types.String]] = lines
        self.messages: typing.Final[types.Tuple[types.String]] = messages

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Mcnp`` from OUTP.

        Parameters:
            source: OUTP for ``Mcnp``.

        Returns:
            ``Mcnp``.

        Raises:
            OutpError: SYNTAX_TABLE.
        """

        tokens = Mcnp._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        version = types.String.from_mcnp(tokens[1])
        code_date = types.String.from_mcnp(tokens[2])
        run_date = types.String.from_mcnp(tokens[3])
        run_time = types.String.from_mcnp(tokens[4])
        probid = types.String.from_mcnp(tokens[5])
        command = types.String(tokens[6])
        lines = types.Tuple(types.String(line) for line in tokens[7].split('\n'))
        messages = types.Tuple(types.String(line) for line in tokens[8].split('\n'))

        return Mcnp(
            version,
            code_date,
            run_date,
            run_time,
            probid,
            command,
            lines,
            messages,
        )

    def to_mcnp(self):
        """
        Generates OUTP from ``Mcnp``.

        Returns:
            OUTP for ``Mcnp``.
        """

        lines = '\n'.join(self.lines)
        messages = '\n'.join(self.messages)

        return f"""
1mcnp     {self.version}{self.code_date}{self.run_date}{self.run_time}
 *************************************************************************                 {self.probid}
 {self.command}
{lines}
{messages}
"""[1:-1]
