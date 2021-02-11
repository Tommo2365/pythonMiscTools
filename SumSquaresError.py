import serial
import configparser
import argparse
import time
from datetime import datetime
import numpy as np
import keyboard  # using module keyboard
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, draw, show, ion
import statistics

import matplotlib.animation as animation
from matplotlib import style
from tkinter.filedialog import askdirectory
import numpy
import scipy
from scipy.optimize import curve_fit
from pytictoc import TicToc
import easygui
from easygui import msgbox, multenterbox

pi = numpy.pi
#pi =1
def SumSquaresError(xyData, xyDataPrime):
    
    r1 = np.sqrt((np.square(xyData[:,0])+ np.square(xyData[:,1])))

    r2 = np.sqrt((np.square(xyDataPrime[:,0])+ np.square(xyDataPrime[:,1])))
    diff = r2 -r1

    absDiff = abs(diff)

    squareAbsDiff = np.square(absDiff)

    ms = np.sum(squareAbsDiff)

    rms = np.power(ms, 0.5)

    return rms