import re
import dataclasses

_REGEX_VERSION = re.compile(r'Code Name & Version = (.*\S)')
_REGEX_NPS = re.compile(r'^ *dump no\. +\d+ on file .*? nps = +(\d+)', re.MULTILINE)
_REGEX_TIME = re.compile(r'^ *computer time = +([\d.]+) minutes', re.MULTILINE)
_REGEX_TERMINATED = re.compile(r'^ *run terminated (when +(\d+) +(?:(kcode cycles)|particle histories) +were done|because of fatal errors)', re.MULTILINE)
_REGEX_WARNING = re.compile(r'^ *warning\. +(.*\S)', re.MULTILINE)
_REGEX_KEFF = re.compile(r'^ *final result +([\d.]+) +([\d.]+) ', re.MULTILINE)
_REGEX_CHECK = re.compile(
    r'^ +(\d+) +(?:passed the 10 statistical checks|missed +(\d+) of 10 tfc bin checks: (.*\S))',
    re.MULTILINE,
)


@dataclasses.dataclass
class TallyCheck:
    """
    Represents the statistical checks of one tally's fluctuation chart bin.

    Attributes:
        number: Tally number.
        passed: Whether the bin passed all 10 statistical checks.
        failed: Number of checks that were missed.
        message: MCNP's reason for the first missed check, empty if all passed.
    """

    number: int
    passed: bool
    failed: int = 0
    message: str = ''


@dataclasses.dataclass
class Summary:
    """
    Represents the headline results of an output file.

    Values that the output does not contain (e.g., `keff` without `KCODE`) are `None`.

    Attributes:
        version: Code name and version, e.g., `'MCNP6, 1.0'`.
        nps: Number of histories (source particles) run.
        run_time: Computer time in minutes.
        terminated: Why the run ended: `'histories'`, `'cycles'`, `'fatal errors'`, or `None` if the output does not say.
        keff: Final combined `keff` of a `KCODE` problem.
        keff_sd: Standard deviation of `keff`.
        fatal_errors: Fatal errors MCNP reported.
        warnings: Warnings MCNP printed, in order, without repeats.
        checks: Statistical checks by tally number.
    """

    version: str | None = None
    nps: int | None = None
    run_time: float | None = None
    terminated: str | None = None
    keff: float | None = None
    keff_sd: float | None = None
    fatal_errors: list[str] = dataclasses.field(default_factory=list)
    warnings: list[str] = dataclasses.field(default_factory=list)
    checks: dict[int, TallyCheck] = dataclasses.field(default_factory=dict)

    @property
    def ok(self) -> bool:
        """
        Whether the run finished without fatal errors.
        """

        return self.terminated in ('histories', 'cycles') and not self.fatal_errors

    @property
    def checks_passed(self) -> bool | None:
        """
        Whether every tally passed all statistical checks, `None` if the output has no such checks.
        """

        return all(check.passed for check in self.checks.values()) if self.checks else None

    @classmethod
    def from_text(cls, text: str, fatal_errors: list[str] | None = None) -> 'Summary':
        """
        Reads the headline results from the text of an output file.

        Parameters:
            text: Text of the output file.
            fatal_errors: Fatal errors MCNP reported, if known.
        """

        summary = cls(fatal_errors=fatal_errors or [])

        if match := _REGEX_VERSION.search(text):
            summary.version = match[1]

        if matches := _REGEX_NPS.findall(text):
            summary.nps = int(matches[-1])

        if matches := _REGEX_TIME.findall(text):
            summary.run_time = float(matches[-1])

        if found := list(_REGEX_TERMINATED.finditer(text)):
            last = found[-1]
            summary.terminated = 'fatal errors' if last[1].startswith('because') else ('cycles' if last[3] else 'histories')

        if found := list(_REGEX_KEFF.finditer(text)):
            summary.keff, summary.keff_sd = float(found[-1][1]), float(found[-1][2])

        summary.warnings = list(dict.fromkeys(match[1] for match in _REGEX_WARNING.finditer(text)))

        for match in _REGEX_CHECK.finditer(text):
            failed = int(match[2] or 0)
            summary.checks[int(match[1])] = TallyCheck(int(match[1]), failed == 0, failed, match[3] or '')

        return summary
