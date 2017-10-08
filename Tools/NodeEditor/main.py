import sys
import ui.ui_main
from Main.MainWindow import FFMainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    MainWindow = FFMainWindow()

    MainWindow.setUp()
    MainWindow.setDockNestingEnabled(True)
    MainWindow.show()

    sys.exit(app.exec_())