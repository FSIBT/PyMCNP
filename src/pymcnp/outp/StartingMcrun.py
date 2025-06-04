import re
import typing

from . import _block
from ..utils import types
from ..utils import errors


class StartingMcrun(_block.Block):
    """
    Represents OUTP ``1starting mcrun`` blocks.

    Attributes:
        cp0: Geometry error.
        title: Problem title.
        data: First 50 source particles.
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
        r'\A1starting mcrun.      cp0 = (.{5})                                                                       print table 110\n\n'
        r'      (.{80})\n\n\n'
        r'     nps    x          y          z          cell       surf     u          v          w        energy     weight      time\n \n'
        r'((?:.+\n)+)'
        r'1problem summary                                                                                                           \n\n'
        r'      run terminated when (.{11})  particle histories were done[.]\n'
        r'[+]                                                                                                    (.{17}) \n'
        r'      .{80}     probid =  (.{17}) \n\n'
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
        cp0: types.String,
        title: types.String,
        data: types.String,
        histories: types.String,
        datetime: types.String,
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
        Initializes ``StartingMcrun``.

        Parameters:
            cp0: Geometry error.
            title: Problem title.
            data: First 50 source particles.
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

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if cp0 is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, cp0)
        if title is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, title)
        if data is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, data)
        if histories is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, histories)
        if datetime is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, datetime)
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

        self.cp0: typing.Final[types.String] = cp0
        self.title: typing.Final[types.String] = title
        self.data: typing.Final[types.String] = data
        self.histories: typing.Final[types.String] = histories
        self.datetime: typing.Final[types.String] = datetime
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
        Generates ``StartingMcrun`` from OUTP.

        Parameters:
            source: OUTP for ``StartingMcrun``.

        Returns:
            ``StartingMcrun``.
        """

        tokens = StartingMcrun._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        cp0 = types.String.from_mcnp(tokens[1])
        title = types.String.from_mcnp(tokens[2])
        data = types.String.from_mcnp(tokens[3])
        histories = types.String.from_mcnp(tokens[4])
        datetime = types.String.from_mcnp(tokens[5])
        probid = types.String.from_mcnp(tokens[6])
        neutron_data = types.String.from_mcnp(tokens[7])
        proton_data = types.String.from_mcnp(tokens[8])
        computer_time = types.String.from_mcnp(tokens[9])
        max_bank = types.String.from_mcnp(tokens[10])
        computer_mcrun = types.String.from_mcnp(tokens[11])
        bank_overflows = types.String.from_mcnp(tokens[12])
        source_per_minute = types.String.from_mcnp(tokens[13])
        random_numbers = types.String.from_mcnp(tokens[14])
        most_random = types.String.from_mcnp(tokens[15])
        most_history = types.String.from_mcnp(tokens[16])
        range_lower = types.String.from_mcnp(tokens[17])
        range_upper = types.String.from_mcnp(tokens[18])

        return StartingMcrun(
            cp0,
            title,
            data,
            histories,
            datetime,
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
        Generates OUTP from ``StartingMcrun``.

        Returns:
            OUTP for ``StartingMcrun``.
        """

        return f"""
1starting mcrun.      cp0 = {self.cp0:5}                                                                       print table 110

      {self.title:80}


     nps    x          y          z          cell       surf     u          v          w        energy     weight      time

{self.data}
1problem summary                                                                                                           

      run terminated when {self.histories:11}  particle histories were done.
[+]                                                                                                    {self.datetime:17}
      {self.title:80}     probid =  {self.probid:17} 

neutron creation    tracks      weight        energy            neutron loss        tracks      weight        energy
                                 (per source particle)                                           (per source particle)

{self.neutron_data}
 photon creation     tracks      weight        energy            photon loss         tracks      weight        ener
                                 (per source particle)                                           (per source particle)

{self.proton_data}
 computer time so far in this run     {self.computer_time:11}            maximum number ever in bank   {self.max_bank:7}
 computer time in mcrun               {self.computer_mcrun:11}            bank overflows to backup file {self.bank_overflows:7}
 source particles per minute            {self.source_per_minute:11}
 random numbers generated              {self.random_numbers:11}            most random numbers used was {self.most_random:11} in history {self.most_history:11}

 range of sampled source weights = {self.range_lower:10} to {self.range_upper:10}
"""[1:-1]
