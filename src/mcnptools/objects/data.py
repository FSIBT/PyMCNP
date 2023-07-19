from typing import Dict, List, Optional

from rich import print


def parse_generic_parameters(components: List[str]):
    """Parse key-value pairs separated with equal signs."""

    parameters = {}
    for c in components:
        tmp = c.split("=")
        if len(tmp) == 2:
            parameters[tmp[0]] = tmp[1]
        else:
            print(f"[orange3]Warning[/] {c} not implemented.")
    return parameters


def is_numeric(value):
    """Quick test if a string can be converted to float.

    This is better than value.isnumeric(), since it can handle 1e6 or -1.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


class Data:
    all_data = []

    def __init__(self, name: str, parameters: Dict) -> None:
        self.name = name
        self.parameters = parameters

    @classmethod
    def get_all_data(cls):
        return cls.all_data

    def to_mcnp(self):
        out = f"{self.name} "
        for k, v in self.parameters.items():
            out += f"{k}={v} "
        return out.strip() + "\n"

    @classmethod
    def from_mcnp(cls, line):
        """Most lines in the data part will be parsed in the general class.

        For some we have specialized subclasses.
        """

        components = line.split()
        name = components[0].lower()

        if name == "ptrac":
            return Ptrac.from_mcnp(line)
        elif name == "sdef":
            return Source.from_mcnp(line)
        elif name == "nps":
            return Nps.from_mcnp(line)
        elif name == "mode":
            return Mode.from_mcnp(line)
        elif name == "rand":
            return Random.from_mcnp(line)
        elif name == "print":
            return Print.from_mcnp(line)
        elif name[0] == "s" and name[1] in "ibp":
            return SourceInformation.from_mcnp(line)
        elif name[0] == "f":
            return Tally.from_mcnp(line)
        elif name[0] == "e":
            return Energy.from_mcnp(line)

        parameters = parse_generic_parameters(components[1:])

        return cls(
            name=name,
            parameters=parameters,
        )


class Source(Data):
    def __init__(self, parameters):
        self.parameters = parameters

    def to_mcnp(self):
        out = "sdef "
        for k, v in self.parameters.items():
            out += f"{k}={v} "
        return out.strip() + "\n"

    @classmethod
    def from_mcnp(cls, line):
        """Most lines in the data part will be parsed in the general class.

        For some we have specialized subclasses.
        """

        components = line.split()
        name = components[0].lower()
        parameters = parse_generic_parameters(components[1:])

        return cls(
            parameters=parameters,
        )

    def __str__(self):
        out = "Source "
        for k, v in self.parameters.items():
            out += f"{k}={v} "
        return out.strip() + "\n"


class SourceInformation(Data):
    def __init__(self, name: str, values: List[float], option: Optional[str] = None):
        self.name = name
        self.option = option
        self.values = values

    def to_mcnp(self):
        out = f"{self.name} {self.option} "
        out += " ".join(self.values)
        return out.strip() + "\n"

    @classmethod
    def from_mcnp(cls, line):
        components = line.split()
        name = components[0].lower()
        if name.startswith("si"):
            tmp = components[1]
            if is_numeric(tmp):
                option = "H"
            else:
                option = tmp
                components = components[1:]
            values = components[1:]
        elif name.startswith("sp"):
            tmp = components[1]
            if not is_numeric(tmp):
                option = tmp
            else:
                option = float(tmp)
            values = components[1:]
        elif name.startswith("sb"):
            tmp = components[1]
            if not is_numeric(tmp):
                option = tmp
                components = components[1:]
            else:
                option = float(tmp)
                if option >= 0:
                    option = "D"
                else:
                    components = components[1:]
            values = components[1:]

        return cls(name, values, option)

    def __str__(self):
        out = f"Source infornation {self.name} {self.option}: "
        out += "     " + " ".join(self.values)
        return out.strip() + "\n"


class Nps(Data):
    def __init__(self, number):
        self.number = number

    def to_mcnp(self):
        return f"nps {self.number}\n"

    @classmethod
    def from_mcnp(cls, line):
        components = line.split()

        number = components[1]
        if is_numeric(number):
            number = int(float(number))
        else:
            print(f"[red]Error[/] Cannot parse {number}")
            return
        return cls(number)

    def __str__(self):
        return f"Number of particles: {self.number}\n"


class Print(Data):
    def __init__(self, values):
        self.values = values

    def to_mcnp(self):
        out = "Print " + " ".join(self.values)
        return out.strip() + "\n"

    @classmethod
    def from_mcnp(cls, line):
        components = line.split()

        values = components[1:]
        return cls(values)

    def __str__(self):
        return f"Print: {' '.join(self.values)}\n"


class Random(Data):
    def __init__(self, parameters):
        self.parameters = parameters

    def to_mcnp(self):
        out = f"RAND "
        out += " ".join(f"{k}={v}" for k, v in self.parameters.items())
        return out.strip() + "\n"

    @classmethod
    def from_mcnp(cls, line):
        components = line.split()

        parameters = parse_generic_parameters(components[1:])

        return cls(parameters)

    def __str__(self):
        out = "Random "
        for k, v in self.parameters.items():
            out += f"{k}={v} "
        return out.strip() + "\n"


class Mode(Data):
    def __init__(self, neutrons: bool = False, photons: bool = False):
        self.neutrons = neutrons
        self.photons = photons

    def to_mcnp(self):
        out = "mode "
        if self.neutrons:
            out += "n "
        if self.photons:
            out += "p "
        return out.strip() + "\n"

    @classmethod
    def from_mcnp(cls, line):
        components = line.split()[1:]

        photons = "p" in components
        neutrons = "n" in components

        return cls(neutrons, photons)

    def __str__(self):
        out = "Mode "
        if self.neutrons:
            out += "neutrons "
        if self.photons:
            out += "photons "
        return out.strip() + "\n"


class Ptrac(Data):
    def __init__(self, parameters):
        self.parameters = parameters

    def to_mcnp(self):
        out = "PTRAC "
        for k, v in self.parameters.items():
            out += f"{k}={v} "
        return out.strip() + "\n"

    @classmethod
    def from_mcnp(cls, line):
        """Most lines in the data part will be parsed in the general class.

        For some we have specialized subclasses.
        """

        components = line.split()

        parameters = parse_generic_parameters(components[1:])

        return cls(
            parameters=parameters,
        )

    def __str__(self):
        out = "Ptrac "
        for k, v in self.parameters.items():
            out += f"{k}={v} "
        return out.strip() + "\n"


class Tally(Data):
    def __init__(self, number, particle, parameters: str):
        self.number = number
        self.particle = particle
        self.parameters = parameters

    def to_mcnp(self):
        return f"F{self.number}:{self.particle} {self.parameters}\n"

    @classmethod
    def from_mcnp(cls, line):
        """Most lines in the data part will be parsed in the general class.

        For some we have specialized subclasses.
        """

        components = line.split()

        name = components[0]

        a, particle = name.split(":")
        number = int(a[1:])

        parameters = " ".join(components[1:])

        return cls(number, particle, parameters=parameters)

    def __str__(self):
        out = f"Tally number={self.number} particle={self.particle}:\n"
        out += f"     {self.parameters}\n"
        return out


class Energy(Data):
    def __init__(
        self,
        number,
        bins,
        nt: Optional[bool] = False,
        cumulative: Optional[bool] = False,
    ):
        self.number = number
        self.bins = bins
        self.nt = nt
        self.cumulative = cumulative

    def to_mcnp(self):
        nt = " NT" if self.nt else ""
        c = " C" if self.cumulative else ""
        bins = " ".join(str(x) for x in self.bins)
        return f"E{self.number} {bins}{nt}{c}\n"

    @classmethod
    def from_mcnp(cls, line):
        """Most lines in the data part will be parsed in the general class.

        For some we have specialized subclasses.
        """

        components = line.split()

        number = int(components[0][1:])
        components = components[1:]

        nt = False
        c = False
        if components[-1].lower() == "c":
            c = True
            if components[-2].lower() == "nt":
                nt = True
                components = components[:-1]
            components = components[:-1]
        elif components[-1].lower() == "nt":
            nt = True
            components = components[:-1]

        return cls(number, components, nt=nt, cumulative=c)

    def __str__(self):
        out = f"Energy number={self.number} no_total={self.nt} cumulative={self.cumulative}:\n"
        out += f"    bins: {self.bins}\n"
        return out
