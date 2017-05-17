import logging
from optima_ui import neuron_utils
from math import sqrt, pow

from jupyter_geppetto.geppetto_comm import GeppettoCoreAPI as G
from jupyter_geppetto.geppetto_comm import GeppettoJupyterModelSync

from optima_ui.singleton import Singleton

from matplotlib import pyplot
import numpy as np

@Singleton
class OptimaMatplotlib:

    def __init__(self):
        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2*np.pi*t)
        pyplot.plot(t, s)

        pyplot.xlabel('time (s)')
        pyplot.ylabel('voltage (mV)')
        pyplot.title('About as simple as it gets, folks')
        pyplot.grid(True)
        pyplot.savefig("test.png")
        pyplot.show()
