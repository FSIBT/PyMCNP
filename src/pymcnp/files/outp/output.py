"""
Read MCNP Output files
"""

from datetime import datetime
import numpy as np
import pandas as pd
from scipy.interpolate import griddata as gd


class ReadOutput:
    def __init__(self, filename):
        self.filename = filename
        self.df_info = 0
        self.all_lines = self.read_entire_file()
        self.get_tally_info()

    def read_entire_file(self):
        with open(self.filename) as f:
            allf = f.readlines()
        return allf

    def read_tally(self, n=0, tally_type="e"):
        start = -1
        if tally_type == "e":
            key_word = "energy"
        start_line = list(self.df_info["line_number"])[n]

        for i, line in enumerate(self.all_lines[start_line:]):
            l = line.split()
            if key_word in l:
                start = start_line + i
            if "total" in l and start != -1:
                end = start_line + i
                break
        corpus = self.all_lines[start + 1 : end]
        corpus_np = np.array([x.split() for x in corpus], dtype=float)
        df = pd.DataFrame(columns=["energy", "cts", "error"], data=corpus_np)
        return df

    def get_runtime(self):
        # in development
        outp = open(self.filename).read().split("\n")

        time1 = ""
        time2 = ""
        for line in outp:
            if "mcnp" in line and "version 6" in line and "probid" in line:
                string = line.replace("     ", " ").split(" ")
                time1 = string[10]
                time2 = string[19]
            if "computer" in line and "time" in line:
                cpt = line

        datetime2 = datetime.strptime(time2, "%H:%M:%S")
        datetime1 = datetime.strptime(time1, "%H:%M:%S")
        diff = datetime1 - datetime2
        # real_time = "real time: " + time.strftime("%H:%M:%S", time.gmtime(diff.seconds))
        real_time = f"real time: {round(diff.seconds/60,1)} minutes"
        computer_time = cpt[1:]
        return real_time, computer_time

    def get_nps(self):
        print("Reading output file...")
        nps = 0
        with open(self.filename) as myfile:
            for i, l in enumerate(myfile):
                tmp = l.split()
                if "run" in tmp and "terminated" in tmp:
                    nps = tmp[3]
                    print(tmp)
                    break
        print("Done reading")
        print(f"Number of simulated particles: {nps}")
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
            l = line.lower().split()
            if "print" in l and "table" in l and "110" in l:
                start = i
            if "nps" in l and start != -1:
                col_line = i
                break
        col_names = allf[col_line].split()
        corpus = allf[col_line + 2 : col_line + 2 + 50]
        corpus_np = np.array([x.split() for x in corpus], dtype=float)
        df = pd.DataFrame(columns=col_names, data=corpus_np)
        return df

    def get_tally_info(self):
        lidx, pidx, ix_angle = [], [], []
        surf, tagix, uncol = [], [], []
        tally_type, particle, surface = [], [], []
        uncollided, user_bin, l_angle = [], [], []

        print("Reading output file...")
        for i, l in enumerate(self.all_lines):
            tmp = l.split()
            if "tally" in tmp and "type" in tmp:
                lidx.append(i)
                tally_type.append(l)
            if "particle(s):" in tmp:
                pidx.append(i)
                particle.append(tmp)
            if "surface" in tmp and len(tmp) == 2 and len(lidx) > 0 and i >= min(lidx):
                surf.append(i)
                surface.append(tmp)
            if "angle" in tmp and "bin:" in tmp:
                l_angle.append(tmp)
                ix_angle.append(i)
            if "uncollided" in tmp and "flux" in tmp:
                uncol.append(i)
                uncollided.append(l)
            if "user" in tmp and "bin" in tmp:
                tagix.append(i)
                user_bin.append(l.split()[-1])
        print("Done reading")
        if len(surface) > 0 and len(user_bin) > 0:
            tot_subtly = len(user_bin)
        else:
            tot_subtly = len(surface) + len(uncollided) + len(user_bin)
        print("--" * 20)
        print(f"Number of tallies: {len(lidx)}")
        print(f"Number of subtallies: {tot_subtly}")
        print("--" * 20)
        ttype = tally_type[0].split()

        # initialize dataframe
        cols = [
            "tally_type",
            "description",
            "particle",
            "surfaces",
            "angle_bin",
            "flux",
            "user_bin",
            "line_number",
        ]
        df = pd.DataFrame(columns=cols)
        sur, ang, unc, ub = 0, 0, 0, 0
        if len(surface) > 0 and len(user_bin) == 0:
            if len(ix_angle) == 0:
                sur = surface
                for ix, s in zip(surf, sur):
                    dat0 = [
                        "F" + ttype[2],
                        " ".join(ttype[3:]),
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
                        "F" + ttype[2],
                        " ".join(ttype[3:]),
                        particle[0][1],
                        s[1],
                        " ".join(a[2:]),
                        unc,
                        ub,
                        ix,
                    ]
                    ser0 = pd.Series(dat0, index=df.columns)
                    df.loc[len(df)] = ser0

        if len(uncollided) > 0:
            uncol_idx = uncol
            flux = "collided flux"
            unc = uncollided
            for l, p in zip(lidx, particle):
                dat0 = [
                    "F" + ttype[2],
                    " ".join(ttype[3:]),
                    p[1],
                    sur,
                    ang,
                    flux,
                    ub,
                    l,
                ]
                ser0 = pd.Series(dat0, index=df.columns)
                df.loc[len(df)] = ser0
            for line, ix, p in zip(unc, uncol_idx, particle):
                dat0 = [
                    "F" + ttype[2],
                    " ".join(ttype[3:]),
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
                    "F" + ttype[2],
                    " ".join(ttype[3:]),
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
                    "F" + ttype[2],
                    " ".join(ttype[3:]),
                    particle[0][1],
                    s[1],
                    " ".join(a[2:]),
                    unc,
                    line,
                    ix,
                ]
                ser0 = pd.Series(dat0, index=df.columns)
                df.loc[len(df)] = ser0

        if tot_subtly == 0:
            for l in lidx:
                dat0 = [
                    "F" + ttype[2],
                    " ".join(ttype[3:]),
                    particle[0][1],
                    sur,
                    ang,
                    unc,
                    ub,
                    l,
                ]
                ser0 = pd.Series(dat0, index=df.columns)
                df.loc[len(df)] = ser0

        # drop all zero columns
        df = df.loc[:, (df != 0).any(axis=0)]
        self.df_info = df


# This function should be implemented separately under the ptrac reader
def read_ptrac_surf(files, surfaces=["5.1", "5.2", "5.3"], event_types=["3000", "9000"]):
    # surface crossing event (3000) and last event for given history (9000)
    det = []
    det_info = []
    for file in files:
        elem_det = []
        idx_det = []
        with open(file) as f:
            # file = f.readlines()
            for i, l in enumerate(f):
                line = l.split()
                if line[0] in event_types and line[2] in surfaces:
                    idx_det.append(i)
                    elem_det.append(line[2])

        with open(file) as f:
            file = f.readlines()

        for d in idx_det:
            tmp = np.array(file[d + 1].split(), dtype=float)
            info = np.array(file[d].split(), dtype=float)
            if len(info) == 8:
                det_info.append(info)
            if len(tmp) == 9:
                det.append(tmp)

    cols_i = ["event", "node", "ZA", "MTP", "particle", "cell", "material", "ncp"]
    df_i = pd.DataFrame(data=det_info, columns=cols_i)
    cols = ["x", "y", "z", "u", "v", "w", "energy", "wgt", "tme"]
    df = pd.DataFrame(data=det, columns=cols)

    df["tme"] = df["tme"] * 10  # ns
    return df_i, df


class ReadFmesh:
    def __init__(self, filename):
        self.filename = filename
        self.df_info = 0
        self.all_lines = self.read_entire_file()
        self.get_tally_info()


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
        for i, l in enumerate(myfile):
            tmp = l.split()
            if ("X direction") in l:
                x0 = np.asarray(tmp[2:], dtype=float)
            if ("Y direction") in l:
                y0 = np.asarray(tmp[2:], dtype=float)
            if ("Z direction") in l:
                z0 = np.asarray(tmp[2:], dtype=float)
            if ("Energy bin boundaries") in l:
                e0 = np.asarray(tmp[3:], dtype=float)
            if ("Time bin boundaries") in l:
                t0 = np.asarray(tmp[3:], dtype=float)
            if "Result" in tmp and "Error" in tmp:
                idx0 = i
            if "Total" in tmp:
                totals.append(i)

    with open(file) as f:
        all_data = f.readlines()

    data0 = all_data[idx0 + 1 :]
    data1 = np.array(
        [np.fromstring(x, dtype=float, sep=" ") for x in data0 if "Total" not in x]
    )
    cols = all_data[idx0].split()
    cols.remove("Rel")
    if "Volume" in cols:
        cols.remove("*")
        cols.remove("Vol")
        cols = [w.replace("Rslt", "ResVol") for w in cols]
    df = pd.DataFrame(data=data1, columns=cols)
    # info
    if mesh_info:
        data_info = [e0, t0, x0, y0, z0]
        info_np = np.array(data_info, dtype=object)
        a = numpy_fillna(info_np)
        df_info = pd.DataFrame(
            data=a.T, columns=["Ebins", "tbins", "Xbins", "Ybins", "Zbins"]
        )
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
    if xrange == None:
        lowx = x.min()
        highx = x.max()
    if yrange == None:
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