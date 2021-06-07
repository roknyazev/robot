from PyQt5.QtCore import QObject, QThread, pyqtSlot, pyqtSignal
import serial
import time
import keyboard


def func(i):
    global code
    code = i


code = "0"

keyboard.add_hotkey('Space', func, ["0"])
keyboard.add_hotkey('Up', func, ["1"])
keyboard.add_hotkey('Down', func, ["2"])
keyboard.add_hotkey('Right', func, ["3"])
keyboard.add_hotkey('Left', func, ["4"])


class ThreadForIntegrator(QThread, QObject):
    def __init__(self):
        super().__init__()

    def run(self):
        ser = serial.Serial('COM3', 9600)
        time.sleep(2)
        while True:

            s = ser.readline()
            try:

                ser.write((code + "\n").encode())
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
