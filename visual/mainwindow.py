from PyQt5.QtWidgets import *
import form
import pyqtgraph as pg
import Thread
import numpy as np


class MainWindow(QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.thread_instance = Thread.ThreadForIntegrator()
        Thread.sender.data.connect(self.upd)
        self.pushButton.clicked.connect(self.simulation)

        self.widget = self.label
        self.widget.setLayout(QGridLayout())
        self.widget.layout().setContentsMargins(0, 0, 0, 0)
        self.widget.layout().setSpacing(0)

        self.plt1 = pg.plot()
        self.plt1.setAspectLocked()
        self.plt1.showGrid(x=False, y=False)
        self.plt1.addLegend()
        self.plt1.addLine(x=0, pen=0.2)
        self.plt1.addLine(y=0, pen=0.2)
        circle = pg.QtGui.QGraphicsEllipseItem(-2, -2, 2 * 2, 2 * 2)
        circle.setPen(pg.mkPen(0.2))
        self.plt1.addItem(circle)

        self.orbit = self.plt1.plot([0], [0], pen=pg.mkPen('y', width=5), name=' Distance')

        self.widget.layout().addWidget(self.plt1, 0, 0)

        self.x = [[], []]

    def simulation(self):
        self.thread_instance.start()

    def upd(self, data):
        self.x[0].append(data[1] * np.cos(data[0] * np.pi / 180))
        self.x[1].append(data[1] * np.sin(data[0] * np.pi / 180))
        if len(self.x[0]) > 20:
            self.x[0].pop(0)
            self.x[1].pop(0)
        self.time.setNum(data[0])
        self.orbit.setData(self.x[0], self.x[1])
