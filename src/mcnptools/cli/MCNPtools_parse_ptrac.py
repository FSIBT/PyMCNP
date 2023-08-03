"""
Usage:
    MCNPtools-parse_ptrac filter <filter> <filename> [options]


Options:
   -h  --help                        This information
   -n <number>                       how many events to parse [default: 0]
   -p <prob>                         probability to skip events [default: 1.0]
   -o <output>  --output=<output>    Output file name


filter can be one of:
  gammas:     creates several output files, one for each element
  neutrons:   creates several output files, one for each element
  plot:               3d plot of traces
  plotsurfaces:       3d plot of traces

The -n and -p option can be used to reduce the plotting output

"""


from docopt import docopt
from collections import defaultdict
import numpy as np
import mcnptools
import matplotlib.pyplot as plt


class HistoryHandlerGammas:
    def __init__(self, input):
        self.input = input
        self.output_files = {}

    def __call__(self, hist):
        for h in hist.history:
            if h.event_type == "Photon from Neutron":
                element = str(h.nxs)
                outf = self.output_files.get(element, None)
                if not outf:
                    outf = open(f"{self.input}-output-{element}.txt", "w")
                    self.output_files[element] = outf
                outf.write(
                    f"{h.pos.x} {h.pos.y} {h.pos.z} {h.dir.u} {h.dir.v} {h.dir.w} {h.energy} {h.weight} {h.time}\n"
                )

    def close(self):
        for f in self.output_files.values():
            f.close()


class HistoryHandlerPlot:
    def __init__(self, number, probability, plot_surfaces=False):
        self.number = number
        self.probability = probability
        self.plot_surfaces = plot_surfaces
        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        self.node = 1
        self.colors = {"neutron": "red", "photon": "blue"}
        self.lineX = []
        self.lineY = []
        self.lineZ = []
        self.scatterX = []
        self.scatterY = []
        self.scatterZ = []
        self.surfaceX = defaultdict(list)
        self.surfaceY = defaultdict(list)
        self.surfaceZ = defaultdict(list)
        self.counter = 0

    def plot(self):
        self.counter += 1
        if not self.plot_surfaces:
            self.ax.plot(
                self.lineX, self.lineY, self.lineZ, color=self.colors[self.particle]
            )
        self.lineX = []
        self.lineY = []
        self.lineZ = []

    def __call__(self, hist):
        if self.number:
            if self.counter > self.number:
                return True
        if np.random.random() > self.probability:
            # skip this history
            return

        for h in hist.history:
            if h.node and (h.node < self.node):
                self.plot()
                self.particle = h.particle
            if h.event_type == "initial source":
                self.node = h.node
                self.particle = h.particle
                self.lineX.append(h.pos.x)
                self.lineY.append(h.pos.y)
                self.lineZ.append(h.pos.z)
            elif h.event_type == "collision":
                self.node = h.node
                self.lineX.append(h.pos.x)
                self.lineY.append(h.pos.y)
                self.lineZ.append(h.pos.z)
                self.scatterX.append(h.pos.x)
                self.scatterY.append(h.pos.y)
                self.scatterZ.append(h.pos.z)
            elif h.event_type == "surface":
                self.node = h.node
                self.lineX.append(h.pos.x)
                self.lineY.append(h.pos.y)
                self.lineZ.append(h.pos.z)
                s = int(h.surface)
                self.surfaceX[s].append(h.pos.x)
                self.surfaceY[s].append(h.pos.y)
                self.surfaceZ[s].append(h.pos.z)
            elif h.event_type == "Photon from Neutron":
                self.node = h.node
                self.lineX.append(h.pos.x)
                self.lineY.append(h.pos.y)
                self.lineZ.append(h.pos.z)
        self.plot()

    def close(self):
        if self.plot_surfaces:
            for s in self.surfaceX:
                self.ax.scatter(self.surfaceX[s], self.surfaceY[s], self.surfaceZ[s])
        else:
            self.ax.scatter(self.scatterX, self.scatterY, self.scatterZ, color="green")
        plt.show()


class HistoryHandlerNeutrons(mcnptools.parse_ptrac.HistoryHandler):
    def __call__(self, hist):
        for h in hist.history:
            if h.event_type == "initial source" and h.particle == "neutron":
                self.output_file.write(
                    f"source NA {h.pos.x} {h.pos.y} {h.pos.z} {h.dir.u} {h.dir.v} {h.dir.w} {h.energy} NA\n"
                )
            if h.event_type == "Photon from Neutron":
                self.output_file.write(
                    f"photon {h.pos.x} {h.pos.y} {h.pos.z} {h.dir.u} {h.dir.v} {h.dir.w} {h.energy} {h.nxs}\n"
                )
                if (
                    h.event_type == "collision"
                    and h.energy > 0.001
                    and h.particle == "neutron"
                ):
                    self.output_file.write(
                        f"collision {h.pos.x} {h.pos.y} {h.pos.z} {h.dir.u} {h.dir.v} {h.dir.w} {h.energy} {h.nxs}"
                    )


def main():
    commands = docopt(__doc__)
    # print(commands)

    input = commands["<filename>"]
    filter = commands["<filter>"]
    output = commands["-o"]
    probability = float(commands["-p"])
    number = int(commands["-n"])

    if output:
        if filter == "gammas":
            handler = HistoryHandlerGammas(input)
        elif filter == "neutrons":
            handler = HistoryHandlerNeutrons(f"{input}-output-neutrons.txt")
        elif filter == "plot":
            handler = HistoryHandlerPlot(number, probability)
        elif filter == "plotsurfaces":
            handler = HistoryHandlerPlot(number, probability, plot_surfaces=True)
        else:
            handler = mcnptools.parse_ptrac.HistoryHandler(f"{input}-output.txt")

        mcnptools.parse_ptrac.read_file(input, handler)
        handler.close()

    else:
        header = mcnptools.parse_ptrac.read_file(input)
        print(header)


if __name__ == "__main__":
    main()
