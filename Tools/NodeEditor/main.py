import sys
import ui.ui_main
from MainWindow import FFMainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = FFMainWindow()
    #ui = ui.ui_main.Ui_MainWindow()
    #ui.setupUi(MainWindow)

    MainWindow.setUp()
    #centerWidget = MainWindow.takeCentralWidget()
    #MainWindow.setCentralWidget(None)
    MainWindow.setDockNestingEnabled(True)
    MainWindow.show()
    sys.exit(app.exec_())