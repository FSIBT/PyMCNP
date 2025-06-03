import re
import typing

from . import _block
from ..utils import types
from ..utils import errors


class Footer(_block.Block):
    """
    Represents OUTP header tables.

    Attributes:
        file: RUNTPE filename.
        args: Nps, coll, cmt, nrn values.
        warnings: Number of warnings so far.
        nps: Particle histories done.
        time: Computer time.
        code: Simulation name.
        version: Simulation version.
        code_date: Simulation compilation date.
        run_date: Simulation run date.
        run_time: Simulation run time.
        probid: Simulation problem ID.
    """

    _REGEX = re.compile(
        r'\A \*{119}\n'
        r'\n'
        r' dump no.    2 on file (.+?) ([\s\S]+?)\n'
        r'\n'
        r' (.{9}) warning messages so far[.]\n'
        r'\n'
        r'\n'
        r' run terminated when (.{12}) particle histories were done[.]\n'
        r'\n'
        r' computer time = (.{7}) minutes\n'
        r'\n'
        r' (.{9})(.{14})(.{29})(.{9})(.{29})(.{28})\n\Z'
    )

    def __init__(
        self,
        file: types.String,
        args: types.String,
        warnings: types.String,
        nps: types.String,
        time: types.String,
        code: types.String,
        version: types.String,
        code_date: types.String,
        run_date: types.String,
        run_time: types.String,
        probid: types.String,
    ):
        """
        Initializes ``Footer``.

        Parameters:
            file: RUNTPE filename.
            args: Nps, coll, cmt, nrn values.
            warnings: Number of warnings so far.
            nps: Particle histories done.
            time: Computer time.
            code: Simulation name.
            version: Simulation version.
            code_date: Simulation compilation date.
            run_date: Simulation run date.
            run_time: Simulation run time.
            probid: Simulation problem ID.

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if file is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, file)

        if args is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, args)

        if warnings is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, warnings)

        if nps is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps)

        if time is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, time)

        if code is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, code)

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

        self.file: typing.Final[types.String] = file
        self.args: typing.Final[types.String] = args
        self.warnings: typing.Final[types.String] = warnings
        self.nps: typing.Final[types.String] = nps
        self.time: typing.Final[types.String] = time
        self.code: typing.Final[types.String] = code
        self.version: typing.Final[types.String] = version
        self.code_date: typing.Final[types.String] = code_date
        self.run_date: typing.Final[types.String] = run_date
        self.run_time: typing.Final[types.String] = run_time
        self.probid: typing.Final[types.String] = probid

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Footer`` from OUTP.

        Parameters:
            source: OUTP for ``Footer``.

        Returns:
            ``Footer``.

        Raises:
            OutpError: SYNTAX_TABLE.
        """

        tokens = Footer._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        file = types.String.from_mcnp(tokens[1])
        args = types.String.from_mcnp(tokens[2])
        warnings = types.String.from_mcnp(tokens[3])
        nps = types.String.from_mcnp(tokens[4])
        time = types.String.from_mcnp(tokens[5])
        code = types.String.from_mcnp(tokens[6])
        version = types.String.from_mcnp(tokens[7])
        code_date = types.String.from_mcnp(tokens[8])
        run_date = types.String.from_mcnp(tokens[9])
        run_time = types.String.from_mcnp(tokens[10])
        probid = types.String.from_mcnp(tokens[11])

        return Footer(
            file,
            args,
            warnings,
            nps,
            time,
            code,
            version,
            code_date,
            run_date,
            run_time,
            probid,
        )

    def to_mcnp(self):
        """
        Generates OUTP from ``Footer``.

        Returns:
            OUTP for ``Footer``.
        """

        return f"""
 ***********************************************************************************************************************

 dump no.    2 on file {self.file} {self.args}

 {self.warnings} warning messages so far.


 run terminated when {self.nps} particle histories were done.

 computer time = {self.time} minutes

 {self.code}{self.version}{self.code_date}{self.run_date}{self.run_time}{self.probid}
"""
