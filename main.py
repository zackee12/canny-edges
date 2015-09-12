from PyQt4 import QtGui
import sys
from ui.mainform import MainForm


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec_())


