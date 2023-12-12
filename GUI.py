# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class GUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 457)
        MainWindow.setMinimumSize(QtCore.QSize(600, 457))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(10, 40, 75, 24))
        self.startButton.setObjectName("startButton")
        self.pauseButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(90, 40, 75, 24))
        self.pauseButton.setObjectName("pauseButton")
        self.stopButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(170, 40, 75, 24))
        self.stopButton.setObjectName("stopButton")
        self.removeObjectButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.removeObjectButton.setGeometry(QtCore.QRect(100, 180, 75, 24))
        self.removeObjectButton.setObjectName("removeObjectButton")
        self.addObjectButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addObjectButton.setGeometry(QtCore.QRect(20, 180, 75, 24))
        self.addObjectButton.setObjectName("addObjectButton")
        self.currentSpeedLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.currentSpeedLabel.setGeometry(QtCore.QRect(170, 70, 81, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.currentSpeedLabel.setPalette(palette)
        self.currentSpeedLabel.setObjectName("currentSpeedLabel")
        self.obstacleDistanceLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.obstacleDistanceLabel.setGeometry(QtCore.QRect(10, 100, 101, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.obstacleDistanceLabel.setPalette(palette)
        self.obstacleDistanceLabel.setObjectName("obstacleDistanceLabel")
        self.breakDistanceLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.breakDistanceLabel.setGeometry(QtCore.QRect(10, 130, 141, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.breakDistanceLabel.setPalette(palette)
        self.breakDistanceLabel.setObjectName("breakDistanceLabel")
        self.speedLimitLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.speedLimitLabel.setGeometry(QtCore.QRect(10, 70, 71, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.speedLimitLabel.setPalette(palette)
        self.speedLimitLabel.setObjectName("speedLimitLabel")
        self.mainTitleLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.mainTitleLabel.setGeometry(QtCore.QRect(160, 10, 271, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.mainTitleLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mainTitleLabel.setFont(font)
        self.mainTitleLabel.setObjectName("mainTitleLabel")
        self.currentSpeedField = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.currentSpeedField.setGeometry(QtCore.QRect(260, 70, 41, 21))
        self.currentSpeedField.setObjectName("currentSpeedField")
        self.speedLimitField = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.speedLimitField.setGeometry(QtCore.QRect(80, 70, 41, 21))
        self.speedLimitField.setObjectName("speedLimitField")
        self.obstacleDistanceField = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.obstacleDistanceField.setGeometry(QtCore.QRect(120, 100, 41, 21))
        self.obstacleDistanceField.setObjectName("obstacleDistanceField")
        self.breakDistanceField = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.breakDistanceField.setGeometry(QtCore.QRect(150, 130, 41, 21))
        self.breakDistanceField.setObjectName("breakDistanceField")
        self.resetButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(250, 40, 75, 24))
        self.resetButton.setObjectName("resetButton")
        self.addLeftParaButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addLeftParaButton.setGeometry(QtCore.QRect(40, 260, 75, 24))
        self.addLeftParaButton.setObjectName("addLeftParaButton")
        self.removeLeftParaButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.removeLeftParaButton.setGeometry(QtCore.QRect(120, 260, 75, 24))
        self.removeLeftParaButton.setObjectName("removeLeftParaButton")
        self.addRightParaButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addRightParaButton.setGeometry(QtCore.QRect(40, 310, 75, 24))
        self.addRightParaButton.setObjectName("addRightParaButton")
        self.removeRightParaButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.removeRightParaButton_2.setGeometry(QtCore.QRect(120, 310, 75, 24))
        self.removeRightParaButton_2.setObjectName("removeRightParaButton_2")
        self.addLeftAftButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addLeftAftButton.setGeometry(QtCore.QRect(40, 360, 75, 24))
        self.addLeftAftButton.setObjectName("addLeftAftButton")
        self.removeLeftAftButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.removeLeftAftButton.setGeometry(QtCore.QRect(120, 360, 75, 24))
        self.removeLeftAftButton.setObjectName("removeLeftAftButton")
        self.addRightAftButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addRightAftButton.setGeometry(QtCore.QRect(40, 410, 75, 24))
        self.addRightAftButton.setObjectName("addRightAftButton")
        self.removeRightAftButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.removeRightAftButton.setGeometry(QtCore.QRect(120, 410, 75, 24))
        self.removeRightAftButton.setObjectName("removeRightAftButton")
        self.leftParaLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.leftParaLabel.setGeometry(QtCore.QRect(10, 240, 111, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.leftParaLabel.setPalette(palette)
        self.leftParaLabel.setObjectName("leftParaLabel")
        self.rightParaLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.rightParaLabel.setGeometry(QtCore.QRect(10, 290, 111, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.rightParaLabel.setPalette(palette)
        self.rightParaLabel.setObjectName("rightParaLabel")
        self.leftAftLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.leftAftLabel.setGeometry(QtCore.QRect(10, 340, 111, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.leftAftLabel.setPalette(palette)
        self.leftAftLabel.setObjectName("leftAftLabel")
        self.rightAftLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.rightAftLabel.setGeometry(QtCore.QRect(10, 390, 111, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.rightAftLabel.setPalette(palette)
        self.rightAftLabel.setObjectName("rightAftLabel")
        self.addObjectLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.addObjectLabel.setGeometry(QtCore.QRect(70, 160, 111, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.addObjectLabel.setPalette(palette)
        self.addObjectLabel.setObjectName("addObjectLabel")
        self.addCarLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.addCarLabel.setGeometry(QtCore.QRect(70, 220, 111, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        self.addCarLabel.setPalette(palette)
        self.addCarLabel.setObjectName("addCarLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Collision Avoidance Simulator"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.removeObjectButton.setText(_translate("MainWindow", "Remove"))
        self.addObjectButton.setText(_translate("MainWindow", "Add"))
        self.currentSpeedLabel.setText(_translate("MainWindow", "Current Speed:"))
        self.obstacleDistanceLabel.setText(_translate("MainWindow", "Obstacle Distance:"))
        self.breakDistanceLabel.setText(_translate("MainWindow", "Minimum Break Distance:"))
        self.speedLimitLabel.setText(_translate("MainWindow", "Speed Limit:"))
        self.mainTitleLabel.setText(_translate("MainWindow", "Vehicle Collision Avoidance Simulator"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.addLeftParaButton.setText(_translate("MainWindow", "Add"))
        self.removeLeftParaButton.setText(_translate("MainWindow", "Remove"))
        self.addRightParaButton.setText(_translate("MainWindow", "Add"))
        self.removeRightParaButton_2.setText(_translate("MainWindow", "Remove"))
        self.addLeftAftButton.setText(_translate("MainWindow", "Add"))
        self.removeLeftAftButton.setText(_translate("MainWindow", "Remove"))
        self.addRightAftButton.setText(_translate("MainWindow", "Add"))
        self.removeRightAftButton.setText(_translate("MainWindow", "Remove"))
        self.leftParaLabel.setText(_translate("MainWindow", "Left Parallel:"))
        self.rightParaLabel.setText(_translate("MainWindow", "Right Parallel:"))
        self.leftAftLabel.setText(_translate("MainWindow", "Left Aft:"))
        self.rightAftLabel.setText(_translate("MainWindow", "Right Aft:"))
        self.addObjectLabel.setText(_translate("MainWindow", "Add Object"))
        self.addCarLabel.setText(_translate("MainWindow", "Add Car"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())