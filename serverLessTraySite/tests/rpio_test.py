import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

print("Mode used: ", GPIO.getmode())

GPIO.setup(4, GPIO.IN)

while True:
    print("Value of input: ", GPIO.input(4))
    time.sleep(1)