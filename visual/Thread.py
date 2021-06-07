from PyQt5.QtCore import QObject, QThread, pyqtSlot, pyqtSignal
import serial
import time


class ThreadForIntegrator(QThread, QObject):
    def __init__(self):
        super().__init__()

    def run(self):
        ser = serial.Serial('COM3', 9600)
        time.sleep(2)
        while True:
            s = ser.readline()
            try:
                s = s.decode('ascii')
                v = float(s[0:4])
                a = float(s[6:-1])
                x = [a, v]
                self.slot(x)
            except Exception:
                continue

    @pyqtSlot(name='call_function')
    def slot(self, results):
        sender.data.emit(results)


class Sender(QObject):
    data = pyqtSignal(list)


sender = Sender()
