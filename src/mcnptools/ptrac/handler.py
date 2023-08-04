"""Classes to get certain information out of a parsed ptrac history.

These are to be used with the read_file function in parse_ptrac.py.

In principle the historyhandler can just be a function that takes a
single history event.  However, in practise it is often better to use
a class, that can keep some state (for example open and close files to
write output to).

If the function/class returns a True value, the parsing of events will stop.

The following handlers currently exist:

HistoryHandler:     Create a list of events and return on close
HistoryToFile:      Save every event into an output file
HistoryHeaderOnly:  Only parse the header and then stop
"""

from matplotlib import pyplot as plt


class HistoryHandler:
    """A default output handler class that can be used in read_file

    In principle the handler can be any function. This class with callable instances
    takes care of opening and closing files, so that the file does not need to be opened
    every time.
    """

    def __init__(self):
        self.data = []

    def __call__(self, hist):
        self.data.append(hist)

    def close(self):
        return self.data


class HistoryToFile(HistoryHandler):
    """Write every event to a file."""

    def __init__(self, filename):
        self.output_file = open(filename, "w")

    def __call__(self, hist):
        self.output_file.write(str(hist))

    def close(self):
        self.output_file.close()


class HistoryHeaderOnly(HistoryHandler):
    """Only parse the header and then stop."""

    def __init__(self):
        pass

    def __call__(self, hist):
        return True

    def close(self):
        pass


class HistoryGammas(HistoryHandler):
    """Create several output files for each element in the target.

    This handler will only write out 'Photon from Neutron' events and
    save them in multiple files, sorted by the element the photon
    originates from.

    """

    def __init__(self, input):
        self.input = input
        self.output_files = {}
        self.header_info = None  # str naming all the columns in the output file

    def __call__(self, hist):
        for h in hist.history:
            if h.event_type == "Photon from Neutron" and not h.rejected:
                element = str(h.nxs)
                outf = self.get_or_create_output_file(element, h)
                outf.write(h.to_value_str())

    def get_or_create_output_file(self, element: str, h):
        outf = self.output_files.get(element, None)
        if outf is None:
            outf = open(f"{self.input}-output-{element}.txt", "w")
            self.output_files[element] = outf
            outf.write(h.to_header_str())
        return outf

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


class HistoryHandlerNeutrons(HistoryHandler):
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
