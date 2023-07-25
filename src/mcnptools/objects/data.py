from typing import Dict, List, Optional

from rich import print

from ..input_line import InputLine


def parse_generic_parameters(components: List[str]):
    """Parse key-value pairs separated with equal signs."""

    parameters = {}
    for c in components:
        tmp = c.split("=")
        if len(tmp) == 2:
            parameters[tmp[0]] = tmp[1]
        else:
            print(f"[orange3]Warning[/] Data: {c} not implemented (in {components}).")
    return parameters


def parse_number(value: str, requested_type=float):
    value = value.strip()
    if value == "j":
        return None
    else:
        return requested_type(value)


def to_number(value) -> str:
    if value is None:
        return "j"

    return str(value)


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

    def __init__(
        self,
        name: str,
        parameters: Dict,
        comment: Optional[str] = None,
    ) -> None:
        self.name = name
        self.parameters = parameters
        self.comment = comment

    @classmethod
    def get_all_data(cls):
        return cls.all_data

    def to_mcnp(self):
        out = f"{self.name} "
        for k, v in self.parameters.items():
            out += f"{k}={v} "
        out = out.strip()
        if self.comment:
            out += f" $ {self.comment}"
        return out + "\n"

    @classmethod
    def from_mcnp(cls, line: InputLine):
        """Most lines in the data part will be parsed in the general class.

        For some we have specialized subclasses.
        """

        components = line.text.split()
        comment = line.comment
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
        elif name.startswith("cut"):
            return Cut.from_mcnp(line)
        elif name[0] == "s" and name[1] in "ibp":
            return SourceInformation.from_mcnp(line)
        elif name.startswith("fm"):
            return TallyMultiplier.from_mcnp(line)
        elif name[0] == "f":
            return Tally.from_mcnp(line)
        elif name[0] == "e":
            return Energy.from_mcnp(line)

        parameters = parse_generic_parameters(components[1:])

        return cls(name=name, parameters=parameters, comment=comment)


class Source(Data):
    def __init__(self, parameters, comment: Optional[str] = None):
        self.parameters = parameters
        self.comment = comment

    def to_mcnp(self):
        out = "sdef "
        for k, v in self.parameters.items():
            out += f"{k}={v} "
        out = out.strip()
        if self.comment:
            out += f" $ {self.comment}"
        return out + "\n"

    @classmethod
    def from_mcnp(cls, line: InputLine):
        """Most lines in the data part will be parsed in the general class.

        For some we have specialized subclasses.
        """

        components = line.text.split()
        comment = line.comment
        parameters = parse_generic_parameters(components[1:])

        return cls(parameters=parameters, comment=comment)

    def __str__(self):
        out = "Source "
        if self.comment:
            out += f" ({self.comment}) "
        for k, v in self.parameters.items():
            out += f"{k}={v} "
        return out.strip() + "\n"


class SourceInformation(Data):
    def __init__(
        self,
        name: str,
        values: List[float],
        option: Optional[str] = None,
        comment: Optional[str] = None,
    ):
        self.name = name
        self.option = option
        self.values = values
        self.comment = comment

    def to_mcnp(self):
        out = f"{self.name} {self.option} "
        out += " ".join(self.values)
        if self.comment:
            out += f" $ {self.comment}"
        return out.strip() + "\n"

    @classmethod
    def from_mcnp(cls, line: InputLine):
        components = line.text.split()
        comment = line.comment

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

        return cls(name, values, option, comment=comment)

    def __str__(self):
        comment = f" ({self.comment})" if self.comment else ""
        out = f"Source information {self.name} {self.option}{comment}: "
        out += "     " + " ".join(self.values)
        return out.strip() + "\n"


class Nps(Data):
    def __init__(self, number, comment: Optional[str] = None):
        self.number = number
        self.comment = comment

    def to_mcnp(self):
        out = f"nps {self.number}"
        if self.comment:
            out += f" $ {self.comment}"
        return out + "\n"

    @classmethod
    def from_mcnp(cls, line: InputLine):
        components = line.text.split()
        comment = line.comment

        number = components[1]
        if is_numeric(number):
            number = int(float(number))
        else:
            print(f"[red]Error[/] Cannot parse {number}")
            return
        return cls(number, comment)

    def __str__(self):
        out = f"Number of particles: {self.number}"
        if self.comment:
            out += f" ({self.comment})"
        return out + "\n"


class Print(Data):
    def __init__(self, values, comment: Optional[str] = None):
        self.values = values
        self.comment = comment

    def to_mcnp(self):
        out = "Print " + " ".join(self.values)
        if self.comment:
            out += f" $ {self.comment}"
        return out.strip() + "\n"

    @classmethod
    def from_mcnp(cls, line: InputLine):
        components = line.text.split()
        comment = line.comment

        values = components[1:]
        return cls(values, comment)

    def __str__(self):
        out = f"Print: {' '.join(self.values)}"
        if self.comment:
            out += f" ({self.comment})"
        return out + "\n"


class Random(Data):
    def __init__(self, parameters, comment: Optional[str] = None):
        self.parameters = parameters
        self.comment = comment

    def to_mcnp(self):
        out = f"RAND "
        out += " ".join(f"{k}={v}" for k, v in self.parameters.items())
        out = out.strip()
        if self.comment:
            out += f" $ {self.comment}"
        return out + "\n"

    @classmethod
    def from_mcnp(cls, line: InputLine):
        components = line.text.split()
        comment = line.comment

        parameters = parse_generic_parameters(components[1:])

        return cls(parameters, comment)

    def __str__(self):
        out = "Random "
        for k, v in self.parameters.items():
            out += f"{k}={v} "
        out = out.strip()
        if self.comment:
            out += f" $ {self.comment}"
        return out + "\n"


class Mode(Data):
    def __init__(
        self,
        neutrons: bool = False,
        photons: bool = False,
        comment: Optional[str] = None,
    ):
        self.neutrons = neutrons
        self.photons = photons
        self.comment = comment

    def to_mcnp(self):
        out = "mode "
        if self.neutrons:
            out += "n "
        if self.photons:
            out += "p "
        out = out.strip()
        if self.comment:
            out += f" ${self.comment}"
        return out + "\n"

    @classmethod
    def from_mcnp(cls, line: InputLine):
        components = line.text.split()[1:]
        comment = line.comment

        photons = "p" in components
        neutrons = "n" in components

        return cls(neutrons, photons, comment)

    def __str__(self):
        out = "Mode "
        if self.comment:
            out += f"({self.comment}) "
        if self.neutrons:
            out += "neutrons "
        if self.photons:
            out += "photons "
        out = out.strip()
        return out + "\n"


class Ptrac(Data):
    def __init__(self, parameters, comment: Optional[str] = None):
        self.parameters = parameters
        self.comment = comment

    def to_mcnp(self):
        out = "PTRAC "
        for k, v in self.parameters.items():
            out += f"{k}={v} "
        out = out.strip()
        if self.comment:
            out += f"$ {self.comment}"
        return out + "\n"

    @classmethod
    def from_mcnp(cls, line: InputLine):
        """Most lines in the data part will be parsed in the general class.

        For some we have specialized subclasses.
        """

        components = line.text.split()
        comment = line.comment

        parameters = parse_generic_parameters(components[1:])

        return cls(parameters=parameters, comment=comment)

    def __str__(self):
        out = "Ptrac "
        for k, v in self.parameters.items():
            out += f"{k}={v} "
        out = out.strip()
        if self.comment:
            out += f" $ {self.comment}"
        return out + "\n"


class Tally(Data):
    def __init__(
        self, number, particle, parameters: str, comment: Optional[str] = None
    ):
        self.number = number
        self.particle = particle
        self.parameters = parameters
        self.comment = comment

    def to_mcnp(self):
        out = f"F{self.number}:{self.particle} {self.parameters}"
        if self.comment:
            out += f" $ {self.comment}"
        return out + "\n"

    @classmethod
    def from_mcnp(cls, line: InputLine):
        """Most lines in the data part will be parsed in the general class.

        For some we have specialized subclasses.
        """

        components = line.text.split()
        comment = line.comment

        name = components[0]

        a, particle = name.split(":")
        number = int(a[1:])

        parameters = " ".join(components[1:])

        return cls(number, particle, parameters=parameters, comment=comment)

    def __str__(self):
        comment = f" ({self.comment})" if self.comment else ""
        out = f"Tally number={self.number} particle={self.particle}{comment}:\n"
        out += f"     {self.parameters}\n"
        return out


class TallyMultiplier(Data):
    def __init__(self, number: int, parameters, comment: Optional[str] = None):
        self.number = number
        self.parameters = parameters
        self.comment = comment

    def to_mcnp(self):
        out = f"FM{self.number} "
        out += " ".join(self.parameters)
        out = out.strip()
        if self.comment:
            out += f" $ {self.comment}"
        return out + "\n"

    @classmethod
    def from_mcnp(cls, line: InputLine):
        components = line.text.split()
        comment = line.comment

        number = int(components[0][2:])

        parameters = components[1:]

        return cls(number, parameters, comment)

    def __str__(self):
        out = "Tally Multiplier {self.number} "
        if self.comment:
            out += f" ({self.comment})"
        out = out.strip() + "\n"
        for p in self.parameters:
            out += f"{p} "
        out = out.strip()
        return out + "\n"


class Cut(Data):
    def __init__(
        self,
        particle,
        time_cutoff,
        energy_cutoff,
        weight_cutoff,
        weight_min,
        comment: Optional[str] = None,
    ):
        self.particle = particle
        self.time_cutoff = time_cutoff
        self.energy_cutoff = energy_cutoff
        self.weight_cutoff = weight_cutoff
        self.weight_min = weight_min
        self.comment = comment

    def to_mcnp(self):
        # go through reverse order, so that we can skip undefined options at the back
        if self.weight_min is None:
            out = " "
        else:
            out = f" {self.weight_min}"

        if self.weight_cutoff is None:
            if out:
                out = "j j " + out
        else:
            out = f"{self.weight_cutoff[0]} {self.weight_cutoff[1]} " + out

        if self.energy_cutoff is None:
            if out:
                out = "j " + out
        else:
            out = f"{self.energy_cutoff} " + out

        if self.time_cutoff is None:
            if out:
                out = "j " + out
        else:
            out = f"{self.time_cutoff} " + out

        out = f"cut:{self.particle} " + out
        return out.strip() + "\n"

    @classmethod
    def from_mcnp(cls, line: InputLine):
        components = line.text.split()
        comment = line.comment

        particle = ""
        tc = None
        ec = None
        wc = None
        w_min = None

        for i, c in enumerate(components):
            if i == 0:
                particle = c[4]
            elif i == 1:
                tc = parse_number(c)
            elif i == 2:
                ec = parse_number(c)
            elif i == 3:
                wc = parse_number(c)
                if wc is not None:
                    wc = [wc, None]
            elif i == 4:
                tmp = parse_number(c)
                if wc:
                    wc[1] = tmp
            elif i == 5:
                w_min = parse_number(c)

        if wc is not None:
            if (wc[0] is None) or (wc[1] is None):
                print(
                    f"[orange3]Warning[/] Parsing '{line.text}'. Possible bug: only one weight cutoff given! ... Fixing it."
                )
            wc[0] = wc[0] if wc[0] is not None else 0
            wc[1] = wc[1] if wc[1] is not None else 0
        return cls(particle, tc, ec, wc, w_min, comment)

    def __str__(self):
        comment = f" ({self.comment})" if self.comment else ""
        p = self.particle
        tc = self.time_cutoff
        ec = self.energy_cutoff
        wc = self.weight_cutoff
        w_min = self.weight_min

        out = f"Cut particle={p}{comment}:\n"
        if tc:
            out += f"    time cutoff: {tc}\n"
        if ec:
            out += f"    energy cutoff: {ec}\n"
        if wc:
            out += f"    weight cutoff: {wc}\n"
        if w_min:
            out += f"    weight min: {w_min}\n"
        return out


class Energy(Data):
    def __init__(
        self,
        number,
        bins,
        nt: Optional[bool] = False,
        cumulative: Optional[bool] = False,
        comment: Optional[str] = None,
    ):
        self.number = number
        self.bins = bins
        self.nt = nt
        self.cumulative = cumulative
        self.comment = comment

    def to_mcnp(self):
        nt = " NT" if self.nt else ""
        c = " C" if self.cumulative else ""
        bins = " ".join(str(x) for x in self.bins)
        comment = f" $ {self.comment}" if self.comment else ""
        return f"E{self.number} {bins}{nt}{c}{comment}\n"

    @classmethod
    def from_mcnp(cls, line: InputLine):
        """Most lines in the data part will be parsed in the general class.

        For some we have specialized subclasses.
        """

        components = line.text.split()
        comment = line.comment

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

        return cls(number, components, nt=nt, cumulative=c, comment=comment)

    def __str__(self):
        comment = f" ({self.comment})" if self.comment else ""
        n = self.number
        nt = self.nt
        c = self.cumulative
        out = f"Energy number={n} no_total={nt} cumulative={c}{comment}:\n"
        out += f"    bins: {self.bins}\n"
        return out
