import re
import typing

from . import _block
from .. import types
from .. import errors


class Mcnp(_block.Block):
    """
    Represents OUTP `1mcnp` tables.

    Attributes:
        version: Simulation version.
        code_date: Simulation compilation date.
        run_date: Simulation run date.
        run_time: Simulation run time.
        probid: Simulation problem ID.
        command: Simulation command.
        random_generator: Simulation random number generator.
        random_seed: Simulation random number seed.
        random_multiplier: Simulation random number multiplier.
        random_adder: Simulation random number adder.
        random_bits: Simulation random number bits.
        random_stride: Simulation random number stride.
        lines: Input lines.
        messages: Input messages.
    """

    _REGEX = re.compile(
        r'\A1mcnp     (.{14})(.{32})(.{9})(.{9})\n'
        r' \*{73}                 (.{28})\n'
        r' (.+)\n\n'
        r' \n'
        r'((?:.*\n)*)\n'
        r' \*{51}\n'
        r' \* Random Number Generator  = (.{20}) \*\n'
        r' \* Random Number Seed       = (.{20}) \*\n'
        r' \* Random Number Multiplier = (.{20}) \*\n'
        r' \* Random Number Adder      = (.{20}) \*\n'
        r' \* Random Number Bits Used  = (.{20}) \*\n'
        r' \* Random Number Stride     = (.{20}) \*\n'
        r' \*{51}\n'
        r'((?:.*\n)*)\Z'
    )

    def __init__(
        self,
        version: types.String,
        code_date: types.String,
        run_date: types.String,
        run_time: types.String,
        probid: types.String,
        command: types.String,
        lines: types.String,
        random_generator: types.String,
        random_seed: types.String,
        random_multiplier: types.String,
        random_adder: types.String,
        random_bits: types.String,
        random_stride: types.String,
        messages: types.String,
    ):
        """
        Initializes `Mcnp`.

        Parameters:
            version: Simulation version.
            code_date: Simulation compilation date.
            run_date: Simulation run date.
            run_time: Simulation run time.
            probid: Simulation problem ID.
            command: Simulation command.
            lines: Input lines.
            random_generator: Simulation random number generator.
            random_seed: Simulation random number seed.
            random_multiplier: Simulation random number multiplier.
            random_adder: Simulation random number adder.
            random_bits: Simulation random number bits.
            random_stride: Simulation random number stride.
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

        if random_generator is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, random_generator)

        if random_seed is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, random_seed)

        if random_multiplier is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, random_multiplier)

        if random_adder is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, random_adder)

        if random_bits is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, random_bits)

        if random_stride is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, random_stride)

        if lines is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, lines)

        if messages is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, messages)

        self.version: typing.Final[types.String] = version
        self.code_date: typing.Final[types.String] = code_date
        self.run_date: typing.Final[types.String] = run_date
        self.run_time: typing.Final[types.String] = run_time
        self.probid: typing.Final[types.String] = probid
        self.command: typing.Final[types.String] = command
        self.lines: typing.Final[types.String] = lines
        self.random_generator: typing.Final[types.String] = random_generator
        self.random_seed: typing.Final[types.String] = random_seed
        self.random_multiplier: typing.Final[types.String] = random_multiplier
        self.random_adder: typing.Final[types.String] = random_adder
        self.random_bits: typing.Final[types.String] = random_bits
        self.random_stride: typing.Final[types.String] = random_stride
        self.messages: typing.Final[types.String] = messages

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Mcnp` from OUTP.

        Parameters:
            source: OUTP for `Mcnp`.

        Returns:
            `Mcnp`.

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
        command = types.String.from_mcnp(tokens[6])
        lines = types.String.from_mcnp(tokens[7])
        random_generator = types.String.from_mcnp(tokens[8])
        random_seed = types.String.from_mcnp(tokens[9])
        random_multiplier = types.String.from_mcnp(tokens[10])
        random_adder = types.String.from_mcnp(tokens[11])
        random_bits = types.String.from_mcnp(tokens[12])
        random_stride = types.String.from_mcnp(tokens[13])
        messages = types.String.from_mcnp(tokens[14])

        return Mcnp(
            version,
            code_date,
            run_date,
            run_time,
            probid,
            command,
            lines,
            random_generator,
            random_seed,
            random_multiplier,
            random_adder,
            random_bits,
            random_stride,
            messages,
        )

    def to_mcnp(self):
        """
        Generates OUTP from `Mcnp`.

        Returns:
            OUTP for `Mcnp`.
        """

        return f"""
1mcnp     {self.version}{self.code_date}{self.run_date}{self.run_time}
 *************************************************************************                 {self.probid}
 {self.command}

 
{self.lines}
 ***************************************************
 * Random Number Generator  = {self.random_generator} *
 * Random Number Seed       = {self.random_seed} *
 * Random Number Multiplier = {self.random_multiplier} *
 * Random Number Adder      = {self.random_adder} *
 * Random Number Bits Used  = {self.random_bits} *
 * Random Number Stride     = {self.random_stride} *
 ***************************************************
{self.messages}
"""[1:-1]
