import logging
import importlib
from . import neuron_utils
from jupyter_geppetto.geppetto_comm import GeppettoJupyterModelSync
from jupyter_geppetto.geppetto_comm import GeppettoCoreAPI
from optima_ui.singleton import Singleton
from matplotlib import pyplot
import numpy as np


@Singleton
class OptimaMenu:

    def __init__(self):
        logging.debug('Initializing Optima Menu')
        self.items = []
        self.items.append(neuron_utils.add_button('Testing Popup', self.testingPopup))
        self.items.append(neuron_utils.add_button('Testing Plot 1', self.testingPlot1))
        self.items.append(neuron_utils.add_button('Testing Plot 2', self.testingPlot2))
        

        self.loadModelPanel = neuron_utils.add_panel(
            'Example', items=self.items, widget_id='example', position_x=108, position_y=125, width=287, properties={"closable":False})
        self.loadModelPanel.on_close(self.close)
        self.loadModelPanel.display()

    def close(self, component, args):
        # Close Jupyter object
        self.loadModelPanel.close()
        del self.loadModelPanel

        # Destroy this class
        OptimaMenu.delete()
        # del RunControl._instance

    def shake_panel(self):
        self.loadModelPanel.shake()

    def testingPopup(self, triggeredComponent, args):
        try:
            logging.debug(GeppettoJupyterModelSync.current_python_model)

            self.popup = GeppettoCoreAPI.popupVariable('Pop up', variables = ["Lorem ipsum"], position_x=90, position_y=405)

        except Exception as e:
            logging.exception("Unexpected error loading model")
            raise

    def testingPlot1(self, triggeredComponent, args):
        try:
            logging.debug(GeppettoJupyterModelSync.current_python_model)

            t = np.arange(0.0, 2.0, 0.01)
            s = 1 + np.sin(2*np.pi*t)
            pyplot.plot(t, s)

            pyplot.xlabel('time (s)')
            pyplot.ylabel('voltage (mV)')
            pyplot.title('About as simple as it gets, folks')
            pyplot.grid(True)
            pyplot.savefig("test.png")
            pyplot.show()
            

        except Exception as e:
            logging.exception("Unexpected error loading model")
            raise

    def testingPlot2(self, triggeredComponent, args):
        try:
            logging.debug(GeppettoJupyterModelSync.current_python_model)

            self.popup = GeppettoCoreAPI.popupVariable('Pop up', variables = ["Lorem ipsum"], position_x=90, position_y=405)

        except Exception as e:
            logging.exception("Unexpected error loading model")
            raise
