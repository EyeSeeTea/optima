"""
GeppettoNeuron.py
Initialise geppetto neuron, listeners and variables
"""
import logging
from collections import defaultdict
import threading
import time
from jupyter_geppetto.geppetto_comm import GeppettoJupyterModelSync
from jupyter_geppetto.geppetto_comm import GeppettoJupyterGUISync

from optima_ui.optima_menu import OptimaMenu
from optima_ui.optima_matplotlib import OptimaMatplotlib


from optima_ui import neuron_utils


def init():
    try:
        # Configure log
        neuron_utils.configure_logging()

        logging.debug('Initialising Optima Demo')

        # Reset any previous value
        logging.debug('Initialising Sync Mechanism')
        # GeppettoJupyterGUISync.sync_values = defaultdict(list)
        # GeppettoJupyterModelSync.record_variables = defaultdict(list)
        # GeppettoJupyterModelSync.current_project = None
        # GeppettoJupyterModelSync.current_experiment = None
        # GeppettoJupyterModelSync.current_model = None
        # GeppettoJupyterModelSync.current_python_model = None
        GeppettoJupyterModelSync.events_controller = GeppettoJupyterModelSync.EventsSync()

        # Init Panels
        logging.debug('Initialising Optima')
        OptimaMenu.Instance()
        OptimaMatplotlib.Instance()

    except Exception as exception:
        logging.exception("Unexpected error in neuron_geppetto initialization:")
        raise
