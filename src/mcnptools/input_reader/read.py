from pathlib import Path
from textwrap import wrap


from .file_parser import parse_file
from ..objects import Cell, Surface, Material, Data, Nps


class Input:
    def __init__(self, filename: Path):
        self.lines = parse_file(filename)

        self.message = self.lines["message"]
        self.title = self.lines["title"]
        self.cells = [Cell.from_mcnp(c) for c in self.lines["cells"]]
        self.surfaces = [Surface.from_mcnp(c) for c in self.lines["surfaces"]]
        self.materials = [Material.from_mcnp(c) for c in self.lines["materials"]]
        self.data = [Data.from_mcnp(c) for c in self.lines["data"]]

    def to_mcnp(self):
        if self.message:
            out = self.message + "\n"
            out += self.title + "\n"
        else:
            out = self.title + "\n"

        for x in [self.cells, None, self.surfaces, None, self.materials, self.data]:
            if x is None:
                out += "\n"
            else:
                for y in x:
                    out += y.to_mcnp()

        # wrap the text
        out = out.split("\n")
        out = ["\n".join(wrap(x, width=80, subsequent_indent="     ")) for x in out]
        out = "\n".join(out) + "\n"

        return out

    @property
    def nps(self):
        """Convenient function to get the number of particles."""
        for d in self.data:
            if isinstance(d, Nps):
                return d.number

    @nps.setter
    def nps(self, value):
        """Convenient function to set the number of particles."""
        for d in self.data:
            if isinstance(d, Nps):
                d.number = value

    def __str__(self):
        out = ""
        for x in [self.cells, self.surfaces, self.materials, self.data]:
            for y in x:
                out += str(y)
        return out
