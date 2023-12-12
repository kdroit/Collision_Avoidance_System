###########################################################################################
#                  Revision History Table
###########################################################################################
#    DATE    #    AUTHOR      #    WHAT
# 11/22/2023 # John Jenkins   # Created the proposed GUI window with a control panel
# 11/25/2023 # John Jenkins   # Adjusted, removed, and added components to fit new design
# 11/28/2023 # John Jenkins   # Removed the GUI to use the control panel as a widget
#                             # and found a way to add it to Simulation_Display.py
# 11/30/2023 # John Jenkins   # Added the code to allow text inside the Line edit fields
#            #                # Made the Line edit fields for the stopping range and obstacle
#            #                # distance read only. Change "breaking distance" to "stopping range"
#            #                # and adjusted the text field location to fit the name change.
# 12/02/2023 # John Jenkins   # Added functionality to all control buttons by calling
#            #                # defs from Simulation_Logic. Still waiting on Logic for the
#            #                # remove buttons.
# 12/04/2023 # John Jenkins   # Fixed control buttons functionality for definitions in Sim_Display
# 12/04/2023 # Mark Phillippi # Added functions for removing components from the display.
#            #                # created the function to retrieve the stopping distance. Updated
#            #                # field widths to accomodate larger outputs.
# 12/05/2023 # John Jenkins   # Added functionality to disable start button when the stop button
#            #                # is clicked. Reenable start button when reset button is clicked.
# 12/06/2023 # Keith Droit    # Changed import statement for Simulation_Logic
###########################################################################################


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QObject, pyqtSlot
from PyQt6.QtWidgets import QWidget



class Input (QWidget,QObject):
    sl = None

    @pyqtSlot(str)
    def __init__(self, logic, parent=None):
        super().__init__(parent)
        self.sl = logic
        self.Simulation_Logic = logic
        self.setObjectName("MainWindow")
        self.resize(979, 683)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.pauseButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(110, 40, 75, 24))
        self.pauseButton.setObjectName("pauseButton")
        self.pauseButton.setCheckable(True)
        self.pauseButton.clicked.connect(self.pauseClicked)

        self.obstacleDistanceField = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.obstacleDistanceField.setText("")
        self.obstacleDistanceField.setReadOnly(True)
        self.obstacleDistanceField.setGeometry(QtCore.QRect(140, 120, 41, 21))
        self.obstacleDistanceField.setObjectName("obstacleDistanceField")

        self.addLeftAftButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addLeftAftButton.setGeometry(QtCore.QRect(60, 430, 75, 24))
        self.addLeftAftButton.setObjectName("addLeftAftButton")
        self.addLeftAftButton.setCheckable(True)
        self.addLeftAftButton.clicked.connect(self.addleftAft)

        #Updated 12/4/2023 Mark Phillippi
        #dist = self.sl.get_minimum_stopping_distance()
        #dist_string = f"{dist:.3f} Feet"
        self.stoppingRangeField = QtWidgets.QLineEdit(parent=self.centralwidget)
        #self.stoppingRangeField.setText(dist_string)
        self.stoppingRangeField.setReadOnly(True)
        self.stoppingRangeField.setGeometry(QtCore.QRect(178, 150, 41, 21))
        self.stoppingRangeField.setObjectName("stoppingRange")

        self.removeRightParaButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.removeRightParaButton_2.setGeometry(QtCore.QRect(140, 370, 75, 24))
        self.removeRightParaButton_2.setObjectName("removeRightParaButton_2")

        self.speedLimitLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.speedLimitLabel.setGeometry(QtCore.QRect(30, 90, 71, 16))
        # label color
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)

        self.speedLimitLabel.setPalette(palette)
        self.speedLimitLabel.setObjectName("speedLimitLabel")

        self.removeLeftAftButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.removeLeftAftButton.setGeometry(QtCore.QRect(140, 430, 75, 24))
        self.removeLeftAftButton.setObjectName("removeLeftAftButton")

        self.obstacleDistanceLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.obstacleDistanceLabel.setGeometry(QtCore.QRect(30, 120, 101, 16))
        # label color
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)

        self.obstacleDistanceLabel.setPalette(palette)
        self.obstacleDistanceLabel.setObjectName("obstacleDistanceLabel")

        self.addObjectButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addObjectButton.setGeometry(QtCore.QRect(60, 220, 75, 24))
        self.addObjectButton.setObjectName("addObjectButton")
        self.addObjectButton.setCheckable(True)
        self.addObjectButton.clicked.connect(self.addObject)

        self.addRightParaButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addRightParaButton.setGeometry(QtCore.QRect(60, 370, 75, 24))
        self.addRightParaButton.setObjectName("addRightParaButton")
        self.addRightParaButton.setCheckable(True)
        self.addRightParaButton.clicked.connect(self.addrightParallel)

        self.leftAftLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.leftAftLabel.setGeometry(QtCore.QRect(30, 410, 111, 16))
        # label color
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.leftAftLabel.setPalette(palette)
        self.leftAftLabel.setObjectName("leftAftLabel")

        self.rightParaLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.rightParaLabel.setGeometry(QtCore.QRect(30, 350, 111, 16))
        # label color
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.rightParaLabel.setPalette(palette)
        self.rightParaLabel.setObjectName("rightParaLabel")

        self.removeObjectButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.removeObjectButton.setGeometry(QtCore.QRect(140, 220, 75, 24))
        self.removeObjectButton.setObjectName("removeObjectButton")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 10, 271, 21))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)

        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.addObjectLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.addObjectLabel.setGeometry(QtCore.QRect(110, 200, 111, 16))
        # label color
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.addObjectLabel.setPalette(palette)
        self.addObjectLabel.setObjectName("addObjectLabel")

        self.addLeftParaButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addLeftParaButton.setGeometry(QtCore.QRect(60, 310, 75, 24))
        self.addLeftParaButton.setObjectName("addLeftParaButton")
        self.addLeftParaButton.setCheckable(True)
        self.addLeftParaButton.clicked.connect(self.addleftParallel)

        self.removeRightAftButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.removeRightAftButton.setGeometry(QtCore.QRect(140, 490, 75, 24))
        self.removeRightAftButton.setObjectName("removeRightAftButton")

        self.stopButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(190, 40, 75, 24))
        self.stopButton.setObjectName("stopButton")
        self.stopButton.setCheckable(True)
        self.stopButton.clicked.connect(self.stopClicked)

        self.rightAftLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.rightAftLabel.setGeometry(QtCore.QRect(30, 470, 111, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        # label color
        self.rightAftLabel.setPalette(palette)
        self.rightAftLabel.setObjectName("rightAftLabel")

        self.currentSpeedLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.currentSpeedLabel.setGeometry(QtCore.QRect(190, 90, 81, 16))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.currentSpeedLabel.setPalette(palette)
        self.currentSpeedLabel.setObjectName("currentSpeedLabel")

        self.currentSpeedField = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.currentSpeedField.setGeometry(QtCore.QRect(270, 90, 41, 21))
        self.currentSpeedField.setObjectName("currentSpeedField")

        self.speedLimitField = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.speedLimitField.setText("")
        self.speedLimitField.setGeometry(QtCore.QRect(100, 90, 41, 21))
        self.speedLimitField.setObjectName("speedLimitField")

        self.startButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(30, 40, 75, 24))
        self.startButton.setObjectName("startButton")
        self.startButton.setCheckable(True)
        self.startButton.clicked.connect(self.startClicked)

        self.addCarLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.addCarLabel.setGeometry(QtCore.QRect(110, 260, 111, 16))
        # label color
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.addCarLabel.setPalette(palette)
        self.addCarLabel.setObjectName("addCarLabel")

        self.resetButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(270, 40, 75, 24))
        self.resetButton.setObjectName("resetButton")
        self.resetButton.setCheckable(True)
        self.resetButton.clicked.connect(self.resetClicked)

        self.stoppingRangeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.stoppingRangeLabel.setGeometry(QtCore.QRect(30, 150, 141, 16))
        # label color
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.stoppingRangeLabel.setPalette(palette)
        self.stoppingRangeLabel.setObjectName("stoppingRangeLabel")

        self.removeLeftParaButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.removeLeftParaButton.setGeometry(QtCore.QRect(140, 310, 75, 24))
        self.removeLeftParaButton.setObjectName("removeLeftParaButton")

        self.addRightAftButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addRightAftButton.setGeometry(QtCore.QRect(60, 490, 75, 24))
        self.addRightAftButton.setObjectName("addRightAftButton")
        self.addRightAftButton.setCheckable(True)
        self.addRightAftButton.clicked.connect(self.addrightAft)

        self.leftParaLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.leftParaLabel.setGeometry(QtCore.QRect(30, 290, 111, 16))
        # label color
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.leftParaLabel.setPalette(palette)
        self.leftParaLabel.setObjectName("leftParaLabel")

        self.statusbar = QtWidgets.QStatusBar(parent=self)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(self)


    # Definitons for buttons
    def startClicked(self):
        self.parent().startAnimation()
    def pauseClicked(self):
        self.parent().pauseAnimation()
    def stopClicked(self):
        self.parent().stopAnimation()
        self.startButton.setEnabled(False)
    def resetClicked(self):
        self.parent().resetSimulation()
        #Simulation_Logic.reset()
        self.startButton.setEnabled(True)
    def addObject(self):
        self.Simulation_Logic.add_object()
    def addrightParallel(self):
        car = self.Simulation_Logic.add_car("Right")
        self.parent().addCar(car)
    def addrightAft(self):
        car = self.Simulation_Logic.add_car("Right Aft")
        self.parent().addCar(car)
    def addleftParallel(self):
        car = self.Simulation_Logic.add_car("Left")
        self.parent().addCar(car)
    def addleftAft(self):
        car = self.Simulation_Logic.add_car("Left Aft")
        self.parent().addCar(car)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.addLeftAftButton.setText(_translate("MainWindow", "Add"))
        self.removeRightParaButton_2.setText(_translate("MainWindow", "Remove"))
        self.speedLimitLabel.setText(_translate("MainWindow", "Speed Limit:"))
        self.removeLeftAftButton.setText(_translate("MainWindow", "Remove"))
        self.obstacleDistanceLabel.setText(_translate("MainWindow", "Obstacle Distance:"))
        self.addObjectButton.setText(_translate("MainWindow", "Add"))
        self.addRightParaButton.setText(_translate("MainWindow", "Add"))
        self.leftAftLabel.setText(_translate("MainWindow", "Left Aft:"))
        self.rightParaLabel.setText(_translate("MainWindow", "Right Parallel:"))
        self.removeObjectButton.setText(_translate("MainWindow", "Remove"))
        self.label.setText(_translate("MainWindow", "Vehicle Collision Avoidance Simulator"))
        self.addObjectLabel.setText(_translate("MainWindow", "Add Object"))
        self.addLeftParaButton.setText(_translate("MainWindow", "Add"))
        self.removeRightAftButton.setText(_translate("MainWindow", "Remove"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.rightAftLabel.setText(_translate("MainWindow", "Right Aft:"))
        self.currentSpeedLabel.setText(_translate("MainWindow", "Current Speed:"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.addCarLabel.setText(_translate("MainWindow", "Add Car"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.stoppingRangeLabel.setText(_translate("MainWindow", "Minimum Stopping Range:"))
        self.removeLeftParaButton.setText(_translate("MainWindow", "Remove"))
        self.addRightAftButton.setText(_translate("MainWindow", "Add"))
        self.leftParaLabel.setText(_translate("MainWindow", "Left Parallel:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Input()
    widget.show()
    sys.exit(app.exec())
