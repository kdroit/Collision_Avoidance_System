###############################################
#         Revision History Table
###############################################
#    Date    #    Author   #    What
# 11/26/2023 # Keith Droit # Created main.py
###############################################

from PyQt6.QtWidgets import QApplication
from Simulation_Display import Simulation_Display

# Startup
app = QApplication([])

window = Simulation_Display()
window.show()

# Start the event loop
app.exec()