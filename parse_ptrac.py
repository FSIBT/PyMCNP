#!/usr/bin/env python3

"""
Usage:
    parse_ptrac list <filename> [options]
    parse_ptrac filter <filter> <filename> [options]


Options:
   -h  --help                        This information
   -o <output>  --output=<output>    Output file name


filter can be one of:
  -gammas:     creates several output files, one for each element
  -neutrons:   creates several output files, one for each element
  -plot:       produces: [alpha_xyz, alpha_time,  neutron_xyzuvw,
                              atom/gamma_xyzuvw, detected-gamma_xyz]
  -data:       produces: (alpha_y,z [cm], alpha_time [s], atom_type,
                              atom_x,y,z [cm], gamma_time [s], gamma_energy [MeV])
"""



import sys
from docopt import docopt
from collections import namedtuple
from fortranformat import FortranRecordReader
import numpy as np
import h5py

Position = namedtuple('Position', 'x y z')
Direction = namedtuple('Direction', 'u v w') #gives the direction cosines for each axis

commands = docopt(__doc__, version="0.1")
print(commands)


input = commands['<filename>']
filter = commands['<filter>']
detector = 24
output = commands['-o']
print(input)

PARTICLE = {1: 'neutron',
            2: 'photon', }


def get_particle(nr):
    name = PARTICLE.get(nr, None)
    if name is not None:
        return name
    else:
        print("need to implement particle type {}, see page 166 in the manual".format(nr))
        return ""


KEYWORDS = {1: 'Buffer',
            2: 'Cell',
            3: 'Event',
            4: 'File',
            5: 'Filter',
            6: 'Max',
            7: 'Menp',
            8: 'NPS',
            9: 'Surface',
            10: 'Tally',
            11: 'Type',
            12: 'Value',
            13: 'Write',
            14: 'unknown'}

keywords = {v: None for k, v in KEYWORDS.items()}

types = {1: 'initial source',
         2: 'bank',
         3: 'surface',
         4: 'collision',
         5: 'termination'}

IDs = {1: 'NPS',
       2: 'first event type',
       3: 'NCL',
       4: 'NSF',
       5: 'JPTAL',
       6: 'TAL',
       7: 'next event type',
       8: 'NODE',
       9: 'NSR',
       10: 'NXS',
       11: 'NTYN/MTP',
       12: 'Surface number',
       13: 'angle with surface normal',
       14: 'termination type',
       15: 'branch number for this history',
       16: 'IPT',
       17: 'NCL',
       18: 'MAT',
       19: 'NCP',
       20: 'XXX',
       21: 'YYY',
       22: 'ZZZ',
       23: 'UUU',
       24: 'VVV',
       25: 'WWW',
       26: 'ERG',
       27: 'WGT',
       28: 'TME'}


def parse_ID(list):
    return [IDs[i] for i in list]



event_type = {1000: 'initial source',
              3000: 'surface',
              4000: 'collision',
              5000: 'termination',
              9000: 'final'}


bank_event_type = {1: ['DXTRAN Track', True],
                   2: ['Energy Split', False],
                   3: ['Weight-Window Surface Split', False],
                   4: ['Weight-Window Collision Split', True],
                   5: ['Forced Collision-Uncollided Part', False],
                   6: ['Importance Split', False],
                   7: ['Neutron from Neutron ( n , xn ) ( n , f ) and '
                       'Secondary Particles from Library Protons', True],
                   8: ['Photon from Neutron', True],
                   9: ['Photon from Double Fluorescence', True],
                   10: ['Photon from Annihilation', False],
                   11: ['Electron from Photoelectric', True],
                   12: ['Electron from Compton', True],
                   13: ['Electron from Pair Production', True],
                   14: ['Auger Electron from Photon/X-ray', True],
                   15: ['Positron from Pair Production', False],
                   16: ['Bremsstrahlung from Electron', True],
                   17: ['Knock-on Electron', False],
                   18: ['X-rays from Electron', False],
                   19: ['Photon from Neutron - Multigroup', True],
                   20: ['Neutron ( n , f ) - Multigroup', True],
                   21: ['Neutron ( n , xn ) k- Multigroup', True],
                   22: ['Photo from Photon - Multigroup', True],
                   23: ['Adjoint Weight Split - Multigroup', False],
                   24: ['Weight-Window Pseudo-Collision Split', False],
                   25: ['Secondary Particles from Photonuclear', True],
                   26: ['DXTRAN annihilation photon from pulse-height tally variance reduction', True],
                   30: ['Light Ions from Neutrons', True],
                   31: ['Light Ions from Protons', True],
                   32: ['Library Neutrons from Model Neutrons', False],
                   33: ['Secondary Particles from Inelastic Nuclear Interactions', False],
                   34: ['Secondary Particles from Elastic Nuclear Interactions', False]}



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
            return "Error ntyn lookup: shouldn't happen {}".format(idx)
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
            return "Error ntyn lookup: shouldn't happen {}".format(idx)


def lookup_mtp(idx, neutron=True):
    if neutron:
        if idx == 4:
            return "Inelastic S(alpha, beta)"
        elif idx == 2:
            return "Elastic S(alpha, beta)"
        elif idx > 0:
            return "Elastic scatter/Inelastic scatter"
        else:
            return "Error mtp lookup: shouldn't happen: {}".format(idx)
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
            return "Error mtp lookup: shouldn't happen {}".format(idx)


def parse_event(event):
    if event in event_type:
        return event_type[event]
    else:
        return 'bank'


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


termination_type = {1: 'Escape',
                    2: 'Energy cutoff',
                    3: 'Time cutoff',
                    4: 'Weight window',
                    5: 'Cell importance',
                    6: 'Weight cutoff',
                    7: 'Energy importance',
                    8: 'DXTRAN',
                    9: 'Forced collision',
                    10: 'Exponential transform'}

termination_type_neutron = {11: 'Downscattering',
                            12: 'Capture',
                            13: 'Loss to (x, xn)',
                            14: 'Loss to fission',
                            15: 'Nuclear Interactions',
                            16: 'Particle decay',
                            17: 'Tabular boundary'}

termination_type_photon = {11: ' Compton scatter',
                           12: 'Capture',
                           13: 'Pair production',
                           14: 'Photonuclear'}


def get_termination_type(idx, particle):
    if idx < 11:
        return termination_type[idx]
    if particle == 'neutron':
        return termination_type_neutron[idx]
    if particle == 'photon':
        return termination_type_photon[idx]
    else:
        return "need to implement termination type {} for {}".format(idx, particle)


class Event():
    """Save information from a single event in a particles history"""

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
        out += "  type: {}\n".format(self.event_type)
        if self.particle:
            out += "  particle type: {}\n".format(self.particle)
        if self.ntyn:
            out += "  ntyn: {}\n".format(self.ntyn)
        if self.nxs:
            out += "  nxs: {}\n".format(self.nxs)
        if self.node:
            out += "  node: {}\n".format(self.node)
        if self.pos:
            out += "  loc: {} {} {}\n".format(self.pos.x, self.pos.y, self.pos.z)
        if self.dir:
            out += "  dir: {} {} {}\n".format(self.dir.u, self.dir.v, self.dir.w)
        if self.energy:
            out += "  energy: {}\n".format(self.energy)
        if self.weight:
            out += "  weight: {}\n".format(self.weight)
        if self.time:
            out += "  time: {}\n".format(self.time)
        if self.branch_number:
            out += "  branch number: {}\n".format(self.branch_number)
        if self.surface:
            out += "  surface number: {}\n".format(self.surface)
        if self.angle:
            out += "  angle with surface normal: {}\n".format(self.angle)
        if self.cell_number:
            out += "  cell number: {}\n".format(self.cell_number)
        if self.source:
            out += "  source: {}\n".format(self.source)
        if self.material:
            out += "  material: {}\n".format(self.material)
        if self.termination_type:
            out += "  termination type: {}\n".format(self.termination_type)
        if self.misc:
            for k, v in self.misc.items():
                out += "  misc:  {} {}\n".format(k, v)
        return out

    def parse(self, hist, line):
        """Takes an input line and extracts all the information into
        this class
        """
       # convert to array of numbers
        line = [float(i) for i in line]
        d = {k: v for k, v in zip(header.IDS[hist.current_event], line)}
        if hist.current_event == 'bank':
            t, e = parse_bank(hist.current_event_id)
            d['type'] = t
            d['bank extra'] = e
        else:
            d['type'] = hist.current_event

        # sort into event class
        self.event_type = d.pop('type', None)
        self.bank_extra = d.pop('bank extra', None)
        if self.bank_extra or self.event_type == 'collision':
            self.ntyn = lookup_ntyn(int(d.pop('NTYN/MTP')))
            self.nxs = d.pop('NXS')
        self.particle = d.pop('IPT', None)
        self.source = d.pop('NSR', None)
        self.node = d.pop('NODE', None)
        self.surface = d.pop('Surface number', None)
        if self.particle:
            self.particle = get_particle(int(self.particle))
        self.cell_number = d.pop('NCL', None)
        if self.cell_number:
            self.cell_number = int(self.cell_number)
        self.material = d.pop('MAT', None)
        self.branch_number = d.pop('branch number for this history', None)
        self.angle = d.pop('angle with surface normal', None)
        self.termination_type = d.pop('termination type', None)
        if self.termination_type:
            self.termination_type = get_termination_type(self.termination_type,
                                                         self.particle)
        x = d.pop('XXX', None)
        y = d.pop('YYY', None)
        z = d.pop('ZZZ', None)
        if x is not None:
            self.pos = Position(float(x), float(y), float(z))
        u = d.pop('UUU', None)
        v = d.pop('VVV', None)
        w = d.pop('WWW', None)
        if u is not None:
            self.dir = Direction(float(u), float(v), float(w))
        self.ncp = d.pop('NCP', None)
        self.energy = d.pop('ERG', None)
        self.weight = d.pop('WGT', None)
        self.time = d.pop('TME', None)
        d.pop('next event type', None)
        self.misc = d

        # update for next event
        hist.current_event_id = int(line[0])
        hist.current_event = parse_event(hist.current_event_id)


class History():
    def __init__(self, line=None, header=None):

        if line is not None:
            n1 = str(header.N1 - 1)
            form = FortranRecordReader('(1x,{}i10,e13.5)'.format(n1))
            line = form.read(line) #NPS Line (I line)
            if len(line) == 2:
                n, next_type_id = line
                next_type = parse_event(int(next_type_id))
            elif len(line) == 3:
                n, next_type_id, a = line
                next_type = parse_event(int(next_type_id))
            elif len(line) == 4:
                n, next_type_id, a, b = line
                next_type = parse_event(int(next_type_id))
            elif len(line) == 5:
                n, next_type_id, a, b, c = line
                next_type = parse_event(int(next_type_id))
                self.c = c
            elif len(line) == 6:
                n, next_type_id, a, b, c, d = line
                next_type = parse_event(int(next_type_id))
                self.c = c
                self.d = d
        self.n = int(n) #particle ID
        self.a = a
        self.b = b
        self.current_event = next_type
        self.current_event_id = int(next_type_id)
        self.history = []

    def add(self, e):
        self.history.append(e)

    def __repr__(self):
        out = "Event for particle {} \n".format(self.n)
        for h in self.history:
            out += "  --------\n"
            out += str(h)
        out += "+++++++++++++++++++\n"
        return out


def handle_history(hist):
    """default handler for history events

    overwrite this function to sort events
    """
    sys.stdout.flush()


class Header():
    def __init__(self):
        self.IDs = {}
        self.program = None
        self.version = None
        self.program_date = None
        self.run_date = None
        self.run_time = None
        self.N = None
        self.N1 = None
        self.shorthash = None
        self.num_particles = None

    def parse(self, f):
        # first line is always -1
        line = next(f)
        # program version, etc.
        line = next(f)
        form = FortranRecordReader('(a4,a5,a32,a9,a9)')
        line = form.read(line)
        line = [a.strip() for a in line]
        self.program, self.version, self.program_date, self.run_date, self.run_time = line
        """self.program, self.version, self.program_date, self.run_date,
        self.run_time = self.program.strip(), self.version.strip(), self.program_date.strip(),
        self.run_date.strip(), self.run_time.strip() """
        # user defined name of simulations
        line = next(f)
        self.name = line
        self.shorthash = line.split()[-1]
        self.num_particles = line.split()[-2]
        # 3 lines of keyword values
        line = next(f)
        form = FortranRecordReader('(1x,10e12.4)')
        line = form.read(line)
        K = line
        line = next(f)
        form = FortranRecordReader('(1x,10e12.4)')
        line = form.read(line)
        K = K + line
        line = next(f)
        form = FortranRecordReader('(1x,10e12.4)')
        line = form.read(line)
        K = K + line
        #K meaning:
        # [m(number of n_m) n_1 V1_1 V1_2.....V1_n n_2 V2_1 V2_2..... n_m Vn_1 Vn_2.... Vn_m]
        # n is the index of KEYWORDS
        # Vn_m is the value
        j = 0
        idx = 0
        while idx < K[0]:
            j += 1
            idx += 1
            n = int(K[j])
            keywords[KEYWORDS[idx]] = K[j+1:j+1+n] or None
            j += n
        # list of N values
        line = next(f)
        form = FortranRecordReader('(1x,20i5)')
        line = form.read(line)
        N = line
        self.N1 = N[0]
        N_src = self.N1 + N[1]+N[2] #L_src = L[N1:N_src]
        N_bnk = N_src + N[3]+N[4] #L_bnk = L[N_src:N_bnk]
        N_sur = N_bnk + N[5]+N[6]
        N_col = N_sur + N[7]+N[8]
        N_ter = N_col + N[9]+N[10]
        N12 = N[11]
        N13 = N[12]
        # the next block of lines needs to provide this many values
        need = N_ter #number of values is N_ter and will fill up necessary number of lines to achieve N_ter entries
        line = next(f)
        form = FortranRecordReader('(1x,30i4)')
        line = form.read(line)
        L = line
        got = len(L) #Current number of values
        while got < need:
            line = next(f)
            if need-got > 30:
                p = '30'
            else:
                p = str(need-got)
            form = FortranRecordReader('(1x,{}i4)'.format(p))
            line = form.read(line)
            L = L + line
            got = len(L)
        self.IDS = {}
        self.IDS['nps'] = parse_ID(L[:self.N1]) #list of Variables for the NPS line
        self.IDS['initial source'] = parse_ID(L[self.N1:N_src]) #list of variable IDs for an src event
        self.IDS['bank'] = parse_ID(L[N_src:N_bnk]) #list of variable IDs for an bank event
        self.IDS['surface'] = parse_ID(L[N_bnk:N_sur]) #list of variable IDs for an sur event
        self.IDS['collision'] = parse_ID(L[N_sur:N_col]) #list of variable IDs for an col event
        self.IDS['termination'] = parse_ID(L[N_col:N_ter]) #list of variable IDs for an ter event

    def __repr__(self):
        out = ""
        out += "Program:{} ; Version:({} , {}) ; Current Date:{} {}\n".format(self.program,
                                                                              self.version,
                                                                              self.program_date,
                                                                              self.run_date,
                                                                              self.run_time)
        out += "{}\n".format(self.name)
        for k, v in keywords.items():
            if v:
                out += "  {} {}\n".format(k, v)
        for k, v in self.IDS.items():
            out += "   IDS: {} {}\n".format(k, v)
        return out


class alpha():
    '''Calcualte and store the position of an alpha particle from a neutron event'''
    def __init__(self, event):
        '''Calculate alpha position and time'''

        #alpha starts same place as neutron
        xi = event.pos.x
        yi = event.pos.y
        zi = event.pos.z
        #alpha trajectory opposite of neutron
        ui = -event.dir.u
        vi = -event.dir.v
        wi = -event.dir.w

        #energy and velocity calculation
        MeV = 3.5 #MeV of neutrons
        energy = MeV * 1.602E-19 * 1E6 #Joules
        mass = 6.64424E-27 #kg
        velocity = np.sqrt((2*energy)/mass)*100 #cm/s

        #alpha detector
        az = -6 #distance from neutron source to alpha detector
        R = abs(az/wi) #total travel distance

        #location and time of detection
        self.ay = vi*R
        self.ax = ui*R
        self.atime = R/velocity

    def __repr__(self):
        return '{} {} {}'.format(self.ax, self.ay, self.atime)


def read_file(filename):
    """ """
    global header
    header = Header()
    with open(filename, 'r') as fin: #open for read
        header.parse(fin)
        # parse particle histories
        try:
            while True:
                line = next(fin)
                # read first nps entry in history
                #print("in read_file", line)
                hist = History(line, header)
                while hist.current_event != 'final':
                    # get two lines and add them together
                    line = next(fin)
                    form = FortranRecordReader('(1x,8e10.0)')
                    Jline = form.read(line)
                    Jline = [i for i in Jline if i is not None]
                    line = next(fin)
                    form = FortranRecordReader('(1x,9e13.5)')
                    Pline = form.read(line)
                    Pline = [i for i in Pline if i is not None]
                    event_line = Jline +  Pline
                    # parse event
                    event = Event(parent=hist, line=event_line, header=header)
                    hist.add(event)
                handle_history(hist)
                del hist
        except StopIteration:
            pass

if __name__ == "__main__":
    if output:
        outfiles = {}
        outfiles1 = {}
        def handle_history(hist):

            global outfiles
            if filter == 'gammas':
                for h in hist.history:
                    if h.event_type == 'Photon from Neutron':
                        element = str(h.nxs)
                        outf = outfiles.get(element, None)
                        if not outf:
                            outf = open("{}-output-{}".format(commands['<filename>'], element)+".txt", 'w')
                            outfiles[element] = outf
                        outf.write("{} {} {} {} {} {} {} {} {}\n".format(h.pos.x, h.pos.y,
                                                                         h.pos.z, h.dir.u, h.dir.v, h.dir.w, h.energy, h.weight, h.time))

            elif filter == 'plot':
                filename = "{}-output-plot".format(commands['<filename>'])+".txt"
                if outfiles.get(filename, None) is None:
                    outf = open(filename, 'w')
                    outfiles[filename] = outf
                else:
                    outf = outfiles[filename]
                condition = True
                idx = 0
                for h in hist.history:
                    idx += 1
                    if h.event_type == 'initial source':
                        #neutron position and directions
                        neutron = '{} {} {} {} {} {}'.format(h.pos.x, h.pos.y, h.pos.z, h.dir.u, h.dir.v, h.dir.w)
                        a = alpha(h) #prints ay, az, atime
                    if h.event_type == 'Photon from Neutron': #get atom info
                        atom = ('{} {} {} {} {} {} {}'.format(h.pos.x, h.pos.y, h.pos.z, h.dir.u, h.dir.v, h.dir.w, h.nxs))
                    if condition is True: #get photon info and print
                        if h.event_type == 'surface' and h.particle == 'photon' and h.surface >= 114.0 and h.surface < 115.0:
                            outf.write("{} -6 {} {} {} {} {}\n".format(a, neutron, atom, h.pos.x, h.pos.y, h.pos.z))
                            condition = False
                    if h.event_type != 'surface' or h.surface < 114.0:
                        condition = True

            elif filter == 'data':
                filename = "{}-output-data".format(commands['<filename>'])
                global data_array
                global repeat_gammas
                if outfiles1.get(filename, None) is None:
                    #outf = open(filename+".txt", 'w')
                    #outfiles[filename] = outf
                    outfiles1[filename] = 'placeholder'
                    data_array = np.empty((0, 12), float)
                    repeat_gammas = 0
                    #print(repeat_gammas)
                    #print('outside',data_array)
                else:
                    outf = outfiles1[filename]
                condition = True
                check = 0
                for h in hist.history:
                    if h.event_type == 'initial source':
                        #neutron position and directions
                        a = alpha(h) #prints ay, az, atime
                        a_num = [a.ax, a.ay, a.atime]
                    if h.event_type == 'Photon from Neutron': #get atom info
                        atom = '{} {} {} {}'.format(h.nxs, h.pos.x, h.pos.y, h.pos.z) #string for txt file
                        atom_number = [h.nxs, h.pos.x, h.pos.y, h.pos.z] #array for numpy file
                    if condition is True: #skip double detector hits (two sides to detector surface)
                        #get photon info and print
                        if h.event_type == 'surface' and h.particle == 'photon' and h.surface >= detector and h.surface < (detector+1):
                            gamma_time = h.time*10**(-8)
                            #outf.write("{} {} {} {}\n".format(a, atom, gamma_time, h.energy))
                            x = [a_num[0], a_num[1], a_num[2], atom_number[0], atom_number[1], atom_number[2], atom_number[3], gamma_time, h.energy, h.pos.x, h.pos.y, h.pos.z]
                            data_array = np.append(data_array, [x], axis=0)
                            with h5py.File(filename+ '-' + header.shorthash + '_numpart-' + header.num_particles + '.hdf5', 'w') as f:
                                #all_data = f.create_dataset('all_data', data=data_array, dtype='f')
                                alpha_x = f.create_dataset('alpha_x[cm]', data=data_array[:, 0], dtype='float64')
                                alpha_y = f.create_dataset('alpha_y[cm]', data=data_array[:, 1], dtype='float64')
                                alpha_t = f.create_dataset('alpha_t[s]', data=data_array[:, 2], dtype='float64')
                                atom_type = f.create_dataset('atom_type', data=data_array[:, 3], dtype='i')
                                atom_x = f.create_dataset('atom_x[cm]', data=data_array[:, 4], dtype='float64')
                                atom_y = f.create_dataset('atom_y[cm]', data=data_array[:, 5], dtype='float64')
                                atom_z = f.create_dataset('atom_z[cm]', data=data_array[:, 6], dtype='float64')
                                gamma_t = f.create_dataset('gamma_t[s]', data=data_array[:, 7], dtype='float64')
                                gamma_e = f.create_dataset('gamma_e[MeV]', data=data_array[:, 8], dtype='float64')
                                gamma_x = f.create_dataset('gamma_x[cm]', data=data_array[:, 9], dtype='float64')
                                gamma_y = f.create_dataset('gamma_y[cm]', data=data_array[:, 10], dtype='float64')
                                gamma_z = f.create_dataset('gamma_z[cm]', data=data_array[:, 11], dtype='float64')
                            condition = False #omit consecutive detector events
                            check += 1 #adds one gamma for this history
                        if check > 1 and h.event_type == 'surface' and h.particle == 'photon' and h.surface >= detector and h.surface < (detector+1):
                            #check for repeat gammas
                            repeat_gammas += 1
                            print('number of repeat gamma', repeat_gammas)
                    if h.event_type != 'surface' or h.surface < detector:
                        condition = True

            elif filter == 'neutrons':
                filename = "{}-output-neutrons".format(commands['<filename>'])+".txt"
                if outfiles.get(filename, None) is None:
                    outf = open(filename, 'w')
                    outfiles[filename] = outf
                else:
                    outf = outfiles[filename]
                idx = 0
                for h in hist.history:
                    if h.event_type == 'initial source' and h.particle == 'neutron':
                        outf.write('source NA {} {} {} {} {} {} NA\n'.format(h.pos.x, h.pos.y, h.pos.z, h.dir.u, h.dir.v, h.dir.w, h.energy))
                    if h.event_type == 'Photon from Neutron':
                        outf.write('photon {} {} {} {} {} {} {} {}\n'.format(h.pos.x, h.pos.y, h.pos.z, h.dir.u, h.dir.v, h.dir.w, h.energy, h.nxs))
                    if h.event_type == 'collision' and h.energy>0.001 and h.particle == 'neutron':
                        outf.write('collision {} {} {} {} {} {} {} {}\n'.format(h.pos.x, h.pos.y, h.pos.z, h.dir.u, h.dir.v, h.dir.w, h.energy, h.nxs))
                    if not outf:
                        	outf = open("{}-output-ncol".format(commands['<filename>'])+".txt", 'w')
                        	outfiles[element] = outf
                
            else:
                outf = outfiles.get('misc', None)
                if not outf:
                    outf = open("{}-output".format(commands['<filename>'])+".txt", 'w')
                    outfiles['misc'] = outf
                outf.write(hist.__repr__())

        read_file(input)

        for k, f in outfiles.items():
            f.close()
    else:
        read_file(input)
        print(header)