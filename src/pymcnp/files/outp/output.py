"""
Read MCNP Output files
"""

from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.interpolate import griddata as gd


class ReadOutput:
    def __init__(self, filename):
        self.filename = Path(filename)
        self.df_info = 0
        self.all_lines = self.read_entire_file()
        self.get_tally_info()

    def read_entire_file(self):
        return self.filename.read_text().split('\n')

    def read_tally(self, n=0):
        s = self.df_info['line_start'][n]
        e = self.df_info['line_end'][n]
        corpus = self.all_lines[s:e]
        corpus_np = np.array([x.split() for x in corpus], dtype=float)
        df = pd.DataFrame(columns=['energy', 'cts', 'error'], data=corpus_np)
        return df

    def old_read_tally(self, n=0, tally_type='e'):
        start = -1
        if tally_type == 'e':
            key_word = 'energy'
        start_line = list(self.df_info['line_number'])[n]

        for i, line in enumerate(self.all_lines[start_line:]):
            words = line.split()
            if key_word in words:
                start = start_line + i
            if 'total' in words and start != -1:
                end = start_line + i
                break
        corpus = self.all_lines[start + 1 : end]
        corpus_np = np.array([x.split() for x in corpus], dtype=float)
        df = pd.DataFrame(columns=['energy', 'cts', 'error'], data=corpus_np)
        return df

    def get_runtime(self):
        # in development
        outp = self.filename.read_text().split('\n')

        time1 = ''
        time2 = ''
        for line in outp:
            if 'mcnp' in line and 'version 6' in line and 'probid' in line:
                string = line.replace('     ', ' ').split(' ')
                time1 = string[10]
                time2 = string[19]
            if 'computer' in line and 'time' in line:
                cpt = line

        datetime2 = datetime.strptime(time2, '%H:%M:%S')
        datetime1 = datetime.strptime(time1, '%H:%M:%S')
        diff = datetime1 - datetime2
        # real_time = "real time: " + time.strftime("%H:%M:%S", time.gmtime(diff.seconds))
        real_time = f'real time: {round(diff.seconds/60,1)} minutes'
        computer_time = cpt[1:]
        return real_time, computer_time

    def get_nps(self):
        print('Reading output file...')
        nps = 0
        with self.filename.open() as myfile:
            for i, line in enumerate(myfile):
                tmp = line.split()
                if 'run' in tmp and 'terminated' in tmp:
                    nps = tmp[3]
                    print(tmp)
                    break
        print('Done reading')
        print(f'Number of simulated particles: {nps}')
        return nps

    def read_table110(self):
        """
        Reads in Table 110 from MCNP output files. This table is printed only if
        the keyword 'print' or 'print 110' is explicitly written in the input file.
        Table 110 prints the first 50 starting histories
        """
        allf = self.all_lines
        start = -1
        for i, line in enumerate(allf):
            words = line.lower().split()
            if 'print' in words and 'table' in words and '110' in words:
                start = i
            if 'nps' in words and start != -1:
                col_line = i
                break
        col_names = allf[col_line].split()
        corpus = allf[col_line + 2 : col_line + 2 + 50]
        corpus_np = np.array([x.split() for x in corpus], dtype=float)
        df = pd.DataFrame(columns=col_names, data=corpus_np)
        return df

    @staticmethod
    def parse_tally_info(lst):
        """
        Parse a list of strings for tally information
        """
        nps, tally_type, tally_name, description, particle = 0, 0, 0, 0, 0
        other = []
        for line in lst:
            tmp = line.split()
            if len(tmp) == 0:
                continue
            if '1tally' in tmp and 'nps' in tmp and len(tmp) >= 5:
                tally_name = f'F{tmp[1]}'
                nps = int(tmp[-1])
            elif 'tally' in tmp and 'type' in tmp:
                tally_type = f'F{tmp[2]}'
                description = ' '.join(tmp[3:])
            elif 'particle(s):' in tmp and len(tmp) > 1:
                particle = ' '.join(tmp[1:])
            else:
                other.append(' '.join(tmp))
        other_info = ' |***| '.join(other)
        dic = {
            'nps': nps,
            'tally_type': tally_type,
            'tally_name': tally_name,
            'description': description,
            'particle': particle,
            'other': other_info,
        }
        return dic

    def get_tally_info(self):
        blank_idx, erg_idx, time_idx, total_idx = [], [], [], []
        print('Reading output file...')
        for i, line in enumerate(self.all_lines):
            tmp = line.split()
            if len(tmp) == 0:
                blank_idx.append(i)
            if 'energy' in tmp and len(tmp) == 1:
                erg_idx.append(i)
            if 'time' in tmp and len(tmp) == 1:
                time_idx.append(i)
            if 'total' in tmp and len(tmp) == 3 and (len(erg_idx) > 0 or len(time_idx) > 0):
                total_idx.append(i)
        ky_idx = sorted(total_idx + erg_idx + time_idx)  # keyword indices
        ky_idx = np.array(ky_idx).reshape(-1, 2)
        ky_idx[:, 0] = ky_idx[:, 0] + 1  # remove keyword header
        blank_idx = np.array(blank_idx)
        # find tally and subtally info indices by looking at blank spaces
        # before the keywords
        tly_info_idx = []
        lines_before_tly = 10  # look for empty lines before tally
        for x in ky_idx:  # this won't work for short tallies
            tly_info_idx.append(
                blank_idx[(blank_idx < x[0]) & (blank_idx > x[0] - lines_before_tly)].min()
            )
        tly_info_idx = np.array(tly_info_idx) + 1

        # initialize dataframe
        cols = [
            'tally_name',
            'tally_type',
            'particle',
            'line_start',
            'line_end',
            'description',
            'nps',
            'other',
        ]
        df = pd.DataFrame(columns=cols)

        for info, data in zip(tly_info_idx, ky_idx):
            info_start = info
            info_end = data[0] - 1
            data_start = data[0]
            data_end = data[1]
            info_lst = self.all_lines[info_start:info_end]
            info_dict = self.parse_tally_info(info_lst)
            info_dict['line_start'] = data_start
            info_dict['line_end'] = data_end
            df.loc[len(df)] = info_dict
        print('--' * 20)
        print(f'Number of tallies and/or subtallies found: {df.shape[0]}')
        print('--' * 20)
        self.df_info = df

    def old_get_tally_info(self):
        lidx, pidx, ix_angle = [], [], []
        surf, tagix, uncol = [], [], []
        tally_type, particle, surface = [], [], []
        uncollided, user_bin, l_angle = [], [], []

        print('Reading output file...')
        for i, line in enumerate(self.all_lines):
            tmp = line.split()
            if 'tally' in tmp and 'type' in tmp:
                lidx.append(i)
                tally_type.append(line)
            if 'particle(s):' in tmp:
                pidx.append(i)
                particle.append(tmp)
            if 'surface' in tmp and len(tmp) == 2 and len(lidx) > 0 and i >= min(lidx):
                surf.append(i)
                surface.append(tmp)
            if 'angle' in tmp and 'bin:' in tmp:
                l_angle.append(tmp)
                ix_angle.append(i)
            if 'uncollided' in tmp and 'flux' in tmp:
                uncol.append(i)
                uncollided.append(line)
            if 'user' in tmp and 'bin' in tmp:
                tagix.append(i)
                user_bin.append(line.split()[-1])
        print('Done reading')
        if len(surface) > 0 and len(user_bin) > 0:
            tot_subtly = len(user_bin)
        else:
            tot_subtly = len(surface) + len(uncollided) + len(user_bin)
        print('--' * 20)
        print(f'Number of tallies: {len(lidx)}')
        print(f'Number of subtallies: {tot_subtly}')
        print('--' * 20)
        ttype = tally_type[0].split()

        # initialize dataframe
        cols = [
            'tally_type',
            'description',
            'particle',
            'surfaces',
            'angle_bin',
            'flux',
            'user_bin',
            'line_number',
        ]
        df = pd.DataFrame(columns=cols)
        sur, ang, unc, ub = 0, 0, 0, 0
        if len(surface) > 0 and len(user_bin) == 0:
            if len(ix_angle) == 0:
                sur = surface
                for ix, s in zip(surf, sur):
                    dat0 = [
                        'F' + ttype[2],
                        ' '.join(ttype[3:]),
                        particle[0][1],
                        s[1],
                        ang,
                        unc,
                        ub,
                        ix,
                    ]
                    ser0 = pd.Series(dat0, index=df.columns)
                    df.loc[len(df)] = ser0
            else:
                ang = l_angle
                sur = surface
                for ix, s, a in zip(surf, sur, ang):
                    dat0 = [
                        'F' + ttype[2],
                        ' '.join(ttype[3:]),
                        particle[0][1],
                        s[1],
                        ' '.join(a[2:]),
                        unc,
                        ub,
                        ix,
                    ]
                    ser0 = pd.Series(dat0, index=df.columns)
                    df.loc[len(df)] = ser0

        if len(uncollided) > 0:
            uncol_idx = uncol
            flux = 'collided flux'
            unc = uncollided
            for line, p in zip(lidx, particle):
                dat0 = [
                    'F' + ttype[2],
                    ' '.join(ttype[3:]),
                    p[1],
                    sur,
                    ang,
                    flux,
                    ub,
                    line,
                ]
                ser0 = pd.Series(dat0, index=df.columns)
                df.loc[len(df)] = ser0
            for line, ix, p in zip(unc, uncol_idx, particle):
                dat0 = [
                    'F' + ttype[2],
                    ' '.join(ttype[3:]),
                    p[1],
                    sur,
                    ang,
                    line[1:],
                    ub,
                    ix,
                ]
                ser0 = pd.Series(dat0, index=df.columns)
                df.loc[len(df)] = ser0
        if len(user_bin) > 0 and len(surface) == 0:
            ub = user_bin
            for line, ix in zip(ub, tagix):
                dat0 = [
                    'F' + ttype[2],
                    ' '.join(ttype[3:]),
                    particle[0][1],
                    sur,
                    ang,
                    unc,
                    line,
                    ix,
                ]
                ser0 = pd.Series(dat0, index=df.columns)
                df.loc[len(df)] = ser0

        # work in progress
        if len(surface) > 0 and len(ix_angle) > 0 and len(user_bin) > 0:
            ang = l_angle
            sur = surface
            ub = user_bin
            for ix, s, a, line in zip(surf, sur, ang, ub):
                dat0 = [
                    'F' + ttype[2],
                    ' '.join(ttype[3:]),
                    particle[0][1],
                    s[1],
                    ' '.join(a[2:]),
                    unc,
                    line,
                    ix,
                ]
                ser0 = pd.Series(dat0, index=df.columns)
                df.loc[len(df)] = ser0

        if tot_subtly == 0:
            for n in lidx:
                dat0 = [
                    'F' + ttype[2],
                    ' '.join(ttype[3:]),
                    particle[0][1],
                    sur,
                    ang,
                    unc,
                    ub,
                    n,
                ]
                ser0 = pd.Series(dat0, index=df.columns)
                df.loc[len(df)] = ser0

        # drop all zero columns
        df = df.loc[:, (df != 0).any(axis=0)]
        self.df_info = df


# This function should be implemented separately under the ptrac reader
def read_ptrac_surf(files, surfaces=['5.1', '5.2', '5.3'], event_types=['3000', '9000']):
    # surface crossing event (3000) and last event for given history (9000)
    det = []
    det_info = []
    for file in files:
        elem_det = []
        idx_det = []
        with open(file) as f:
            # file = f.readlines()
            for i, line in enumerate(f):
                words = line.split()
                if words[0] in event_types and words[2] in surfaces:
                    idx_det.append(i)
                    elem_det.append(words[2])

        with open(file) as f:
            file = f.readlines()

        for d in idx_det:
            tmp = np.array(file[d + 1].split(), dtype=float)
            info = np.array(file[d].split(), dtype=float)
            if len(info) == 8:
                det_info.append(info)
            if len(tmp) == 9:
                det.append(tmp)

    cols_i = ['event', 'node', 'ZA', 'MTP', 'particle', 'cell', 'material', 'ncp']
    df_i = pd.DataFrame(data=det_info, columns=cols_i)
    cols = ['x', 'y', 'z', 'u', 'v', 'w', 'energy', 'wgt', 'tme']
    df = pd.DataFrame(data=det, columns=cols)

    df['tme'] = df['tme'] * 10  # ns
    return df_i, df


class ReadFmesh:
    def __init__(self, filename):
        self.filename = Path(filename)
        self.all_lines = self.read_entire_file()
        self.data_idx = 0  # start data index
        self.df_info = self.read_tally_info()

    def read_entire_file(self):
        return self.filename.read_text().split('\n')

    @staticmethod
    def numpy_fillna(data):
        # Get lengths of each row of data
        lens = np.array([len(i) for i in data])
        # Mask of valid places in each row
        mask = np.arange(lens.max()) < lens[:, None]
        # Setup output array and put elements from data into masked positions
        out = np.zeros(mask.shape, dtype=data.dtype)
        out[mask] = np.concatenate(data)
        return out

    def read_tally_info(self):
        e0 = np.array([0])
        t0 = np.array([0])
        totals = []
        for i, line in enumerate(self.all_lines):
            tmp = line.split()
            if ('X direction') in line:
                x0 = np.asarray(tmp[2:], dtype=float)
            if ('Y direction') in line:
                y0 = np.asarray(tmp[2:], dtype=float)
            if ('Z direction') in line:
                z0 = np.asarray(tmp[2:], dtype=float)
            if ('Energy bin boundaries') in line:
                e0 = np.asarray(tmp[3:], dtype=float)
            if ('Time bin boundaries') in line:
                t0 = np.asarray(tmp[3:], dtype=float)
            if 'Result' in tmp and 'Error' in tmp:
                self.data_idx = i
            if 'Total' in tmp:
                totals.append(i)
        data_info = [e0, t0, x0, y0, z0]
        info_np = np.array(data_info, dtype=object)
        info_np = self.numpy_fillna(info_np)
        df_info = pd.DataFrame(
            data=info_np.T, columns=['Ebins', 'tbins', 'Xbins', 'Ybins', 'Zbins']
        )
        return df_info

    def read_data(self):
        data = self.all_lines[self.data_idx + 1 : -1]
        data_np = np.array([x.split() for x in data], dtype=float)
        cols = self.all_lines[self.data_idx].split()
        cols.remove('Rel')
        if 'Volume' in cols:
            cols.remove('*')
            cols.remove('Vol')
            cols = [w.replace('Rslt', 'ResVol') for w in cols]
        df = pd.DataFrame(data=data_np, columns=cols)
        return df


def read_fmesh(file, mesh_info=False):
    """
    Parameters
    ----------
    file : string
        meshtal file.
    mesh_info : boolean, optional
        if mesh points are desired. The default is False.

    Returns
    -------
    pandas dataframe
        dataframe columns: Energy, X, Y, Result, RelError
        or if mesh_info=True, an additional dataframe is returned
        containing information regarding bins
    """

    idx0 = 0
    e0 = np.array([0])
    t0 = np.array([0])
    totals = []
    with open(file) as myfile:
        for i, line in enumerate(myfile):
            tmp = line.split()
            if ('X direction') in line:
                x0 = np.asarray(tmp[2:], dtype=float)
            if ('Y direction') in line:
                y0 = np.asarray(tmp[2:], dtype=float)
            if ('Z direction') in line:
                z0 = np.asarray(tmp[2:], dtype=float)
            if ('Energy bin boundaries') in line:
                e0 = np.asarray(tmp[3:], dtype=float)
            if ('Time bin boundaries') in line:
                t0 = np.asarray(tmp[3:], dtype=float)
            if 'Result' in tmp and 'Error' in tmp:
                idx0 = i
            if 'Total' in tmp:
                totals.append(i)

    with open(file) as f:
        all_data = f.readlines()

    data0 = all_data[idx0 + 1 :]
    data1 = np.array([np.fromstring(x, dtype=float, sep=' ') for x in data0 if 'Total' not in x])
    cols = all_data[idx0].split()
    cols.remove('Rel')
    if 'Volume' in cols:
        cols.remove('*')
        cols.remove('Vol')
        cols = [w.replace('Rslt', 'ResVol') for w in cols]
    df = pd.DataFrame(data=data1, columns=cols)
    # info
    if mesh_info:
        data_info = [e0, t0, x0, y0, z0]
        info_np = np.array(data_info, dtype=object)
        a = numpy_fillna(info_np)
        df_info = pd.DataFrame(data=a.T, columns=['Ebins', 'tbins', 'Xbins', 'Ybins', 'Zbins'])
        return df_info, df
    else:
        return df


def numpy_fillna(data):
    # Get lengths of each row of data
    lens = np.array([len(i) for i in data])

    # Mask of valid places in each row
    mask = np.arange(lens.max()) < lens[:, None]

    # Setup output array and put elements from data into masked positions
    out = np.zeros(mask.shape, dtype=data.dtype)
    out[mask] = np.concatenate(data)
    return out


def griddata(x, y, z, nbins, xrange=None, yrange=None):
    """
    Parameters
    ----------
    x : numpy array or dataframe
        x-values.
    y : numpy array or dataframe
        y-values.
    z : numpy array or dataframe
        z-values.
    nbins : integer
        number of bins.
    xrange : list, optional
        with minimum and maximum values for x. The default is None.
    yrange : list, optional
        with minimum and maximum values for x. The default is None.

    Returns
    -------
    xx : numpy array
        mesh points.
    result : numpy array
        3D matrix better visualized with imshow.

    """
    if xrange is None:
        lowx = x.min()
        highx = x.max()
    if yrange is None:
        lowy = y.min()
        highy = y.max()
    else:
        lowx = xrange[0]
        highx = xrange[1]
        lowy = yrange[0]
        highy = yrange[1]

    xx = np.linspace(lowx, highx, nbins)
    yy = np.linspace(lowy, highy, nbins)
    xg, yg = np.meshgrid(xx, yy)

    result = gd((x, y), z, (xg, yg))  # , method='cubic')
    return xx, result


def read_output(filename: str | Path):
    filename = Path(filename)
    return ReadOutput(filename)
