from gpiozero import LineSensor, DigitalInputDevice
from signal import pause
from time import sleep

def found():
    print("Line has been broken")

def nofound():
    print("Line is intact")

sensor = LineSensor(4)

sensor.when_line = nofound
sensor.when_no_line = found

pause()
