"""
Usage:
    MCNPtools-parse_ptrac header <filename> [options]
    MCNPtools-parse_ptrac data <filename> [options]
    MCNPtools-parse_ptrac gammas <filename> [options]
    MCNPtools-parse_ptrac neutrons <filename> [options]
    MCNPtools-parse_ptrac plot <filename> [options]
    MCNPtools-parse_ptrac plotsurfaces  <filename> [options]


Options:
   -h  --help                        This information
   -n <number>                       how many events to parse [default: 0]
   -p <prob>                         probability to skip events [default: 1.0]
   -o <output>  --output=<output>    Output file name


The following options exist
  header:             only parse the header
  data:               save all events to a file
  gammas:             creates several output files, one for each element
  neutrons:           creates several output files, one for each element
  plot:               3d plot of traces
  plotsurfaces:       3d plot of traces

<filename> is the ptrac file, which needs to be in ascii format.

The -n and -p option can be used to reduce the plotting output

"""


from docopt import docopt
import mcnptools as mt


def main():
    commands = docopt(__doc__)
    # print(commands)

    input = commands["<filename>"]
    output = commands["-o"]
    probability = float(commands["-p"])
    number = int(commands["-n"])

    if commands["header"]:
        handler = mt.ptrac.HistoryHeaderOnly()
        header, _ = mt.ptrac.read_file(input, handler)
        print(header)
        return

    if commands["data"]:
        handler = mt.ptrac.HistoryToFile(f"{input}-all-events.txt")
    elif commands["gammas"]:
        handler = mt.ptrac.HistoryGammas(input)
    elif commands["neutrons"]:
        handler = mt.ptrac.HistoryNeutrons(f"{input}-output-neutrons.txt")
    elif commands["plot"]:
        handler = mt.ptrac.HistoryHandlerPlot(number, probability)
    elif commands["plotsurfaces"]:
        handler = mt.ptrac.HistoryHandlerPlot(number, probability, plot_surfaces=True)
    else:
        handler = mt.ptrac.HistoryHandler(f"{input}-output.txt")

    mt.ptrac.read_file(input, handler, max_number=number)
    handler.close()


if __name__ == "__main__":
    main()
