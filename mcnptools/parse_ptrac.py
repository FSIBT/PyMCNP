"""
Parsing ptrac files from MCNP
"""

from collections import namedtuple
from fortranformat import FortranRecordReader

Position = namedtuple("Position", "x y z")

# direction cosines for each axis
Direction = namedtuple("Direction", "u v w")


PARTICLE = {1: "neutron", 2: "photon"}


def get_particle(nr):
    name = PARTICLE.get(nr, None)
    if name:
        return name
    print(f"WARNING: need to implement particle type {nr}, see page 166 in the manual")
    return ""


KEYWORDS = {
    1: "Buffer",
    2: "Cell",
    3: "Event",
    4: "File",
    5: "Filter",
    6: "Max",
    7: "Menp",
    8: "NPS",
    9: "Surface",
    10: "Tally",
    11: "Type",
    12: "Value",
    13: "Write",
    14: "unknown",
}

types = {1: "initial source", 2: "bank", 3: "surface", 4: "collision", 5: "termination"}

IDs = {
    1: "NPS",
    2: "first event type",
    3: "NCL",
    4: "NSF",
    5: "JPTAL",
    6: "TAL",
    7: "next event type",
    8: "NODE",
    9: "NSR",
    10: "NXS",
    11: "NTYN/MTP",
    12: "Surface number",
    13: "angle with surface normal",
    14: "termination type",
    15: "branch number for this history",
    16: "IPT",
    17: "NCL",
    18: "MAT",
    19: "NCP",
    20: "XXX",
    21: "YYY",
    22: "ZZZ",
    23: "UUU",
    24: "VVV",
    25: "WWW",
    26: "ERG",
    27: "WGT",
    28: "TME",
}


def parse_ID(list):
    return [IDs[i] for i in list]


event_type = {
    1000: "initial source",
    3000: "surface",
    4000: "collision",
    5000: "termination",
    9000: "final",
}


bank_event_type = {
    1: ["DXTRAN Track", True],
    2: ["Energy Split", False],
    3: ["Weight-Window Surface Split", False],
    4: ["Weight-Window Collision Split", True],
    5: ["Forced Collision-Uncollided Part", False],
    6: ["Importance Split", False],
    7: [
        "Neutron from Neutron ( n , xn ) ( n , f ) and "
        "Secondary Particles from Library Protons",
        True,
    ],
    8: ["Photon from Neutron", True],
    9: ["Photon from Double Fluorescence", True],
    10: ["Photon from Annihilation", False],
    11: ["Electron from Photoelectric", True],
    12: ["Electron from Compton", True],
    13: ["Electron from Pair Production", True],
    14: ["Auger Electron from Photon/X-ray", True],
    15: ["Positron from Pair Production", False],
    16: ["Bremsstrahlung from Electron", True],
    17: ["Knock-on Electron", False],
    18: ["X-rays from Electron", False],
    19: ["Photon from Neutron - Multigroup", True],
    20: ["Neutron ( n , f ) - Multigroup", True],
    21: ["Neutron ( n , xn ) k- Multigroup", True],
    22: ["Photo from Photon - Multigroup", True],
    23: ["Adjoint Weight Split - Multigroup", False],
    24: ["Weight-Window Pseudo-Collision Split", False],
    25: ["Secondary Particles from Photonuclear", True],
    26: ["DXTRAN annihilation photon from pulse-height tally variance reduction", True],
    30: ["Light Ions from Neutrons", True],
    31: ["Light Ions from Protons", True],
    32: ["Library Neutrons from Model Neutrons", False],
    33: ["Secondary Particles from Inelastic Nuclear Interactions", False],
    34: ["Secondary Particles from Elastic Nuclear Interactions", False],
}


def lookup_ntyn(idx, neutron=True):
    if neutron:
        if idx == 1:
            return "Inelastic S(alpha, beta)"
        elif idx == 2:
            return "Elastic S(alpha, beta)"
        elif idx == -99:
            return "Elastic scatter/Inelastic scatter"
        elif idx > 5:
            return "ENDF Reaction ID"
        else:
            return f"Error ntyn lookup: shouldn't happen {idx}"
    else:
        if idx == 1:
            return "Incoheren scatter"
        elif idx == 2:
            return "Coherent scatter"
        elif idx == 3:
            return "Fluorescence"
        elif idx == 4:
            return "Pair production"
        elif idx == 5:
            return "Pair production"
        else:
            return f"Error ntyn lookup: shouldn't happen {idx}"


def lookup_mtp(idx, neutron=True):
    if neutron:
        if idx == 4:
            return "Inelastic S(alpha, beta)"
        elif idx == 2:
            return "Elastic S(alpha, beta)"
        elif idx > 0:
            return "Elastic scatter/Inelastic scatter"
        else:
            return f"Error mtp lookup: shouldn't happen: {idx}"
    else:
        if idx == -1:
            return "Incoheren scatter"
        elif idx == -2:
            return "Coherent scatter"
        elif idx == -3:
            return "Fluorescence"
        elif idx == -4:
            return "Pair production"
        else:
            return f"Error mtp lookup: shouldn't happen {idx}"


def parse_event(event):
    if event in event_type:
        return event_type[event]
    return "bank"


def parse_bank(event):
    if event > 1999:
        event -= 2000
        if event in bank_event_type:
            return bank_event_type[event]
    elif event < -1999:
        event *= -1
        event -= 2000
        if event in bank_event_type:
            return bank_event_type[event]


termination_type = {
    1: "Escape",
    2: "Energy cutoff",
    3: "Time cutoff",
    4: "Weight window",
    5: "Cell importance",
    6: "Weight cutoff",
    7: "Energy importance",
    8: "DXTRAN",
    9: "Forced collision",
    10: "Exponential transform",
}

termination_type_neutron = {
    11: "Downscattering",
    12: "Capture",
    13: "Loss to (x, xn)",
    14: "Loss to fission",
    15: "Nuclear Interactions",
    16: "Particle decay",
    17: "Tabular boundary",
}

termination_type_photon = {
    11: " Compton scatter",
    12: "Capture",
    13: "Pair production",
    14: "Photonuclear",
}


def get_termination_type(idx, particle):
    if idx < 11:
        return termination_type[idx]
    if particle == "neutron":
        return termination_type_neutron[idx]
    if particle == "photon":
        return termination_type_photon[idx]
    else:
        return f"need to implement termination type {idx} for {particle}"


class Event:
    """Save information from a single event in a particles history


    For example a single gamma event in a cascade.
    """

    def __init__(self, parent, line=None, header=None):
        self.event_type = parent.current_event
        self.bank_extra = False
        self.ntyn = None
        self.nxs = None
        self.source = None
        self.pos = None
        self.particle = None
        self.cell_number = None
        self.material = None
        self.surface = None
        self.angle = None
        self.termination_type = None
        self.next_event = None
        self.node = None
        self.branch_number = None
        self.ncp = None
        self.dir = None
        self.energy = None
        self.weight = None
        self.time = None
        self.misc = None
        self.parent = parent
        self.header = header

        if line:
            self.parse(parent, line)

    def __repr__(self):
        out = ""
        out += f"  type: {self.event_type}\n"
        if self.particle:
            out += f"  particle type: {self.particle}\n"
        if self.ntyn:
            out += f"  ntyn: {self.ntyn}\n"
        if self.nxs:
            out += f"  nxs: {self.nxs}\n"
        if self.node:
            out += f"  node: {self.node}\n"
        if self.pos:
            out += f"  loc: {self.pos.x} {self.pos.y} {self.pos.z}\n"
        if self.dir:
            out += f"  dir: {self.dir.u} {self.dir.v} {self.dir.w}\n"
        if self.energy:
            out += f"  energy: {self.energy}\n"
        if self.weight:
            out += f"  weight: {self.weight}\n"
        if self.time:
            out += f"  time: {self.time}\n"
        if self.branch_number:
            out += f"  branch number: {self.branch_number}\n"
        if self.surface:
            out += f"  surface number: {self.surface}\n"
        if self.angle:
            out += f"  angle with surface normal: {self.angle}\n"
        if self.cell_number:
            out += f"  cell number: {self.cell_number}\n"
        if self.source:
            out += f"  source: {self.source}\n"
        if self.material:
            out += f"  material: {self.material}\n"
        if self.termination_type:
            out += f"  termination type: {self.termination_type}\n"
        if self.misc:
            for k, v in self.misc.items():
                out += f"  misc:  {k} {v}\n"
        return out

    def parse(self, hist, line):
        """Takes an input line and extracts all the information into
        this class
        """
        # convert to array of numbers
        line = [float(i) for i in line]
        d = {k: v for k, v in zip(self.header.IDS[hist.current_event], line)}
        if hist.current_event == "bank":
            t, e = parse_bank(hist.current_event_id)
            d["type"] = t
            d["bank extra"] = e
        else:
            d["type"] = hist.current_event

        # sort into event class
        self.event_type = d.pop("type", None)
        self.bank_extra = d.pop("bank extra", None)
        if self.bank_extra or self.event_type == "collision":
            self.ntyn = lookup_ntyn(int(d.pop("NTYN/MTP")))
            self.nxs = d.pop("NXS")
        self.particle = d.pop("IPT", None)
        self.source = d.pop("NSR", None)
        self.node = d.pop("NODE", None)
        self.surface = d.pop("Surface number", None)
        if self.particle:
            self.particle = get_particle(int(self.particle))
        self.cell_number = d.pop("NCL", None)
        if self.cell_number:
            self.cell_number = int(self.cell_number)
        self.material = d.pop("MAT", None)
        self.branch_number = d.pop("branch number for this history", None)
        self.angle = d.pop("angle with surface normal", None)
        self.termination_type = d.pop("termination type", None)
        if self.termination_type:
            self.termination_type = get_termination_type(
                self.termination_type, self.particle
            )
        x = d.pop("XXX", None)
        y = d.pop("YYY", None)
        z = d.pop("ZZZ", None)
        if x is not None and y is not None and z is not None:
            self.pos = Position(float(x), float(y), float(z))
        u = d.pop("UUU", None)
        v = d.pop("VVV", None)
        w = d.pop("WWW", None)
        if u is not None and v is not None and w is not None:
            self.dir = Direction(float(u), float(v), float(w))
        self.ncp = d.pop("NCP", None)
        self.energy = d.pop("ERG", None)
        self.weight = d.pop("WGT", None)
        self.time = d.pop("TME", None)
        d.pop("next event type", None)
        self.misc = d

        # update for next event
        hist.current_event_id = int(line[0])
        hist.current_event = parse_event(hist.current_event_id)


class History:
    """Save information of a whole neutron cascade.

    A History contains multiple Event classes that describe the single particles or collisions
    """

    def __init__(self, line=None, header=None):
        if line is not None:
            n1 = str(header.N1 - 1)
            form = FortranRecordReader(f"(1x,{n1}i10,e13.5)")
            line = form.read(line)  # NPS Line (I line)
            if len(line) == 2:
                n, next_type_id = line
                next_type = parse_event(int(next_type_id))
            elif len(line) == 3:
                n, next_type_id, a = line
                next_type = parse_event(int(next_type_id))
            elif len(line) == 4:
                n, next_type_id, a, b = line
                next_type = parse_event(int(next_type_id))
                self.b = b
            elif len(line) == 5:
                n, next_type_id, a, b, c = line
                next_type = parse_event(int(next_type_id))
                self.b = b
                self.c = c
            elif len(line) == 6:
                n, next_type_id, a, b, c, d = line
                next_type = parse_event(int(next_type_id))
                self.b = b
                self.c = c
                self.d = d
        self.n = int(n)  # particle ID
        self.a = a
        self.current_event = next_type
        self.current_event_id = int(next_type_id)
        self.history = []
        self.header = header

    def add(self, e):
        self.history.append(e)

    def __repr__(self):
        out = f"Event for particle {self.n} \n"
        for h in self.history:
            out += "  --------\n"
            out += str(h)
        out += "+++++++++++++++++++\n"
        return out


class Header:
    """Parses the header of a ptrace file"""

    def __init__(self, filehandle):
        self.IDS = {}
        self.program = None
        self.version = None
        self.program_date = None
        self.run_date = None
        self.run_time = None
        self.N = None
        self.N1 = None
        # assumes that the git shorthash is the last word in the name
        self.shorthash = None
        # assumes that the particle numbers is the second to last word in the namedtuple
        self.num_particles = None
        self.name = None
        self.keywords = {}

        self.parse(filehandle)

    def to_hdf(self, f):
        """Saved the information to a writeable hdf file"""

        f.attrs["program"] = self.program
        f.attrs["version"] = self.version
        f.attrs["program_date"] = self.program_date
        f.attrs["run_date"] = self.run_date
        f.attrs["run_time"] = self.run_time
        f.attrs["name"] = self.name

    def parse(self, f):
        # first line is always -1
        line = next(f)
        # program version, etc.
        line = next(f)
        form = FortranRecordReader("(a4,a5,a32,a9,a9)")
        line = form.read(line)
        line = [a.strip() for a in line]
        (
            self.program,
            self.version,
            self.program_date,
            self.run_date,
            self.run_time,
        ) = line
        # user defined name of simulations
        line = next(f)
        self.name = line.strip()
        self.shorthash = line.split()[-1]
        self.num_particles = line.split()[-2]
        # keywords for ptrac.
        # the first number,m, is the number of entries
        # followed by n1 V1_1 V1_2....V1_n1 and then repeated entries for n2...n_m
        # we need to read as many lines of 10 doubles until we reach n_m entries
        # an entry of n_i=0 means no V values
        line = next(f)
        form = FortranRecordReader("(1x,10e12.4)")
        line = form.read(line)
        m = int(line[0])
        line = line[1:]
        n_read = 0
        n = int(line[0])
        while n_read < m:
            if len(line) < n or len(line) == 0:
                # missing values, need to add next line
                newline = next(f)
                newline = form.read(newline)
                line += newline
                continue
            n_read += 1
            # remove n_i
            n = int(line[0])
            line = line[1:]
            self.keywords[KEYWORDS[n_read]] = []
            for i in range(n):
                value = float(line[0])
                line = line[1:]
                self.keywords[KEYWORDS[n_read]].append(value)
        # list of N values
        line = next(f)
        form = FortranRecordReader("(1x,20i5)")
        line = form.read(line)
        N = line
        self.N1 = N[0]
        N_src = self.N1 + N[1] + N[2]  # L_src = L[N1:N_src]
        N_bnk = N_src + N[3] + N[4]  # L_bnk = L[N_src:N_bnk]
        N_sur = N_bnk + N[5] + N[6]
        N_col = N_sur + N[7] + N[8]
        N_ter = N_col + N[9] + N[10]
        N12 = N[11]
        N13 = N[12]
        # the next block of lines needs to provide this many values
        # number of values is N_ter and will fill up necessary number of lines to achieve N_ter entries
        need = N_ter
        line = next(f)
        form = FortranRecordReader("(1x,30i4)")
        line = form.read(line)
        L = line
        got = len(L)  # Current number of values
        while got < need:
            line = next(f)
            if need - got > 30:
                p = "30"
            else:
                p = str(need - got)
            form = FortranRecordReader(f"(1x,{p}i4)")
            line = form.read(line)
            L = L + line
            got = len(L)
        # parse the ids of the events
        self.IDS["nps"] = parse_ID(L[: self.N1])
        self.IDS["initial source"] = parse_ID(L[self.N1 : N_src])
        self.IDS["bank"] = parse_ID(L[N_src:N_bnk])
        self.IDS["surface"] = parse_ID(L[N_bnk:N_sur])
        self.IDS["collision"] = parse_ID(L[N_sur:N_col])
        self.IDS["termination"] = parse_ID(L[N_col:N_ter])

    def __repr__(self):
        out = f"Program:{self.program} ; Version:({self.version} , {self.program_date}) ; Current Date:{self.run_date} {self.run_time}\n"
        out += f"{self.name}\n"
        for k, v in self.keywords.items():
            out += f"  {k} {v}\n"
        for k, v in self.IDS.items():
            out += f"   IDS: {k} {v}\n"
        return out


class HistoryHandler:
    """A default output handler class that can be used in read_file

    In principle the handler can be any function. This class with callable instances
    takes care of opening and closing files, so that the file does not need to be opened
    every time.
    """

    def __init__(self, filename):
        self.output_file = open(filename, "w")

    def __call__(self, hist):
        self.output_file.write(repr(hist))

    def close(self):
        self.output_file.close()


class HistoryHandlerKeep(HistoryHandler):
    """An output handler class that can be used in read_file

    This handler can be used to keep the history of all events.
    """

    def __init__(self):
        self.histories = []

    def __call__(self, hist):
        self.histories.append(hist)


class HistoryHandlerHeaderOnly(HistoryHandler):
    """An output handler, that only reads the header information.

    We stop handling events once we receive the first one and don't do anything with
    the event data.
    """

    def __init__(self):
        pass

    def __call__(self, hist):
        return True


def read_file(filename, handle_history=None):
    """Parses a whole PTRAC file

    This function reads in and parses all events relating to one neutron. The user can provide a
    a custom function to create any output from these events. To save memory, the event is not kept
    in memory, so the user provided function should write any information to disk that is important.

    Parameters
    ----------
    filename : str
        The filename of the ptrac file
    handle_history :
        a function that takes a History object as an argument. This hook is provided to
        have custom code executed for each history in the ptrac file.

    Returns
    -------
    header :
        Returns the heaer of the ptrac file

    """
    with open(filename) as fin:  # open for read
        header = Header(fin)
        # parse particle histories
        try:
            while True:
                line = next(fin)
                hist = History(line, header)
                while hist.current_event != "final":
                    # get two lines and add them together
                    line = next(fin)
                    form = FortranRecordReader("(1x,8e10.0)")
                    Jline = form.read(line)
                    Jline = [i for i in Jline if i is not None]
                    line = next(fin)
                    form = FortranRecordReader("(1x,9e13.5)")
                    Pline = form.read(line)
                    Pline = [i for i in Pline if i is not None]
                    event_line = Jline + Pline
                    # parse event
                    event = Event(parent=hist, line=event_line, header=header)
                    hist.add(event)
                if handle_history:
                    ret = handle_history(hist)
                    if ret:
                        raise StopIteration
                del hist
        except StopIteration:
            pass
    return header
