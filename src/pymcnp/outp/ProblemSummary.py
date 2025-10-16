import re
import typing

from . import _block
from .. import types
from .. import errors


class ProblemSummary(_block.Block):
    """
    Represents OUTP `1starting mcrun` blocks.

    Attributes:
        histories: Particle histories done.
        datetime: Run datetime.
        probid: Run problem id.
        neutron_data: Neutron creation data.
        proton_data: Proton creation data.
        computer_time: Computer time so far.
        max_bank: Maximum number ever in bank.
        computer_mcrun: Computer time in mcrun.
        bank_overflows: Bank overflow to backup.
        source_per_minute: Source particles per minute.
        random_numbers: Random numbers generated.
        most_random: Most random number used.
        most_history: History with most random number used.
        range_lower: Range of sampled source lower.
        range_upper: Range of sampled source upper.
    """

    _REGEX = re.compile(
        r'\A1problem summary                                                                                                           \n\n'
        r'      run terminated when (.{11})  particle histories were done[.]\n'
        r'[+]                                                                                                    (.{17}) \n\n'
        r' =====> (.{10}) M histories/hr    [(]based on wall-clock time in mcrun[)]\n\n\n'
        r'      (.+)     probid =  (.{17}) \n\n'
        r' neutron creation    tracks      weight        energy            neutron loss        tracks      weight        energy\n'
        r'                                 [(]per source particle[)]                                           [(]per source particle[)]\n\n'
        r'((?:.+\n)+\n(?:.+\n)+)\n'
        r' photon creation     tracks      weight        energy            photon loss         tracks      weight        energy\n'
        r'                                 [(]per source particle[)]                                           [(]per source particle[)]\n\n'
        r'((?:.+\n)+\n(?:.+\n)+)\n'
        r' computer time so far in this run     (.{12})            maximum number ever in bank   (.{7})\n'
        r' computer time in mcrun               (.{12})            bank overflows to backup file (.{7})\n'
        r' source particles per minute            (.{10})\n'
        r' random numbers generated              (.{11})            most random numbers used was (.{11}) in history (.{11})\n\n'
        r' range of sampled source weights = (.{10}) to (.{10})\n\Z'
    )

    def __init__(
        self,
        histories: types.String,
        datetime: types.String,
        histories_rate: types.String,
        title: types.String,
        probid: types.String,
        neutron_data: types.String,
        proton_data: types.String,
        computer_time: types.String,
        max_bank: types.String,
        computer_mcrun: types.String,
        bank_overflows: types.String,
        source_per_minute: types.String,
        random_numbers: types.String,
        most_random: types.String,
        most_history: types.String,
        range_lower: types.String,
        range_upper: types.String,
    ):
        """
        Initializes `ProblemSummary`.

        Parameters:
            histories: Particle histories done.
            datetime: Run datetime.
            histories_rate: Histories per hour.
            title: Simulation title.
            probid: Run problem id.
            neutron_data: Neutron creation data.
            proton_data: Proton creation data.
            computer_time: Computer time so far.
            max_bank: Maximum number ever in bank.
            computer_mcrun: Computer time in mcrun.
            bank_overflows: Bank overflow to backup.
            source_per_minute: Source particles per minute.
            random_numbers: Random numbers generated.
            most_random: Most random number used.
            most_history: History with most random number used.
            range_lower: Range of sampled source lower.
            range_upper: Range of sampled source upper.

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if histories is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, histories)
        if datetime is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, datetime)
        if histories_rate is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, histories_rate)
        if title is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, title)
        if probid is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, probid)
        if neutron_data is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, neutron_data)
        if proton_data is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, proton_data)
        if computer_time is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, computer_time)
        if max_bank is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, max_bank)
        if computer_mcrun is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, computer_mcrun)
        if bank_overflows is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, bank_overflows)
        if source_per_minute is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, source_per_minute)
        if random_numbers is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, random_numbers)
        if most_random is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, most_random)
        if most_history is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, most_history)
        if range_lower is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, range_lower)
        if range_upper is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, range_upper)

        self.histories: typing.Final[types.String] = histories
        self.datetime: typing.Final[types.String] = datetime
        self.histories_rate: typing.Final[types.String] = histories_rate
        self.title: typing.Final[types.String] = title
        self.probid: typing.Final[types.String] = probid
        self.neutron_data: typing.Final[types.String] = neutron_data
        self.proton_data: typing.Final[types.String] = proton_data
        self.computer_time: typing.Final[types.String] = computer_time
        self.max_bank: typing.Final[types.String] = max_bank
        self.computer_mcrun: typing.Final[types.String] = computer_mcrun
        self.bank_overflows: typing.Final[types.String] = bank_overflows
        self.source_per_minute: typing.Final[types.String] = source_per_minute
        self.random_numbers: typing.Final[types.String] = random_numbers
        self.most_random: typing.Final[types.String] = most_random
        self.most_history: typing.Final[types.String] = most_history
        self.range_lower: typing.Final[types.String] = range_lower
        self.range_upper: typing.Final[types.String] = range_upper

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `ProblemSummary` from OUTP.

        Parameters:
            source: OUTP for `ProblemSummary`.

        Returns:
            `ProblemSummary`.
        """

        tokens = ProblemSummary._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        histories = types.String.from_mcnp(tokens[1])
        datetime = types.String.from_mcnp(tokens[2])
        histories_rate = types.String.from_mcnp(tokens[3])
        title = types.String.from_mcnp(tokens[4])
        probid = types.String.from_mcnp(tokens[5])
        neutron_data = types.String.from_mcnp(tokens[6])
        proton_data = types.String.from_mcnp(tokens[7])
        computer_time = types.String.from_mcnp(tokens[8])
        max_bank = types.String.from_mcnp(tokens[9])
        computer_mcrun = types.String.from_mcnp(tokens[10])
        bank_overflows = types.String.from_mcnp(tokens[11])
        source_per_minute = types.String.from_mcnp(tokens[12])
        random_numbers = types.String.from_mcnp(tokens[13])
        most_random = types.String.from_mcnp(tokens[14])
        most_history = types.String.from_mcnp(tokens[15])
        range_lower = types.String.from_mcnp(tokens[16])
        range_upper = types.String.from_mcnp(tokens[17])

        return ProblemSummary(
            histories,
            datetime,
            histories_rate,
            title,
            probid,
            neutron_data,
            proton_data,
            computer_time,
            max_bank,
            computer_mcrun,
            bank_overflows,
            source_per_minute,
            random_numbers,
            most_random,
            most_history,
            range_lower,
            range_upper,
        )

    def to_mcnp(self):
        """
        Generates OUTP from `ProblemSummary`.

        Returns:
            OUTP for `ProblemSummary`.
        """

        return f"""
1problem summary                                                                                                           

      run terminated when {self.histories:11}  particle histories were done.
+                                                                                                    {self.datetime:17} 

 =====> {self.histories_rate:10} M histories/hr    (based on wall-clock time in mcrun)


      {self.title}     probid =  {self.probid:17} 

 neutron creation    tracks      weight        energy            neutron loss        tracks      weight        energy
                                 (per source particle)                                           (per source particle)

{self.neutron_data}
 photon creation     tracks      weight        energy            photon loss         tracks      weight        energy
                                 (per source particle)                                           (per source particle)

{self.proton_data}
 computer time so far in this run     {self.computer_time:12}            maximum number ever in bank   {self.max_bank:7}
 computer time in mcrun               {self.computer_mcrun:12}            bank overflows to backup file {self.bank_overflows:7}
 source particles per minute            {self.source_per_minute:10}
 random numbers generated              {self.random_numbers:11}            most random numbers used was {self.most_random:11} in history {self.most_history:11}

 range of sampled source weights = {self.range_lower:10} to {self.range_upper:10}
"""[1:]
