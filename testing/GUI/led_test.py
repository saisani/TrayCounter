from gpiozero import LED
from signal import pause

red = LED(4)

red.blink()

pause()
