# qt.io
# https://build-system.fman.io/qt-designer-download
# https://www.riverbankcomputing.com/software/pyqt/download5

# pip install PyQt5
# pyuic5 messenger.ui -o clientui.py


from PyQt5 import QtWidgets
import clientui


class ExampleApp(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # button.pressed.connect
        # timer = QtCore.QTimer()
        # timer.timeout.connect


app = QtWidgets.QApplication([])
window = ExampleApp()
window.show()
app.exec_()
