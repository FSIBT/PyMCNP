# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 12:00:34 2020

@author: mauricio
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import apipandas as api
from scipy.stats import gaussian_kde

def create_smooth_energy_spectra(energies, E=None, sigma=0.005):
    """Takes a list of energies and uses a gaussian_kde to create a smoothed spectra

    Returned a list of smoothed values and energies. The bandwidth
    parameter, sigma, is set to 0.01 by default (this should be
    smaller than the energy spread of the detector, but large enough
    to get good smoothing.

    The values are suchs that the sum of the values gives the number
    of energies used in the KDE.  The KDE is samples on energies, E,
    that are either given or present a linspace between 0-10 MeV with
    2048 values.

    Parameters
    ----------

    energies : list or np.array
        List or numpy array of energy values in MeV
    E : None or list or np.array
        Values at which the new smoothed spectrum should be sampled.
        If None, we create our own: 0-10 MeV in 2048 steps
    sigma : float
        The width of the sigma for the gaussian KDE

    Returns
    -------

    E :
        The list of values where the spectra got sampled
    values :
        The values of the smoothed spectra. The spectra is normalized, so that
        the sum of the values equals the number of events.
    """
    if E is None:
        E = np.linspace(0, 10, 2048)

    kde = gaussian_kde(energies, sigma)
    values = kde(E)

    # normalize kde and then scale to correct integral
    values = values / values.sum() * len(energies)

    return E, values

def cal_spectrum1(channels, energy, hist_edges):
    a,b = np.polyfit(channels,energy,1)
    E = a*hist_edges + b
    return a,b,E

def cal_spectrum2(channels, energy, hist_edges):
    a,b,c = np.polyfit(channels,energy,2)
    E = a*hist_edges**2 + b*hist_edges + c
    return a,b,c,E