from gpiozero import LineSensor, DigitalInputDevice
from signal import pause
from time import sleep

def found():
    print("hehwerewrewr")

def nofound():
    print("adsadsadsad")

# sensor = LineSensor(4)

# sensor.when_line = found
# sensor.when_no_line = nofound

sensor = DigitalInputDevice(4)

sensor.when_activated = found
sensor.when_deactivated = nofound

sleep(1)

while True:
    print("Sensor value: ", sensor.active_state)
    sleep(1)


#pause()