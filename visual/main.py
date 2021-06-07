import sys
from PyQt5.QtWidgets import QApplication
import mainwindow

app = QApplication(sys.argv)
form = mainwindow.MainWindow()
form.showMaximized()
sys.exit(app.exec_())
